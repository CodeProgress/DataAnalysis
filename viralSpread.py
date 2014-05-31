
import random


def simulate_viral_spread(numPeople, 
                          infectionRate, 
                          numEncounters, 
                          numStartingWithVirus):
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
    percentWithVirus = sum(population)/float(numPeople) * 100
    print '{} percent of the population started with the virus'.format(startingPercent)
    print '{} percent of the population is infected'.format(percentWithVirus)   

print simulate_viral_spread(numPeople           = 10000, 
                            infectionRate        = .2, 
                            numEncounters        = 10000,
                            numStartingWithVirus = 100)