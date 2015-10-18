# Simpson's paradox

import random

def random_fraction(floor=2, limit=100):
    '''
    returns a random numerator and denominator
    where floor <= numerator <= limit
    and numerator <= denominator <= limit
    '''
    numer = random.randint(floor, limit)
    denom = random.randint(numer, limit)
    return numer, denom

numTrials = 10000
limit = 100
count = 0

for trial in xrange(numTrials):
    numerA1, denomA1 = random_fraction()
    numerA2, denomA2 = random_fraction()
    
    combinedAnumer = numerA1 + numerA2
    combinedAdenom = denomA1 + denomA2

    percentageA1 = float(numerA1)/denomA1
    percentageA2 = float(numerA2)/denomA2    
    percentageCombinedA = float(combinedAnumer)/combinedAdenom
                
    numerB1, denomB1 = random_fraction()
    numerB2, denomB2 = random_fraction()
    
    combinedBnumer = numerB1 + numerB2
    combinedBdenom = denomB1 + denomB2
    
    percentageB1 = float(numerB1)/denomB1
    percentageB2 = float(numerB2)/denomB2
    percentageCombinedB = float(combinedBnumer)/combinedBdenom

    #Check for existence of paradox:
    if percentageA1 < percentageB1:
        if percentageA2 < percentageB2:
            if percentageCombinedA > percentageCombinedB:
                count += 1
                print "{}/{}, {}/{}".format(numerA1, denomA1, numerA2, denomA2)
                print "{}/{}, {}/{}".format(numerB1, denomB1, numerB2, denomB2)
                print "{}/{}, {}/{}".format(combinedAnumer, combinedAdenom, combinedBnumer, combinedBdenom)
                print "{}, {}".format(percentageCombinedA, percentageCombinedB)
                print "___________________"

print count, numTrials, float(count)/numTrials


