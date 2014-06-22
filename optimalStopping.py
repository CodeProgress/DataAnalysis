#optimal stopping

import random
import pylab


def pick_val(values, stoppingPoint):
    """Strategy: read through values until the index = stoppingPoint
    keep track of the highest value reached so far.
    Continue iterating through values until a higher number is observed.
    Return this value.
    If a higher value is not reached, return the last value.
    values: List of integers
    stoppingPoint: integer between min(values) and max(values)
    """
    best = values[0]
    for i in range(len(values)):
        if i < stoppingPoint:
            if values[i] > best:
                best = values[i]
        else:
            if values[i] > best:
                return values[i]
    return values[-1]

def sim_outcome(numVals, stoppingPoint, numTrials):
    """returns the average result over numTrials"""
    total = 0.
    for i in range(numTrials):
        values = random.sample(xrange(numVals), numVals)
        #values = [random.randint(0, numVals-1) for x in range(numVals)]
        total += pick_val(values, stoppingPoint)
    return total/numTrials    

numVals = 101
pylab.plot([sim_outcome(numVals, x, 200) for x in range(numVals)])
pylab.xlabel("Stopping Point")
pylab.ylabel("Expected Outcome")
pylab.xticks(range(0,numVals, 5))
pylab.show()

