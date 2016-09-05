import pylab
import random
import numpy
from mpl_toolkits.mplot3d import Axes3D

# adapted from stackoverflow.com/questions/34920680/plotting-3d-random-walk-in-py


# Random next step functions:
def random_single_step_in_one_direction(current_coordinate):
    next_random_coordinate = current_coordinate[:]
    
    axis_of_next_step = random.randint(0, 2)
    next_random_coordinate[axis_of_next_step] += random.choice([-1,1])
    
    return next_random_coordinate


def random_continuous_step_in_all_directions(current_coordinate):
    next_random_coordinate = current_coordinate[:]
    
    next_random_coordinate[0] += random.uniform(-1, 1)
    next_random_coordinate[1] += random.uniform(-1, 1)
    next_random_coordinate[2] += random.uniform(-1, 1)
    
    return next_random_coordinate


# Plotting functions:
def get_3d_walk_coordinates(next_random_3d_step_function, num_trials=1000):
    """returns a list of [x,y,z] coordinates along the random path"""

    current_coordinate = [0, 0, 0]
    xyz = [current_coordinate[:]]
    
    for i in xrange(num_trials):
        current_coordinate = next_random_3d_step_function(current_coordinate)
        xyz.append(current_coordinate)

    return xyz


def plot_3d_walk(next_random_3d_step_function, num_trials=1000):
    figure = pylab.figure()
    ax = figure.gca(projection='3d')

    list_of_coordinates = get_3d_walk_coordinates(next_random_3d_step_function, num_trials)
    x, y, z = zip(*list_of_coordinates)

    ax.plot(x, y, z)

    ax.scatter(0, 0, 0, marker='s', color='green')            # start point
    ax.scatter(x[-1], y[-1], z[-1], marker='8', color='red')  # end point
    ax.plot([0, x[-1]], [0, y[-1]], [0, z[-1]], color='black')  # line connecting start to end
    
    start_point = numpy.array((0, 0, 0))
    end_point = numpy.array((x[-1], y[-1], z[-1]))
    
    distance_from_start_to_end = numpy.linalg.norm(start_point-end_point)
    
    print "Distance from start to end after {} random steps is: {}".format(
        num_trials, distance_from_start_to_end)
    
    pylab.show()


plot_3d_walk(random_single_step_in_one_direction)
