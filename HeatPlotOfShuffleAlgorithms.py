import random
import collections
import pylab as pl

def naive_shuffle(elements):
    for i, element in enumerate(elements):
        randIndex = random.randint(0, len(elements) - 1)
        elements[i], elements[randIndex] = elements[randIndex], elements[i]
    return elements
    
def fishcer_yayes(elements):
    pass

def update_array(array, x_index, y_value):
    pass

numTrials = 10000
histogram = collections.Counter()
numElements = 100

for trial in xrange(numTrials):
    elements = range(numElements)

    shuffled = naive_shuffle(elements)

    indicesOfValues = [-1] * numElements
    for finalIndex, val in enumerate(shuffled):
         indicesOfValues[val] = finalIndex

    histogram.update(zip(range(numElements),indicesOfValues))

histArray = pl.array([[-1]*numElements for i in range(numElements)])

for result in histogram:
    finalIndex, val = result
    histArray[finalIndex][val] = histogram[result]


pl.pcolor(histArray)
pl.colorbar()
pl.show()


