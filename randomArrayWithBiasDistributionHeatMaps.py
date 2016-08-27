import pylab
import random


def bias_distribution_toward_higher_values(outcome_array):
    biased_array = outcome_array.copy()
    rows, cols = biased_array.shape
    for row in xrange(rows):
        for col in xrange(cols):
            if biased_array[row][col] < .5:
                biased_array[row][col] = random.random()
    return biased_array

def bias_distribution_row_vals_high_to_low(outcome_array):
    biased_array = outcome_array.copy()
    rows, cols = biased_array.shape
    for row in xrange(rows):
        startIndex = 0
        tailIndex = rows-1
        for col in xrange(cols):
            if biased_array[row][startIndex] < .5:
                biased_array[row][startIndex], biased_array[row][tailIndex] \
                    = biased_array[row][tailIndex], biased_array[row][startIndex]
                tailIndex -= 1
            startIndex += 1
            if startIndex == tailIndex:
                break
    return biased_array

rows = 200
cols = 200

random_array = pylab.rand(rows,cols)

pylab.pcolor(bias_distribution_row_vals_high_to_low(random_array))
pylab.colorbar()
pylab.show()
