#Checkout Line Simulation

'''
Questions this simulation hope to answer:

For every additional register, how much faster is the checkout time?

Is it faster to have one line that sends the customers to the next available
register, or to have people pick a line and stick with it?

Does switching lines help?

What is the relationship between checkout time and total itemsPerSecond across
all cashiers vs checkout time vs number of cashiers?

If customer is allowed to choose the line, how is overall checkout time affected
when they choose optimally, choose shortest line, choose randomly?

'''

import collections
import random

class Cashier(object):
    def __init__(self, itemsPerMinute):
        self.itemsPerMinute = itemsPerMinute
        self.itemsPerSecond = itemsPerMinute / 60.
        self.line           = collections.deque()
    
    def checkout_customer(self, customer):
        customer.cashierSpeed = self.itemsPerSecond
        while customer.numItems > 0:
            customer.numItems -= self.itemsPerSecond
            customer.totalTime += 1
    
class Customer(object):
    def __init__(self, numItems):
        self.startingItems = numItems
        self.numItems      = numItems
        self.totalTime     = 0
        self.cashierSpeed  = None
    
    def __str__(self):
        return str(vars(self))
    
class Store(object):
    def __init__(self):
        self.cashiers           = []
        self.customers          = []
        self.completedCustomers = []
    
    def add_cashier(self, itemsPerMinute = 'random'):
        if itemsPerMinute == 'random':
            newCashier = Cashier(random.randint(10,100))
        else:    
            newCashier = Cashier(itemsPerMinute)

        self.cashiers.append(newCashier)
    
    def add_customers(self, numCustomers = 1):
        for i in range(numCustomers):
            self.customers.append(Customer(random.randint(10, 20)))
    
    def simulate_one_cashier(self, numCustomers):
        self.add_cashier()
        self.add_customers(numCustomers)
        self.cashiers[0].line = self.customers
        while self.cashiers[0].line:
            cust = self.customers.pop()
            self.cashiers[0].checkout_customer(cust)
            self.completedCustomers.append(cust)

s = Store()
s.simulate_one_cashier(10)
for cust in s.completedCustomers:
    print cust