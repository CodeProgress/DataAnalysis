
# Analysis of CountingRectangles.py algorithm using pylab

import pylab

def count(x, y):
    '''counts the number of rectangles in a grid x by y
    x, y: ints
    '''
    return ( x*(x+1) * y*(y+1) )/4

def findArea(goal = 2000000):
    '''returns the area (int) of the grid with total rectangles closest to goal
    goal: int > 0
    '''
    assert goal > 0
    
    #data to plot
    xList             = []
    yList             = []
    smallestDiffFound = []
    products          = []
    numRecs           = []
    
    #start algorithm
    x = 1
    y = 1

    diff = goal
    smallestDiff = goal

    #dimens = (1, 1)

    while True:
        xList.append(x)
        yList.append(y)
        products.append(x*y)
        numRec = count(x,y)
        numRecs.append(numRec)
        diff = abs(goal - numRec)

        if diff < smallestDiff:
            smallestDiff = diff
            #dimens = (x,y)

        if smallestDiff < x*y:
            smallestDiffFound.append(smallestDiff)
        else:
            smallestDiffFound.append(x*y)
        
        if numRec < goal:
            x += 1
            y += 1
        else:
            x -= 1
        
        #terminating condition
        if x == 1:
            break
    
    #answer = dimens[0] * dimens[1]
    
    return [xList, yList, smallestDiffFound, products, numRecs]

def analyzeFindArea(target = 10000):
    
    xList, yList, sDiff, products, numRecs = findArea(target)
    pylab.plot(xList, label = 'x')
    pylab.plot(yList, label = 'y')
    pylab.plot(sDiff, label = 'Smallest Diff')
    pylab.plot(products, label = 'x * y')
    #pylab.plot(numRecs, label = 'Num Rectangles')
    
    pylab.legend()
    
    pylab.show()


analyzeFindArea()
