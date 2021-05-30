import serial
from time import sleep
#Tutorial: https://www.instructables.com/id/Interface-Python-and-Arduino-with-pySerial/

baudRate = 9600
serialRead = serial.Serial("COM8", baudRate) #Create connection on serial port

counter = 32

def readFromSerial():
    firstString = serialRead.readline().strip()
    secondString = serialRead.readline().strip()
    if(firstString[0] == 'x'):
        xAngle = firstString[1:4]
        yAngle = secondString[1:4]
    else:
        xAngle = firstString[1:4]
        yAngle = secondString[1:4]
    
    print(xAngle)
    print("x")
    print(yAngle)
    print("y")
    




while True:
    readFromSerial()