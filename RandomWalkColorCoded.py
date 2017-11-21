import random
import pylab

def rand_walk_vals(num_vals):
    starting_val = 0
    vals = [starting_val]
    for i in range(num_vals-1):
        vals.append(vals[i] + random.randint(-1, 1))
    return vals


num_steps = 1000
x = rand_walk_vals(num_steps)
y = rand_walk_vals(num_steps)

pylab.scatter(x, y, c=range(num_steps))
pylab.arrow(0, 0, x[-1], y[-1], head_width=1, color="red")

pylab.title("Random Walk")
pylab.colorbar(label="Nth Step")
pylab.show()
