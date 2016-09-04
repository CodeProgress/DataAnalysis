import pylab
import random


def random_walk(num_trials):
    xlist = [0]
    ylist = [0]
    xval = 0
    yval = 0
    for i in range(num_trials):
        xval += random.randint(-1, 1)
        yval += random.randint(-1, 1)
        xlist.append(xval)
        ylist.append(yval)

    return xlist, ylist


def random_walk_continuous(num_trials):
    xlist = [0]
    ylist = [0]
    xval = 0
    yval = 0
    for i in range(num_trials):
        xval += random.uniform(-1, 1)
        yval += random.uniform(-1, 1)
        xlist.append(xval)
        ylist.append(yval)

    return xlist, ylist


def random_walk_continuous_with_random_pos_and_neg(num_trials):
    '''aka the "light speed ahead" random walk
    set num_trials to 1000 for best result'''
    xlist = [0]
    ylist = [0]
    xval = 0
    yval = 0
    for i in range(num_trials):
        xval += random.random()
        yval += random.random()
        if random.random() < .5:
            xval = -xval
        if random.random() < .5:
            yval = -yval
        xlist.append(xval)
        ylist.append(yval)

    return xlist, ylist


def random_unique_x_and_y_coords(num_trials):
    xvisited = set()
    yvisited = set()
    xlist = [0]
    ylist = [0]
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
    xlist = [0]
    ylist = [0]
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


def plot_random_walk_function(random_walk_function, num_trials=1000, num_walks=1):
    for _ in range(num_walks):
        xvals, yvals = random_walk_function(num_trials)
        pylab.plot(xvals, yvals, '-o')
        
        pylab.plot(0, 0, color='green', marker='s')                # start point
        pylab.plot(xvals[-1], yvals[-1], color='red', marker='8')  # end point
        pylab.plot([0, xvals[-1]], [0, yvals[-1]], color='black')
        
    pylab.show()


plot_random_walk_function(random_walk, 1000, 20)
