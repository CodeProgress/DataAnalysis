import pylab
import random
import collections

def get_location_after_random_step(person, low_bound, high_bound):
    x, y = person
    x += random.randint(-1, 1)
    y += random.randint(-1, 1)
    
    # bound walk
    if x < low_bound: x = low_bound
    elif x > high_bound: x = high_bound
    if y < low_bound: y = low_bound
    elif y > high_bound: y = high_bound
    
    return x, y
    
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
        target_remaining = 5):
    
    low_bound = -20
    high_bound = 20
    people = get_random_starting_locations(
                starting_num_people,
                low_bound,
                high_bound)
        
    #pylab.scatter(*zip(*people))
    #pylab.show()
    
    size = len(people)
    counter = 0
    sizes = [size]
    counters = [counter]
    # print size, counter
    
    while size > target_remaining:
        counter += 1
        #people = rem_one_of_duplicates(people)
        people = rem_all_duplicates(people) 
        people = get_new_locations_after_all_people_randomly_step(
                    people, low_bound, high_bound)
        if len(people) < size:
            sizes.append(size)
            counters.append(counter)
            size = len(people)
            # print size, counter
    
    pylab.plot(counters, sizes, label=starting_num_people)

for starting_num_people in range(10, 200, 20):
    plot_remaining_people_after_steps_until_target(starting_num_people)
    
pylab.legend(title="Starting num people in room")
pylab.xlabel("Number of random steps")
pylab.ylabel("Number of people remaining in room")
pylab.title("Number of random steps needed until all people collide")
pylab.show()

