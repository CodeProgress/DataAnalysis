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
import Queue

class CheckoutPoint(object):
    def __init__(self, itemsPerMinute = 10):
        self.itemsPerMinute  = itemsPerMinute
        self.itemsPerSecond  = itemsPerMinute/60.
        self.currentCustomer = None
        self.line            = collections.deque()
        
    def start_checking_out_customer(self, customer):
        self.currentCustomer = customer
    
    def is_occupied(self):
        if self.currentCustomer.numItems <= 0:
            self.currentCustomer = None 
            return True
        self.currentCustomer.numItems -= self.itemsPerSecond
        return False
                                
class Store(object):
    def __init__(self):
        self.customers      = []
        self.checkoutPoints = Queue.PriorityQueue()   #(priority_number, data)
    
    def acquire_customer(self, customer):
        self.customers.append(customer)
    
    def open_checkout_point(self):
        newRegister = (0, CheckoutPoint())
        self.checkoutPoints.put(newRegister)
        
class Customer(object):
    def __init__(self, numItems = None):
        if numItems == None: 
            self.numItems = max(1, random.gauss(30, 10))
        else: 
            self.numItems = numItems
        
        self.timeInLine      = 0
        self.timeCheckingOut = 0
        self.totalTime       = 0
    
        
    
    
store = Store()
     
register = CheckoutPoint()

store.open_checkout_point()
        
print store.checkoutPoints.get()
