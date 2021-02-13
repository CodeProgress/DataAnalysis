# Further exploration of the "Counterintuitive problem:
# "Imagine a room full of 100 people with 100 dollars each.
# With every tick of the clock, every person with money gives a dollar to one randomly chosen other person.
# After some time progresses, how will the money be distributed?" [1]

# Except this time, the concept of earned interest has been added.
# Where everyone's bankroll increases by a fixed interest rate.
# Result: Earned interest "locks in" early random variation, reduces mobility over time, and increases everyone's final
#   dollar value (due to adding more dollars into the system as a whole)
# Future: add the concept of debt and allow people to drop below zero, or keep the pie fixed, animate mobility

# [1] Source: http://www.decisionsciencenews.com/2017/06/19/
#  counterintuitive-problem-everyone-room-keeps-giving-dollars-random-others-youll-never-guess-happens-next/


import random
import numpy
import matplotlib.pyplot as plt


def randomly_give(population):
    updated_values = population[::]
    for index, val in enumerate(population):
        if val > 0:
            updated_values[index] -= 1
            index_to_give_to = random.randint(0, len(population)-1)
            updated_values[index_to_give_to] += 1
    return updated_values


def add_earned_interest(population, int_rate=.001):
    return population * (1+int_rate)


starting_money = 30  # must make low enough for some people to hit zero
num_people = 20
population_random = numpy.array([starting_money] * num_people)
population_with_interest = population_random[::-1]

num_iterations = 10000

history_random = [[starting_money] for _ in range(num_people)]
history_with_interest = [[starting_money] for _ in range(num_people)]

for i in range(num_iterations):
    population_random = randomly_give(population_random)
    population_with_interest = add_earned_interest(population_with_interest)
    for person_hist_index in range(num_people):
        history_random[person_hist_index].append(population_random[person_hist_index])
        history_with_interest[person_hist_index].append(population_with_interest[person_hist_index])

# plt.plot(sorted(population), label="random")
# plt.plot(sorted(population_with_interest), label="with interest")
# plt.legend()

for hist_index in range(num_people):
    # plt.plot(history_with_interest[hist_index])
    plt.plot(history_random[hist_index])

plt.show()
