import serial
import math

def equation(x):
    #return 3 * x**3 - 6 * x**2 - 5 * x - 3
    #return 7*math.cos(x)-8*x
    #return -6*x**3+2*x**2+5*x-9
    return 5*math.cos(x)-7*x

def derivative(x):
    #return 9*x**2-12*x-5
    #return -7*math.sin(x)-8
    #return -18*x**2+4*x+5
    return -5*math.sin(x)-7

def newtonsMethod(iterations, initialGuess):
    currentValue = initialGuess
    currentIteration = 0
    while (currentIteration < iterations):
        functionValue = equation(currentValue)
        derivativeValue = derivative(currentValue)
        currentValue = currentValue - functionValue/derivativeValue
        print("Iteration: " + str(currentIteration + 1) + " Value: " + str(currentValue) + " |===> Func value: " + str(functionValue) + " | Derivative Value:" + str(derivativeValue))
        currentIteration += 1


newtonsMethod(7, 1)

