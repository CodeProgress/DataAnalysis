import random
import math
import pylab

def plot_heat(outcomeArray):
    pylab.pcolor(outcomeArray) # for grey-scale: cmap = pylab.cm.Greys
    pylab.colorbar()
    pylab.show()

def updateHistogram(aHist, aList):
    for i, val in enumerate(aList):
        aHist[val][i] += 1

def swapValuesInList(aList, index1, index2):
    aList[index1], aList[index2] = aList[index2], aList[index1]

def mutation_swapIfValueAtIndexGreaterThanValuesIndexsVal(aList, index, value):
    elementInListValuethPosition = aList[value]
    if value > elementInListValuethPosition:
        swapValuesInList(aList, index, value)

def mutation_randomSwapAtValuesIndex(aList, index, value):
    aList[value] = random.choice(aList)

def mutation_randomSwapAtValuesIndexIfGreaterOrEqual(aList, index, value):
    elementInListValuethPosition = aList[value]
    if value >= elementInListValuethPosition:
        aList[value] = random.choice(aList)

def mutation_randomChoiceInListAtValuesIndex(aList, index, value):
    aList[value] = random.choice(aList)

def mutation_randomChoiceInListAtIndex(aList, index, value):
    aList[index] = random.choice(aList)

def mutation_trueRandom(aList, index, value):
    '''Expect a checkered pattern of values in a very tight range'''
    aList[index] = random.randint(0, len(aList)-1)

def mutation_swapValuesAtIndexAndValuesIndex(aList, index, value):
    swapValuesInList(aList, index, value)

def mutation_swapValueWithRandomIndex(aList, index, value):
    '''Almost like trueRandom except a clear unbalanced distribution where index == value'''
    swapValuesInList(aList, value, random.randint(0, len(aList)-1))

def runMutations(mutationFunction, numTrials = 100000, popSize = 10, verbose = True):
    histogram = pylab.array([[0]*popSize for i in xrange(popSize)])
    
    aList = random.sample(range(popSize), popSize)
    
    for i in range(numTrials):
        for index, value in enumerate(aList):
            mutationFunction(aList, index, value)
        
        # only print the list a small number of times
        if verbose and i % (numTrials/int(math.log(numTrials, 2))) == 0: 
            print aList
        updateHistogram(histogram, aList)
    return histogram

outcome = runMutations(mutation_swapValueWithRandomIndex)
plot_heat(outcome)

    