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
    
def shuffle_bias_lower_values_at_beginning_of_array(outcome_array):
    # compare val to random element in array, if lower, swap with that value
    biased_array = outcome_array.copy()
    rows, cols = biased_array.shape
    for row in xrange(rows):
        for col in xrange(cols):
            randRow = random.randint(0, rows-1)
            randCol = random.randint(0, cols-1)
            if biased_array[row][col] < biased_array[randRow][randCol]:
                biased_array[row][col], biased_array[randRow][randCol] \
                    = biased_array[randRow][randCol], biased_array[row][col]
    return biased_array

def shuffle_bias_lower_values_at_beginning_of_array_subtle(outcome_array):
    # compare val to random.random(), if lower, swap with random element of array
    biased_array = outcome_array.copy()
    rows, cols = biased_array.shape
    for row in xrange(rows):
        for col in xrange(cols):
            randRow = random.randint(0, rows-1)
            randCol = random.randint(0, cols-1)
            if biased_array[row][col] < random.random():
                biased_array[row][col], biased_array[randRow][randCol] \
                    = biased_array[randRow][randCol], biased_array[row][col]
    return biased_array

bias_function = shuffle_bias_lower_values_at_beginning_of_array_subtle
rows = 200
cols = 200

random_array = pylab.rand(rows,cols)

pylab.pcolor(bias_function(random_array))
pylab.colorbar()
pylab.show()
