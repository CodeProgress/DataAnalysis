#Benford's Law

import random
import pylab

def fibGen():
    '''Generator, yields Fibonacci sequence: 0,1,1,2,3,5,8...
    '''
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

def make_hist_fib(numFibs):
    """returns a list, the value at indices is the number of times that index 
    was the leaing number
    indices are indexed starting with 1, ending with 9
    """
    hist = [0]*10
    fibs = fibGen()
    for i in range(numFibs):
        fib = fibs.next()
        firstDigit = int(str(fib)[0])
        hist[firstDigit] += 1
    
    return hist[1:]

def make_hist_random(numDigits, numTrials, uniform = True):
    """returns a list, the value at indices is the number of times that index 
    was the leaing number
    indices are indexed starting with 1, ending with 9
    """
    hist = [0]*10
    
    for i in range(numTrials):
        if uniform:
            randNum = random.uniform(0, 10**numDigits)
        else:
            randNum = random.randint(0, 10**numDigits)
            
        firstDigit = int(str(randNum)[0])
        hist[firstDigit] += 1
    
    return hist[1:]

def plot_hist(colors, *hists):
    index = 0
    maxIndex = len(colors)
    for hist in hists:    
        pylab.scatter(range(1, 10), hist, color = colors[index])
        index += 1
        index %= maxIndex
    pylab.title("Benford's Law")
    pylab.xlabel("Digit")
    pylab.ylabel("Number of Occurrences")
    pylab.xticks(range(1,10))
    pylab.show()


histFib = make_hist_fib(10000)
histRandom = make_hist_random(100, 10000)
colors = ['b', 'r']
plot_hist(colors, histFib, histRandom)

