
import random
import pylab


def simulate_viral_spread(numPeople, 
                          infectionRate, 
                          numEncounters, 
                          numStartingWithVirus,
                          verbose = False):
    """
    Returns two values:
        the percentage of the population starting with the virus
        the percentage ending with the virus
    """
    population = [0 for i in range(numPeople)]
    
    for j in random.sample(xrange(numPeople), numStartingWithVirus):
        population[j] = 1
    
    for i in range(numEncounters):
        x, y = random.sample(xrange(numPeople), 2)
        # Use XOR since we only care if one is infected one is not infected
        if population[x] ^ population[y]:
            if random.random() < infectionRate:
                population[x] = 1
                population[y] = 1
    
    startingPercent  = numStartingWithVirus/float(numPeople)*100
    endingPercent    = sum(population)/float(numPeople) * 100
    PercentChange    = ((endingPercent - startingPercent) / startingPercent) * 100
    if verbose:
        print '{} percent of the population started with the virus'.format(startingPercent)
        print '{} percent of the population is infected'.format(endingPercent)   

    return PercentChange


numPeople            = 1000
infectionRate        = 0. 
numEncounters        = 10000
numStartingWithVirus = 100

incr = .05
testCases = []

for i in range(15):
    testCases.append([numPeople, infectionRate, numEncounters, numStartingWithVirus])
    infectionRate += incr


pylab.plot([simulate_viral_spread(*x) for x in testCases])

pylab.ylabel("Percent increase from starting rate to ending rate")
pylab.xlabel("nth trial")
pylab.show()

