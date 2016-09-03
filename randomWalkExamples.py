import pylab
import random


def random_with_exponent(num_trials):
    xlist = [random.random()**.5 for i in range(num_trials)]
    ylist = [random.random()**.5 for j in range(num_trials)]
    return xlist, ylist
    

def random_unique_x_and_y_coords(num_trials):
    xvisited = set()
    yvisited = set()
    xlist = []
    ylist = []
    xval = 0
    yval = 0
    for i in range(num_trials):
        xval += random.randint(-1, 1)
        yval += random.randint(-1, 1)
        if xval not in xvisited:
            xvisited.add(xval)
            xlist.append(xval)
        if yval not in yvisited:
            yvisited.add(yval)
            ylist.append(yval)
        
    minlength = min(len(xlist), len(ylist))
    
    xlist = xlist[:minlength]
    ylist = ylist[:minlength]
    return xlist, ylist


def random_unique_xy_coords(num_trials):
    visited = set()
    xlist = []
    ylist = []
    xval = 0
    yval = 0
    for i in range(num_trials):
        xval += random.randint(-1, 1)
        yval += random.randint(-1, 1)
        if (xval, yval) not in visited:
            visited.add((xval, yval))
            xlist.append(xval)
            ylist.append(yval)

    return xlist, ylist


pylab.scatter(*random_unique_xy_coords(1000))
pylab.show()
