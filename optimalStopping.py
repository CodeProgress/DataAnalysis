#optimal stopping

import random
import pylab


def pick_val(values, stoppingPoint):
    """Strategy: The Cutoff Rule
    Read through values until the index = stoppingPoint
    Keep track of the highest value reached so far
    Continue iterating through values until a higher number is observed
    Return this value.
    If a higher value is not reached, return the last value in values
    values: List, a continue range of numbers, ex: range(100)
    stoppingPoint: Integer between min(values) and max(values), inclusive
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

def pick_ccr_val(values, numCandidates):
    """Strategy: Candidate Count Rule
    Read through values until numCandidates are seen.  Return next candidate
    If numCandidates candidates not seen, return last value"""
    best = values[0] - 1
    numCandsSeen = 0
    for i in range(len(values)):
        if values[i] > best:
            numCandsSeen += 1
            if numCandsSeen == numCandidates:
                return values[i]                

    return values[-1]
        

def sim_outcome(numVals, stoppingPoint, numTrials, strategyFunction):
    """returns the average result over numTrials"""
    total = 0.
    for i in range(numTrials):
        values = random.sample(xrange(numVals), numVals)
        #values = [random.randint(0, numVals-1) for x in range(numVals)]
        total += strategyFunction(values, stoppingPoint)
    return total/numTrials 

def sim_outcome_list(numVals, stoppingPoint, numTrials, strategyFunction):
    """returns a list of the chosen values when stopping point reached"""
    total = []
    for i in range(numTrials):
        values = random.sample(xrange(numVals), numVals)
        #values = [random.randint(0, numVals-1) for x in range(numVals)]
        total.append(strategyFunction(values, stoppingPoint))
    return total 

def plot_average_outcome(numVals, numTrials, strategyFunction):
    pylab.plot([sim_outcome(numVals, x, numTrials, strategyFunction) for x in range(numVals)])
    pylab.xlabel("Stopping Point")
    pylab.ylabel("Average Expected Outcome")
    pylab.xticks(range(0,numVals, 5))

def plot_chance_of_optimal(numVals, numTrials, strategyFunction):
    results = []
    for x in range(numVals):
        outcomes = sim_outcome_list(numVals, x, numTrials, strategyFunction)    
        results.append(sum(1 for x in outcomes if x == numVals -1)/float(numTrials))
    pylab.plot(results)
    pylab.title("Likelihood of Stopping Optimally")
    pylab.xlabel("Stopping Points")
    pylab.ylabel("Percent (as decimal between 0 and 1)")
    pylab.xticks(range(0,numVals, 5))

plot_chance_of_optimal(100,500, pick_val)
#plot_chance_of_optimal(100,500, pick_ccr_val)
#plot_average_outcome(100,500)
pylab.show()