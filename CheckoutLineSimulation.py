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
        self.currentCustomer = customer
    
    def process_customer(self):
        if self.currentCustomer == None: return
        self.currentCustomer.numItems -= self.itemsPerSecond
                                
class Store(object):
    def __init__(self):
        self.customers      = []
        self.checkoutPoints = {}
        self.checkedOutCustomers = []
    
    def acquire_customer(self, customer):
        self.customers.append(customer)
    
    def assign_customer_to_checkout_point(self, checkOutPoint, customer):
        self.checkoutPoints[checkOutPoint].append(customer)
    
    def open_checkout_point(self):
        self.checkoutPoints[CheckoutPoint()] = []  # consider making this a deque
    
    def run_sim(self, numCustomers, numCheckoutPoints):
        for i in range(numCustomers):
            cust = Customer()
            self.customers.append(cust)
        
        for j in range(numCheckoutPoints):
            self.open_checkout_point()

        flag = True
        while flag:
            flag = False
            for cp in self.checkoutPoints.keys():
                if cp.currentCustomer == None and self.checkoutPoints[cp]:
                    cp.assign_customer(self.checkoutPoints.popleft())
                else:
                    if self.customers:
                        cp.assign_customer(self.customers.pop())
                    
                if cp.currentCustomer:
                    flag = True
                    #print cp.currentCustomer.numItems
                    cp.process_customer()
                    cp.currentCustomer.timeInLine += 1
                    if cp.currentCustomer.numItems <= 0:
                        self.checkedOutCustomers.append(cp.currentCustomer)
                        cp.currentCustomer = None
        
        
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

store.open_checkout_point()
        
store.run_sim(10, 3)

#this should be printing 10 customers, not 4...
for i in store.checkedOutCustomers:
    print i.numItems
