import random
import matplotlib.pyplot as plt


def rand_walk_1d_vals(num_steps):
    """returns an array of ints, increasing or decreasing randomly from the previous int"""
    starting_val = 0
    vals = [starting_val]
    for step in range(num_steps - 1):
        vals.append(vals[step] + random.randint(-1, 1))
        # vals.append(vals[step] + random.random()*(random.choice([-1,1])))
    return vals


num_rand_steps = 10000
x = rand_walk_1d_vals(num_rand_steps)
y = rand_walk_1d_vals(num_rand_steps)

farthest_point_tracker = [0]
farthest_point_coordinates = [(0, 0)]
for i in range(num_rand_steps):
    distance_from_origin = (x[i]**2 + y[i]**2)**.5
    if distance_from_origin > farthest_point_tracker[-1]:
        farthest_point_tracker.append(distance_from_origin)
        farthest_point_coordinates.append((x[i], y[i]))

plt.scatter(x, y, c=range(num_rand_steps))

plt.arrow(0, 0, x[-1], y[-1],
          head_width=1, color="red", label="origin to final position")

plt.arrow(0, 0, farthest_point_coordinates[-1][0], farthest_point_coordinates[-1][1],
          head_width=1, color="blue", label="farthest point from origin")

plt.arrow(farthest_point_coordinates[-1][0],
          farthest_point_coordinates[-1][1],
          x[-1] - farthest_point_coordinates[-1][0],
          y[-1] - farthest_point_coordinates[-1][1],
          head_width=1, color="green", label="farthest point to final position")

# Calculate angle between farthest point, origin and final position?
# What is the distribution of these angles?

plt.title("Random Walk")
plt.colorbar(label="Nth Step")
plt.legend()

# make output graph full screen for best viewing experience
plt.show()
