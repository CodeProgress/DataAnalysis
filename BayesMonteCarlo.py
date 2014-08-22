
import random
import pylab

def bayesMonteCarlo(percentOfPopulation, sensitivity, specificity, numTrials):
    """
    Sensitivity (True Positive Rate)
    Specificity (True Negative Rate)
    """
    numTruePositive = 0.
    numFalsePositive = 0.
    for i in xrange(numTrials):
        person = random.random()
        #person actually positive
        if person < percentOfPopulation:
            if random.random() < sensitivity:
                numTruePositive += 1
        else:
            if random.random() > specificity:
                numFalsePositive += 1
    return numTruePositive/(numTruePositive + numFalsePositive)

#print bayesMonteCarlo(.005, .99, .995, 1000000)
#print bayesMonteCarlo(.005, .9, .995, 1000000)
#print bayesMonteCarlo(.005, .99, .99, 1000000)

def plotVaryingSpecAndSen(percentOfPopulation=.01, constant=.99, numTrials = 100000):

    y = [bayesMonteCarlo(percentOfPopulation, constant, spec, numTrials) for spec in pylab.arange(0,1,.01)]
    x = range(len(y))    
    pylab.plot(x, y, color='b', label="Specificity")
    
    y = [bayesMonteCarlo(percentOfPopulation, sen, constant, numTrials) for sen in pylab.arange(0,1,.01)]
    x = range(len(y))    
    pylab.plot(x, y, color='r', label="Sensitivity")

    pylab.legend(loc=2)     # location 2 is top left
    pylab.title("Relationship between changing Specificity or Sensitiviy \n while leaving the other constant at 99%")
    pylab.xlabel("Variable's Probability")
    pylab.ylabel("True Positive Probability")
    pylab.show()

plotVaryingSpecAndSen()
