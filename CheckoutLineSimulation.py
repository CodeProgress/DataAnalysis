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
        
class Store(object):
    def __init__(self):
        self.cashiers           = []
        self.customersShopping  = set()
        self.readyToCheckout    = set()
        self.completedCustomers = []
        self.numCashiers        = 0
        self.time               = 0  #seconds
    
    def add_cashier(self): 
        itemsPerSecond = 1 
        newCashier = Cashier(itemsPerSecond, self.numCashiers)
        self.cashiers.append(newCashier)
        self.numCashiers += 1
    
    def add_customer_to_store(self):
        if random.random() > .9:
            self.customersShopping.add(Customer()) 
    
    def customers_shop(self):
        '''This is the most expensive method, taking up half of total program
        runtime. This could be calculated ahead of time and fed directly into
        move_ready_customers_to_checkout
        '''
        for cust in self.customersShopping:
            cust.timeInStore += 1
            cust.add_to_basket()
            if cust.is_ready_to_checkout():
                self.readyToCheckout.add(cust)
    
    def move_ready_customers_to_checkout(self):
        self.customersShopping -= self.readyToCheckout
        for cust in self.readyToCheckout:
            cust.pick_shortest_line(self.cashiers).add_customer_to_line(cust)  
        self.readyToCheckout = set()
    
    def checkout_customers(self):
        for cashier in self.cashiers:
            if cashier.checkout_customer():
                self.completedCustomers.append(cashier.most_resent_completed_customer())
        
    def run_simulation(self, numCashiers = 3, numSeconds = 5000):
        for cashier in range(numCashiers):
            self.add_cashier()
        
        while self.time < numSeconds:
            self.add_customer_to_store()
            self.customers_shop()
            self.move_ready_customers_to_checkout()
            self.checkout_customers()
            
            self.time += 1
            
        return self.completedCustomers
        
store = Store()
store.run_simulation()
