import pylab
import random
import numpy
from mpl_toolkits.mplot3d import Axes3D

# adapted from stackoverflow.com/questions/34920680/plotting-3d-random-walk-in-py

num_trials = 1000

figure = pylab.figure()

ax = figure.gca(projection='3d')

cur = [0, 0, 0]
xyz = [cur[:]]

for _ in xrange(num_trials):
    axis_of_next_step = random.randint(0, 2)
    cur[axis_of_next_step] += random.choice([-1,1])
    xyz.append(cur[:])

x, y, z = zip(*xyz)
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

