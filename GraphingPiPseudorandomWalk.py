import matplotlib.pyplot as plt
import sympy


def walk_step(current_location, dx_dy):
    x, y = current_location
    dx, dy = dx_dy
    return x + dx, y + dy


direction_mapper = {"1": (-1, 1), "2": (0, 1), "3": (1, 1),
                    "4": (-1, 0), "5": (0, 0), "6": (1, 0),
                    "7": (-1, -1), "8": (0, -1), "9": (1, -1),
                    "0": (0, 0)}
# nw n ne
# w  - e
# sw s sw

# 1  2  3
# 4 5/0 6
# 7  8  9

# other mapper ideas:
# walk straight when odd, turn right when even

num_digits = 100000
pi_digits = "3" + str(sympy.N(sympy.pi, num_digits))[2:]

random_walk = [(0, 0)]
for num in pi_digits:
    curr_location = random_walk[-1]
    new_location = walk_step(curr_location, direction_mapper[num])
    random_walk.append(new_location)

seen = set()
random_walk_no_duplicate_locations = []
for loc in random_walk:
    if loc in seen:
        continue
    seen.add(loc)
    random_walk_no_duplicate_locations.append(loc)
print(len(random_walk), len(random_walk_no_duplicate_locations), len(random_walk)/len(random_walk_no_duplicate_locations))

x_list = [x[0] for x in random_walk_no_duplicate_locations]
y_list = [y[1] for y in random_walk_no_duplicate_locations]

plt.plot(x_list, y_list)
plt.scatter(x_list, y_list, c=range(len(random_walk_no_duplicate_locations)))    # c=range(len(random_walk)
plt.colorbar()
plt.show()
