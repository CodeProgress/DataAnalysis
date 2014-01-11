#Monte Carlo Simulation of the Birthday Problem
#http://en.wikipedia.org/wiki/Birthday_problem

import random
import pylab
import collections

def rand_birthday():
    return int(random.random()*366) + 1

def num_people_for_same_bday():
    """returns the number of people needed for two to share a birthday
    runs a single Monte Carlo simulation
    """
    bdays = {}
    birthday = rand_birthday()
    while birthday not in bdays:
        bdays[birthday] = True
        birthday = rand_birthday()
        
    return len(bdays) + 1 # +1 because duplicate is not added to set

def shared_bdays(numTrials = 100000):
    """returns a list of the number of people needed for two to share a birthday
    """
    vals = []
    for i in xrange(numTrials):
        vals.append(num_people_for_same_bday())
    
    return vals

def plot_shared_bdays(vals):
    hist = collections.Counter(vals)
    
    vals = []
    high = max(hist)
    for i in range(high + 1):
        vals.append(hist[i])
    
    for i in range(1,len(vals)):
        vals[i] += vals[i-1]
    
    #normalize vals to be between 0 and 1
    yMax = float(max(vals))
    for i in range(len(vals)):
        vals[i] /= yMax
        
    pylab.plot(vals)
    pylab.xlabel("Number of People")
    pylab.ylabel("Probability of Shared Birthday")
    
    pylab.show()

plot_shared_bdays(shared_bdays())
