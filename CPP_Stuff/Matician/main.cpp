/*ASSUMPTIONS: 
* (2n*100)ms does not exceeded max value of a 32 bit integer
*/

#include <iostream>
#include "mtmcu_registers.h"
#include <cmath>
#include <ctime>


//Macros to improve readability of the code
#define isBitSet(byte, bit) (byte & (1 << bit))
#define isBitClear(byte, bit) !(byte & (1 << bit))
#define toggleBit(byte, bit) (byte ^= (1 << bit))

/*
* State machine inits. Due to the low complexity of this task, enums will suffice
* However, solutions involving a dedicated class for each state are much more elegant and useful in non-trivial applications.
*/
enum State {OFFstate, Xstate, Ystate};
State previousState;
State currState;
volatile bool pendingStateChange = false;
const int stateThreshold = 3000; //3000ms = 3s

/*Interrupt Inits*/
volatile long double timeButtonHoldStart = 0;
volatile long double timeButtonHoldEnd = 0;
volatile bool buttonIsHeld = false;
void ISR_TimerCallBack_YState(void);
void ISR_TimerCallBack_XState(void);

//Note: The requirments ask for this to all be in one file
//I wouldn't do this an IRL situation though... this should be split into multiple files.
//It would be better to derive GPIOout and GPIOin from a base GPIO class, but it would make this file very messy.
class GPIOout
{
    public:
    GPIOout(uint16_t pinNumber)
    {
        this->pinNumber = pinNumber;
        GPIO->DIR |= (1 << this->pinNumber);
    }

    void setState(bool state)
    {
        if(isBitSet(GPIO->DIR, this->pinNumber) != state)
        {
            toggleBit(GPIO->DIR, this->pinNumber);
        }
    }

    private:
    uint16_t pinNumber;
};

class GPIOin
{
    public:
    GPIOin(uint16_t pinNumber, bool enablePullup)
    {
        this->pinNumber = pinNumber;
        GPIO->DIR &= ~(1 << this->pinNumber);
        if(enablePullup)
        {
            GPIO->PU |= (1 << this->pinNumber);
        }
    }

    bool getPinState() const
    {
        return isBitSet(GPIO->IDR, this->pinNumber);
    }

    void toggleRisingEdgeInterrupt(bool set)
    {  
        if(isBitSet(GPIO->PCIC, this->pinNumber + 16) != set)
        {
            toggleBit(GPIO->PCIC, this->pinNumber + 16);
        }
    }

    void toggleFallingEdgeInterrupt(bool set)
    {
        if(isBitSet(GPIO->PCIC, this->pinNumber) != set)
        {
            toggleBit(GPIO->PCIC, this->pinNumber);
        }
    }

    
    private:
    uint16_t pinNumber;
};

//Group everything under a namespace so it is clear what items are state-specific. 
//A class with singleton implementations for each state would be better here though, but make this file very long...
namespace stateManager
{
    void OFF()
    {
        //Put the MCU in low power mode
        __wait_for_interrupt();
        //Program will not execute past this line unless interrupt is called.
        while(buttonIsHeld);
        currState = previousState;
    }

    void X()
    {
        /*I was not sure how to implement the 17Hz Green LED peripheral. As such, the code below only implements the Red and Blue LED's*/

        TIMER->CTRL &= ~TIMER_CTRL_TMEN;
        TIMER->PSC = int(pow(10, 4)); //1000 Hz clock
        TIMER->VAL = 0; //Set intial counter to 0
        TIMER->CPR = 1; //0.001 second period in the X state
        TIMER->CTRL |= TIMER_CTRL_CPMIE;
        TIMER->CTRL = intptr_t(ISR_TimerCallBack_XState);
        TIMER->CTRL |= TIMER_CTRL_TMEN; //Enable the timer

        //State change while loop
        while(!pendingStateChange);
        if(timeButtonHoldEnd-timeButtonHoldStart >= stateThreshold)
        {
            currState = OFFstate;
        }
        else
        {
            currState = Ystate;
        }

        TIMER->CTRL &= ~TIMER_CTRL_TMEN; //Turn off timer to clean up
    }
    volatile uint8_t redLEDcounterms = 0;
    volatile bool redLEDbool = true;
    const uint8_t redLEDcountupInterval = 50;

    volatile uint8_t blueLEDcounterms = 0;
    volatile uint32_t blueLEDcomparems = 100; 
    volatile bool blueLEDbool = true;
    const uint8_t blueLEDcountupInterval = 100;

    void Y()
    {
        //Turn off the timer to prevent undefined behaviour when adjusting prescalars :O
        TIMER->CTRL &= ~TIMER_CTRL_TMEN;
        TIMER->PSC = int(pow(10, 6)); //10 Hz clock with 10^6 prescalar
        TIMER->VAL = 0; //Set intial counter to 0
        TIMER->CPR = 10; //1 second period in the Y state
        TIMER->CTRL |= TIMER_CTRL_CPMIE;
        TIMER->CTRL = (intptr_t)ISR_TimerCallBack_YState;
        TIMER->CTRL |= TIMER_CTRL_TMEN; //Enable the timer


        while(!pendingStateChange);
        if(timeButtonHoldEnd-timeButtonHoldStart >= stateThreshold)
        {
            currState = OFFstate;
        }
        else
        {
            currState = Xstate;
        }

        TIMER->CTRL &= ~TIMER_CTRL_TMEN; //Turn off timer to clean up
    }

    volatile uint32_t YStateCounter = 0;
}


//Note: Datasheet specifies GPIO->DIR is reset on startup
GPIOout redLED(0);
GPIOout greenLED(1);
GPIOout blueLED(2);
GPIOin button(3, true);

void setLEDFromBits(uint8_t byte)
{
    redLED.setState(isBitSet(byte, 0));
    greenLED.setState(isBitSet(byte, 1));
    blueLED.setState(isBitSet(byte, 2));
}



void ISR_ButtonCallBack(void)
{
    const volatile long double sysTime = time(0); //Create read-only system time variable for ms
    if(!button.getPinState()) //There is a pullup on the pin, so if the pin is driven LOW it is held down
    {
        timeButtonHoldStart = sysTime;
        buttonIsHeld = true;
    }
    else
    {
        timeButtonHoldEnd = sysTime;
        buttonIsHeld = false;
        pendingStateChange = true;
    }
    
}

//Y State timer callback, called at 1 second intervals
void ISR_TimerCallBack_YState(void)
{
    setLEDFromBits(stateManager::YStateCounter);
    stateManager::YStateCounter++;
}

void ISR_TimerCallBack_XState(void)
{
    redLED.setState(stateManager::redLEDbool);
    stateManager::redLEDcounterms++;
    if(stateManager::redLEDcounterms = stateManager::redLEDcountupInterval)
    {
        stateManager::redLEDcounterms = 0;
        stateManager::redLEDbool = !stateManager::redLEDbool;
    }

    blueLED.setState(stateManager::blueLEDbool);
    stateManager::blueLEDcounterms++;

    if(stateManager::blueLEDcounterms = stateManager::blueLEDcomparems)
    {
        stateManager::blueLEDcounterms = 0;
        stateManager::blueLEDbool = !stateManager::blueLEDbool;
        stateManager::blueLEDcomparems += stateManager::blueLEDcountupInterval;
    }
}


void init(void)
{
    previousState = Xstate;
    currState = OFFstate;

    //Interrupt code
    __enable_interrupts();
    GPIO->ISRA = intptr_t(&ISR_ButtonCallBack); 
    button.toggleRisingEdgeInterrupt(true);
    button.toggleFallingEdgeInterrupt(true);
}

int main(void)
{
    init();
    //while(true and true);

    while(true) {
            switch (currState)
            {
                case OFFstate:
                    stateManager::OFF();
                    break;
                case Xstate:
                    stateManager::X();
                    break;
                case Ystate:
                    stateManager::Y();
                    break;
            }
            previousState = currState;
    }

    return 0;
}