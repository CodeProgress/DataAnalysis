import pylab
import random
import collections


def get_location_after_random_step(current_location, low_bound, high_bound):
    x, y = current_location
    x += random.randint(-1, 1)
    y += random.randint(-1, 1)
    
    x, y = bounded_location(x, y, low_bound, high_bound)
    
    return x, y
    
    
def bounded_location(x, y, low_bound, high_bound):
    x = bound(x, low_bound, high_bound)
    y = bound(y, low_bound, high_bound)
    return x, y
    
    
def bound(dimension, low_bound, high_bound):
    if dimension < low_bound: 
        dimension = low_bound
    elif dimension > high_bound: 
        dimension = high_bound
    return dimension


def get_new_locations_after_all_people_randomly_step(people, low_bound, high_bound):
    new_people = []
    for person in people:
        new_people.append(get_location_after_random_step(person, low_bound, high_bound))
    return new_people
    

def rem_one_of_duplicates(people):
    return list(set(people))


def rem_all_duplicates(people):
    hist = collections.Counter(people)
    seen_once = [x for x in hist if hist[x] ==1]
    return seen_once
    
    
def get_random_starting_locations(num_people, low_bound, high_bound):
    people = []
    for person in range(num_people):
        rand_x = random.randint(low_bound, high_bound)
        rand_y = random.randint(low_bound, high_bound)
        people.append((rand_x, rand_y))
    return people
    

def plot_remaining_people_after_steps_until_target(
        starting_num_people,
        low_bound = -20,
        high_bound = 20,
        target_remaining = 5):
    
    people = get_random_starting_locations(
                starting_num_people,
                low_bound,
                high_bound)
        
    #pylab.scatter(*zip(*people))
    #pylab.show()
    
    size = len(people)
    step_counter = 0
    sizes = [size]
    step_history_after_collision = [step_counter]

    # everyone walks around room until target num remaining
    while size > target_remaining:
        step_counter += 1
        #people = rem_one_of_duplicates(people)
        people = rem_all_duplicates(people) 
        people = get_new_locations_after_all_people_randomly_step(
                    people, low_bound, high_bound)
        if len(people) < size:
            sizes.append(size)
            step_history_after_collision.append(step_counter)
            size = len(people)
    
    pylab.plot(step_history_after_collision, sizes, label=starting_num_people)


for starting_num_people in range(10, 200, 20):
    plot_remaining_people_after_steps_until_target(starting_num_people)
    
pylab.legend(title="Starting num people in room")
pylab.xlabel("Number of random steps")
pylab.ylabel("Number of people remaining in room")
pylab.title("Number of random steps needed until all people collide")
pylab.show()


#cProfile.run('profile_plot()', sort='cumulative')

# speedup using numpy
# x = numpy.array([0]*10)
# x += numpy.random.randint(-1, 2, 10)
# x[x>10] = 10
# x[x<-10] = 10