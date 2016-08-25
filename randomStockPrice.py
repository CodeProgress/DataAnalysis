import pylab
import random


def simulated_stock_prices(num_iterations):
    assert num_iterations > 0
    prices = []
    price = 0
    for i in xrange(num_iterations):
        change_in_price = random.random() * 2 - 1
        price += change_in_price
        prices.append(price)
    return prices


def final_stock_price_after_simulation(prices):
    return prices[-1]


def multi_trial_stock_prices(num_trials, num_iterations_in_trial):
    assert num_trials > 1
    all_prices = []
    for trial in xrange(num_trials):
        all_prices.append(final_stock_price_after_simulation(simulated_stock_prices(num_iterations_in_trial)))
    return all_prices

simulated_prices = simulated_stock_prices(100)

pylab.plot(simulated_prices)
pylab.show()
