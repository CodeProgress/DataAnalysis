#Checkout Line Simulation

import random
import Queue

'''
Questions this simulation hopes to answer:

For every additional register, how much faster is the checkout time?

Is it faster to have one line that sends the customers to the next available
register, or to have people pick a line and stick with it?

Does switching lines help?

What is the relationship between checkout time and total itemsPerSecond across
all cashiers vs checkout time vs number of cashiers?

If customer is allowed to choose the line, how is overall checkout time affected
when they choose optimally, choose shortest line, choose randomly?

'''
#Time is an integer

class Cashier(object):
    def __init__(self, itemsPerSecond, ID):
        self.itemsPerSecond     = itemsPerSecond
        self.currentCustomer    = None
        self.completedCustomers = []
        self.line               = Queue.Queue()
        self.checkoutTime       = 0.
        self.cashierID          = ID
    
    def checkout_customer(self):
        if self.currentCustomer:
            self.currentCustomer.numItems -= self.itemsPerSecond
            if self.currentCustomer.numItems < 0:
                self.completedCustomers.append(self.currentCustomer)
                self.currentCustomer = None
                return True
        elif not self.line.empty(): 
            self.currentCustomer = self.line.get()  
        return False  
            
    def add_customer_to_line(self, customer):
        self.line.put(customer)
    
    def most_resent_completed_customer(self):
        return self.completedCustomers[-1]
        
class Customer(object):
    def __init__(self):
        self.numItems    = 0
        self.timeInStore = 0
        self.willLeaveAfterNumSeconds = abs(random.gauss(1500, 1000))
    
    def add_to_basket(self):
        #add an item per minute
        if self.timeInStore % 60 == 0:
            self.numItems += 1
    
    def is_ready_to_checkout(self):
        return self.timeInStore > self.willLeaveAfterNumSeconds
    
    def pick_shortest_line(self, cashiers):
        return sorted(cashiers, key=lambda x: x.line.qsize())[0]
        
    def __str__(self):
        return str(vars(self))
        
        