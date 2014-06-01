
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
    if verbose:
        print '{} percent of the population started with the virus'.format(startingPercent)
        print '{} percent of the population is infected'.format(endingPercent)   
    return startingPercent, endingPercent


print simulate_viral_spread(numPeople           = 10000, 
                            infectionRate        = .05, 
                            numEncounters        = 50000,
                            numStartingWithVirus = 1000)