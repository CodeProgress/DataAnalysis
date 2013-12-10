
'''
The following program is a simulation of Snakes & Ladders
The final product is a heat map that shows the relative frequency of landing on
a given square.

'''

import random
import pylab
import collections

def climb_or_slide(currentPosition, 
                    snakes  = {16:  6,     47: 26,     49: 11,
                               56: 53,     62: 19,     64: 60, 
                               87: 24,     93: 73,     95: 75, 
                               98: 78},

                    ladders = { 1: 38,      4: 14,      9: 31, 
                               21: 42,     28: 84,     36: 44, 
                               51: 67,     71: 91,     80: 100}
                    ):
    '''if current position is on a magic square, return new location
    else return the current position
    '''
    if currentPosition in snakes:
        return snakes[currentPosition]

    if currentPosition in ladders:
        return ladders[currentPosition]

    return currentPosition

def roll(numSides = 6):
    ''' returns a random int between 1 and numSides, inclusive.
    '''
    #return random.randint(1, numSides) #slow
    return int(random.random() * numSides) + 1


def play_game(boardSize = 100, currentPosition = 0):
    '''Plays through an entire game, returns an ordered list of all squares
    that were landed on
    '''
    positions = []
    #do not have to land on 100 exactly, if so, landing position spread too big
    while currentPosition < boardSize:
        currentPosition = climb_or_slide(currentPosition + roll())
        positions.append(currentPosition)
    return positions

def rel_freq_landings(numGames):
    """returns the relative frequency of landing on each square over numGames.
    relative frequency = (num times landed on sq)/(num times landed on all sqs)
    sum(rel_freq_landings(numGames)) ~ .985 since some games end past goal sq
    """
    landings = collections.Counter()
    count = 0.0
    for i in xrange(numGames):
        for j in play_game():
            landings[j] += 1
            count += 1
    return [landings[k]/count for k in xrange(0,101)]

def make_array(landingList, startVal = 100, rowSize = 10):
    val = startVal
    asArray = []
    desc = False #descending if False, ascending if True
    while val > 0:
        row = []
        counter = rowSize
        while counter > 0:
            row.append(landingList[val])
            val -= 1
            counter -= 1
        if desc:
            row.reverse()
        desc = not desc
        asArray.append(row)
    asArray.reverse() #to match the gameboard visually
    return asArray

def label_board(arrayA, snakes  = {16:  6,     47: 26,     49: 11,
                                    56: 53,     62: 19,     64: 60, 
                                    87: 24,     93: 73,     95: 75, 
                                    98: 78},

                        ladders = { 1: 38,      4: 14,      9: 31, 
                                    21: 42,     28: 84,     36: 44, 
                                    51: 67,     71: 91,     80: 100}
                ):
    ''' label each square corresponding to 10x10 gameboard layout
    numbers start in bottom left, go right and follow a boustrophedon path
    to top left.  (the way an ox would plow a field.)
    And add arrows corresponding to snakes and ladders
    '''
    arrowDict = {}
    for i in range(10):
        for j in range(10):
            if i % 2 ==0:
                if j == 9:
                    ones = str(0)
                    tens = str(i+1)
                else: 
                    ones = str(j+1)
                    tens = str(i)
            else:
                if j == 0:
                    ones = str(0)
                    tens = str(i+1)
                else:
                    ones = str(10-j)
                    tens = str(i)

            pylab.text(j+0.45, i+0.35, tens + ones, 
                        ha='center', va='bottom',color='w')
            
            #add coordinates to arrowDict for use when adding snakes and ladders
            arrowDict[int(tens+ones)] = (j+0.5, i+0.5)
    
    def addArrows(aDict, aColor):
        for i in aDict:
            x, y = arrowDict[i]
            newx, newy = arrowDict[aDict[i]]
            dx, dy = newx - x, newy - y
    
            pylab.arrow(x, y, dx, dy, head_length=0.3,head_width=0.20, 
              color = aColor, linestyle = "dotted", length_includes_head = True)

    addArrows(snakes, 'red')
    addArrows(ladders, '#00FF00') 
    
def plot_heat(landings):
    
    data = pylab.array(landings)

    #remove any values that equal zero
    data = pylab.ma.masked_equal(data, 0)
    
    fig, ax = pylab.subplots()
    
    #cmap values: http://wiki.scipy.org/Cookbook/Matplotlib/Show_colormaps
    im = ax.pcolormesh(data, cmap = 'cool')
    fig.colorbar(im, label = "Relative Frequency (%)")
    

    #set the background to hatched so removed values appear hatched
    p = pylab.Rectangle((0,0), 10, 10, hatch = 'xx', fill = None, zorder = -1)
    ax.add_patch(p)
    
    pylab.axis('off')
    pylab.title('Snakes and Ladders Heat Map for All Game Squares')
    
    #add square numbers and snakes and ladders
    label_board(data)

    pylab.show()

def run_cProfile(numGames = 10000):
    import cProfile
    cProfile.run('make_array(rel_freq_landings(' + str(numGames) + '))')


if __name__ == "__main__":
    numGames = 10000
    plot_heat(make_array(rel_freq_landings(numGames)))

