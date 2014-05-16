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


import random
import collections

class CheckoutPoint(object):
    def __init__(self, itemsPerMinute):
        self.itemsPerMinute = itemsPerMinute
        self.itemsPerSecond = itemsPerMinute/60.     
                
                                
class Store(object):
    def __init__(self):
        self.customers      = []
        self.checkOutPoints = {}        #key: CheckoutPoint object, value: Queue
    
    def acquire_customer(self, customer):
        self.customers.append(customer)
    
    def open_checkout_point(self, checkoutPoint):
        self.checkOutPoints[checkoutPoint] = collections.deque
        
        
class Customer(object):
    def __init__(self, numItems = None):
        if numItems == None: self.numItems = max(1, random.gauss(30, 10))
        else: self.numItems = numItems

        self.timeInLine      = 0
        self.timeCheckingOut = 0
        self.totalTime       = 0
    
store = Store()
     
register = CheckoutPoint(10)

store.open_checkout_point(register)
        