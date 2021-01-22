"""
Snakes & Ladders Heat Map, derived from Monte Carlo Simulation
showing the relative frequency of landing on a given square.
"""

import random
import matplotlib.pyplot as plt
import numpy as np
import collections


snakes = {16: 6,  47: 26, 49: 11,
          56: 53, 62: 19, 64: 60,
          87: 24, 93: 73, 95: 75,
          98: 78}

ladders = {1:  38,  4: 14,  9: 31,
           21: 42, 28: 84, 36: 44,
           51: 67, 71: 91, 80: 100}


def climb_or_slide(current_position, snakes_dict, ladders_dict):
    """if current position is on a magic square, return new location
    else return the current position
    """
    if current_position in snakes_dict:
        return snakes_dict[current_position]

    if current_position in ladders_dict:
        return ladders_dict[current_position]

    return current_position


def roll(num_sides=6):
    """ returns a random int between 1 and numSides, inclusive.
    """
    # return random.randint(1, numSides) #slow
    return int(random.random() * num_sides) + 1


def play_game(board_size=100, current_position=0):
    """Plays through an entire game, returns an ordered list of all squares
    that were landed on
    """
    positions = []
    # do not have to land on 100 exactly, if so, landing position spread too big
    while current_position < board_size:
        current_position = climb_or_slide(current_position + roll(), snakes, ladders)
        positions.append(current_position)
    return positions


def rel_freq_landings(num_games):
    """returns the relative frequency of landing on each square over numGames.
    relative frequency = (num times landed on sq)/(num times landed on all sqs)
    sum(rel_freq_landings(numGames)) ~ .985 since some games end past goal sq
    """
    landings = collections.Counter()
    count = 0.0
    for i in range(num_games):
        for j in play_game():
            landings[j] += 1
            count += 1
    return [landings[k]/count for k in range(0, 101)]


def make_array(landing_list, start_val=100, row_size=10):
    val = start_val
    as_array = []
    desc = False  # descending if False, ascending if True
    while val > 0:
        row = []
        counter = row_size
        while counter > 0:
            row.append(landing_list[val])
            val -= 1
            counter -= 1
        if desc:
            row.reverse()
        desc = not desc
        as_array.append(row)
    as_array.reverse()  # to match the game board visually
    return as_array


def label_board(snakes_dict, ladders_dict):
    """ label each square corresponding to 10x10 game board layout
    numbers start in bottom left, go right and follow a boustrophedon path
    to top left.  (the way an ox would plow a field.)
    And add arrows corresponding to snakes and ladders
    """
    arrow_dict = {}
    for i in range(10):
        for j in range(10):
            if i % 2 == 0:
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

            plt.text(j+0.45, i+0.35, tens + ones,
                     ha='center', va='bottom', color='w')
            
            # add coordinates to arrowDict for use when adding snakes and ladders
            arrow_dict[int(tens+ones)] = (j+0.5, i+0.5)
    
    def add_arrows(a_dict, a_color):
        for coord in a_dict:
            x, y = arrow_dict[coord]
            new_x, new_y = arrow_dict[a_dict[coord]]
            dx, dy = new_x - x, new_y - y
    
            plt.arrow(x, y, dx, dy, head_length=0.3, head_width=0.20,
                      color=a_color, linestyle="dotted", length_includes_head=True)

    add_arrows(snakes_dict, 'red')
    add_arrows(ladders_dict, '#00FF00')


def plot_heat(landings):

    data = np.array(landings)

    # remove any values that equal zero
    data = np.ma.masked_equal(data, 0)
    
    fig, ax = plt.subplots()
    
    # cmap values: http://wiki.scipy.org/Cookbook/Matplotlib/Show_colormaps
    im = ax.pcolormesh(data, cmap='cool')
    fig.colorbar(im, label="Relative Frequency (%)")

    # set the background to hatched so removed values appear hatched
    p = plt.Rectangle((0, 0), 10, 10, hatch='xx', fill=None, zorder=-1)
    ax.add_patch(p)
    
    plt.axis('off')
    plt.title('Snakes and Ladders Heat Map for All Game Squares')
    
    # add square numbers and snakes and ladders
    label_board(snakes, ladders)

    plt.show()


def run_c_profile(num_games=10000):
    import cProfile
    cProfile.run('make_array(rel_freq_landings(' + str(num_games) + '))')


if __name__ == "__main__":
    num_games_to_simulate = 10000
    plot_heat(make_array(rel_freq_landings(num_games_to_simulate)))
