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
    def __init__(self, itemsPerMinute = 20):
        self.itemsPerMinute  = itemsPerMinute
        self.itemsPerSecond  = itemsPerMinute/60.
        self.currentCustomer = None
        self.line            = collections.deque()
        
    def assign_customer(self, customer):
        self.line.append(customer)
    
    def process_customer(self):
        if self.currentCustomer == None: 
            return
        self.currentCustomer.numItems -= self.itemsPerSecond
        self.currentCustomer.timeInLine += 1
    
    def is_done_with_customer(self):
        if self.currentCustomer == None:
            return True
        return self.currentCustomer.numItems <= 0
    
    def take_next_customer(self):
        if self.currentCustomer == None:
            if self.line:
                self.currentCustomer = self.line.popleft()
                                
class Store(object):
    def __init__(self):
        self.customers      = []
        self.checkoutPoints = []
        self.checkedOutCustomers = []
    
    def acquire_customer(self, customer):
        self.customers.append(customer)
    
    def assign_customer_to_checkout_point(self, checkOutPoint, customer):
        self.checkoutPoints[checkOutPoint].append(customer)
    
    def open_checkout_point(self):
        self.checkoutPoints.append(CheckoutPoint())  # consider making this a deque
    
    def distribute_customers(self):
        index = 0
        while self.customers:
            nextCust = self.customers.pop()
            nextClerk = self.checkoutPoints[index]
            nextClerk.assign_customer(nextCust)
            index += 1
            index %= len(self.checkoutPoints)        
    
    def run_sim(self, numCustomers, numCheckoutPoints):
        for i in range(numCustomers):
            cust = Customer()
            self.customers.append(cust)
        
        
        for j in range(numCheckoutPoints):
            self.open_checkout_point()
            
        self.distribute_customers()
        
        print self.checkoutPoints
        
        for cp in self.checkoutPoints:
            cp.take_next_customer()
            cp.process_customer()
            if cp.currentCustomer and cp.is_done_with_customer():
                self.checkedOutCustomers.append(cp.currentCustomer)
                cp.currentCustomer == None
                cp.take_next_customer()
                    
                
        
class Customer(object):
    def __init__(self, numItems = None):
        if numItems == None: 
            self.numItems = max(1, random.gauss(30, 10))
        else: 
            self.numItems = numItems
        
        self.timeInLine      = 0
        self.timeCheckingOut = 0
        self.totalTime       = 0
        
    def __str__(self):
        return 'Time in line: {}, time checking out {}, total time{}'.\
                format(self.timeInLine, self.timeCheckingOut, self.totalTime)
    
        
    
store = Store()
     
register = CheckoutPoint()
        
store.run_sim(10, 4)

#this should be printing 10 customers, not 4...
for i in store.checkedOutCustomers:
    print i.numItems
