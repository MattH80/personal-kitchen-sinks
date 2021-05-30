import math

def recursive(iterations: int, startingTerm: int):

    previousTerm = startingTerm
    for i in range(1, iterations):
        previousTerm = 5 + math.sqrt(3 + previousTerm)
        print(previousTerm)
    


recursive(100, 6)
