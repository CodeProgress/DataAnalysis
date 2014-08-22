
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

print bayesMonteCarlo(.005, .99, .995, 1000000)

print bayesMonteCarlo(.005, .9, .995, 1000000)

print bayesMonteCarlo(.005, .99, .99, 1000000)


