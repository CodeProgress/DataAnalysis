import random
import pylab as pl
import numpy as np

def naive_shuffle(elements):
    for i, element in enumerate(elements):
        randIndex = np.random.randint(len(elements))
        elements[i], elements[randIndex] = elements[randIndex], elements[i]
    return elements
    
def fisher_yates_durstenfeld(elements):
    upperIndex = len(elements)
    while upperIndex > 0:
        randomIndex = np.random.randint(upperIndex)
        elements[randomIndex], elements[upperIndex-1] = elements[upperIndex-1], elements[randomIndex]    
        upperIndex -= 1
    return elements

def built_in_python_shuffle(elements):
    random.shuffle(elements)
    return elements

def crazy_shuffle(elements):
    pass

def increment_outcome_array(array, x_index, y_value):
    array[x_index][y_value] += 1

def draw_heat_plot_of_shuffle_algorithm(shuffleAlgorithm, numElements=100, numTrials=10000):

    outcomeArray = pl.array([[0]*numElements for i in range(numElements)])

    for trial in xrange(numTrials):
        elements = range(numElements)
    
        shuffled = shuffleAlgorithm(elements)

        for finalIndex, val in enumerate(shuffled):
            increment_outcome_array(outcomeArray, finalIndex, val)
    
    pl.pcolor(outcomeArray)
    pl.colorbar()
    pl.show()


draw_heat_plot_of_shuffle_algorithm(naive_shuffle)
#draw_heat_plot_of_shuffle_algorithm(fisher_yates_durstenfeld)
#draw_heat_plot_of_shuffle_algorithm(built_in_python_shuffle)
