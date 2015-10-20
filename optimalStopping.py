#optimal stopping

import pylab
import numpy

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
    bestSoFar = values[0]
    for i, value in enumerate(values):
        if i < stoppingPoint and value > bestSoFar:
            bestSoFar = value
        else:
            if value > bestSoFar:
                return value
    return values[-1]

def pick_val_after_2_new_bests(values, stoppingPoint):
    return pick_val_after_N_new_bests(values, stoppingPoint, 2)

def pick_val_after_3_new_bests(values, stoppingPoint):
    return pick_val_after_N_new_bests(values, stoppingPoint, 3)

def pick_val_after_N_new_bests(values, stoppingPoint, numNewBestsToStopAfter):
    """
    Same as pick_val except when higher number is found, use it as the new best
    and keep iterating until you find something higher.
    """
    bestsSoFar = [values[0]]
    for i, value in enumerate(values):
        if i < stoppingPoint and value > bestsSoFar[0]:
            bestsSoFar[0] = value
        else:
            if value > bestsSoFar[-1]:
                if len(bestsSoFar) >= numNewBestsToStopAfter:
                    return value
                else:
                    bestsSoFar.append(value)
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
        values = numpy.random.choice(10, 10, replace=False)
        #values = [random.randint(0, numVals-1) for x in range(numVals)]
        total += strategyFunction(values, stoppingPoint)
    return total/numTrials 

def sim_outcome_list(numVals, stoppingPoint, numTrials, strategyFunction):
    """returns a list of the chosen values when stopping point reached"""
    total = []
    for i in range(numTrials):
        values = numpy.random.choice(numVals, numVals, replace=False)
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
    optimalVal = numVals-1 
    for stoppingPoint in range(numVals):
        outcomes = sim_outcome_list(numVals, stoppingPoint, numTrials, strategyFunction)   
        results.append(sum(1 for chosenVal in outcomes if chosenVal == optimalVal)/float(numTrials))
    pylab.plot(results)
    pylab.title("Likelihood of Stopping Optimally")
    pylab.xlabel("Stopping Points")
    pylab.ylabel("Percent (as decimal between 0 and 1)")
    pylab.xticks(range(0,numVals, 5))

def plot_chance_of_chosen_being_within_N_points_of_optimal(numVals, numTrials, strategyFunction, NPoints):
    results = []
    optimalVal = numVals-1 
    for stoppingPoint in range(numVals):
        outcomes = sim_outcome_list(numVals, stoppingPoint, numTrials, strategyFunction)   
        results.append(sum(1 for chosenVal in outcomes if abs(chosenVal-optimalVal) <= NPoints)/float(numTrials))
    pylab.plot(results, label="Within {}".format(NPoints))
    pylab.title("Likelihood of Stopping Witin N of Optimal")
    pylab.xlabel("Stopping Points")
    pylab.ylabel("Percent (as decimal between 0 and 1)")
    pylab.xticks(range(0,numVals, 5))

#plot_chance_of_optimal(100,500, pick_val)
#plot_chance_of_optimal(100,500, pick_val_after_2_new_bests)
#plot_chance_of_optimal(100,500, pick_val_after_3_new_bests)
#plot_chance_of_optimal(100,500, pick_ccr_val)

#plot_average_outcome(100,500, pick_val)
#plot_average_outcome(100,500, pick_val_after_2_new_bests)
#plot_average_outcome(100,500, pick_val_after_3_new_bests)

plot_chance_of_chosen_being_within_N_points_of_optimal(100,300, pick_val, 0)
plot_chance_of_chosen_being_within_N_points_of_optimal(100,300, pick_val, 1)
plot_chance_of_chosen_being_within_N_points_of_optimal(100,300, pick_val, 2)
plot_chance_of_chosen_being_within_N_points_of_optimal(100,300, pick_val, 3)
plot_chance_of_chosen_being_within_N_points_of_optimal(100,300, pick_val, 10)
pylab.legend()

pylab.show()
