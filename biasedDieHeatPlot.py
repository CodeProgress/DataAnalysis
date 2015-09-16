import random
import pylab


class die(object):
    def __init__(self, numSides):
        self.numSides = numSides
    
    def roll(self):
        return random.randint(1, self.numSides)

class biasedDieFavoringOneSide(die):
    def __init__(self, numSides, biasedSide, biasPercentage):
        '''biasPercetage is the percent increase/decrease that the biasedSide will be rolled
        '''
        assert numSides >= 1
        assert 1 <= biasedSide <= numSides
        self.numSides = numSides
        self.biasedSide = biasedSide
        self.otherSides = [x for x in range(1, self.numSides+1) if x != self.biasedSide]
        self.biasPercentage = biasPercentage
        self.biasedSideProbability = self.determine_biased_side_probability()
    
    @staticmethod
    def determine_odds(probability):
        return probability/(1.-probability)
    
    @staticmethod
    def determine_probability_as_function_of_odds(odds):
        return odds/(1.+odds)
            
    def determine_biased_side_probability(self):
        normalizedPercent = self.biasPercentage/100.
        fairProbability = 1./self.numSides
        odds = self.determine_odds(fairProbability)
        biasedOdds = odds * (1+normalizedPercent)
        newProbabilityOfBiasedSide = self.determine_probability_as_function_of_odds(biasedOdds)
        return newProbabilityOfBiasedSide

    def roll(self):
        if random.random() < self.biasedSideProbability:
            return self.biasedSide
        return random.choice(self.otherSides)
        

numSides = 6
dieOne = die(numSides)
dieTwo = biasedDieFavoringOneSide(numSides, 3, 50)

numRolls = 10000
outcomeArray = pylab.array([[0]*numSides for i in xrange(numSides)])

for roll in xrange(numRolls):
    outcomeOne = dieOne.roll()
    outcomeTwo = dieTwo.roll()
    
    outcomeArray[outcomeOne - 1][outcomeTwo - 1] += 1

pylab.pcolor(outcomeArray)
pylab.colorbar()
pylab.show()

