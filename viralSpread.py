
import random
import pylab


def simulate_viral_spread(numPeople, 
                          infectionRate, 
                          numEncounters, 
                          numStartingWithVirus,
                          verbose = False):
    """
    Returns the percentage increase in the number of people who have the virus
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

def plot_viral_spread(numPeople, 
                      startingInfectionRate, 
                      numEncounters, 
                      numStartingWithVirus,
                      incr):
    """incr increases the infection rate.  0 < incr < 1"""
    infectionRate = float(startingInfectionRate)
    testCases = []

    for i in range(int(1/incr)):
        testCases.append([numPeople, infectionRate, numEncounters, numStartingWithVirus])
        infectionRate += incr
    
    
    pylab.plot([simulate_viral_spread(*x) for x in testCases])
    
    pylab.ylabel("Percent increase from starting rate to ending rate")
    pylab.xlabel("nth trial")
    pylab.show()
        
plot_viral_spread(1000, 0,  10000, 100, .02)



