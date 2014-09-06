#Checkout Line Simulation

import random
import Queue
import pylab
#import cProfile

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
        return False  
            
    def add_customer_to_line(self, customer):
        self.line.put(customer)
    
    def most_resent_completed_customer(self):
        return self.completedCustomers[-1]
        
class Customer(object):
    def __init__(self):
        self.startingNumItems         = 0
        self.numItems                 = 0
        self.startTime                = 0
        self.timeOnLine               = 0
        self.timeAtRegister           = 0
        self.averageNumItems          = 20
        self.stdDev                   = 10
    
    def finish_shopping(self, time):
        self.numItems = int(abs(random.gauss(self.averageNumItems, self.stdDev)))
        self.startingNumItems = int(self.numItems)
        self.startTime = time 
        
    def pick_shortest_line(self, cashiers):
        return sorted(cashiers, key=lambda x: x.line.qsize())[0]
    
    def calc_time_on_line(self, currentTime):
        temp = self.startTime
        self.startTime = currentTime    #reset startTime for calc_time_at_register
        self.timeOnLine = currentTime - temp
    
    def calc_time_at_register(self, currentTime):
        self.timeAtRegister = currentTime - self.startTime   
                
    def __str__(self):
        return str(vars(self))
        
class Store(object):
    def __init__(self, customersPerMinute = 10):
        self.customersPerMinute  = customersPerMinute
        self.time                = 0  #seconds
        self.numCashiers         = 0
        self.totalNumOfCustomers = 0.
        self.cashiers            = []
        self.newCustomers        = []
        self.completedCustomers  = []
        
    def add_cashier(self): 
        itemsPerSecond = 1 
        newCashier = Cashier(itemsPerSecond, self.numCashiers)
        self.cashiers.append(newCashier)
        self.numCashiers += 1
    
    def create_customers(self, numCustomersToCreate = 1):
        for i in range(numCustomersToCreate):
            self.newCustomers.append(Customer())
    
    def new_customers_shop(self):
        for cust in self.newCustomers:
            cust.finish_shopping(self.time)
    
    def move_new_customers_to_checkout(self):
        for cust in self.newCustomers:
            cust.pick_shortest_line(self.cashiers).add_customer_to_line(cust)
            cust.startTime = self.time  
        self.newCustomers = []
    
    def finish_customer_checkout(self, cashier):
        finishedCust = cashier.most_resent_completed_customer()
        finishedCust.calc_time_at_register(self.time)
        self.completedCustomers.append(finishedCust)
    
    def move_next_in_line_to_register(self, cashier):
        if not cashier.line.empty():
            cashier.currentCustomer = cashier.line.get()
            cashier.currentCustomer.calc_time_on_line(self.time)
    
    def checkout_customers(self):
        for cashier in self.cashiers:
            isCheckoutComplete = cashier.checkout_customer()
            if isCheckoutComplete:
                self.finish_customer_checkout(cashier)
            if cashier.currentCustomer == None:
                self.move_next_in_line_to_register(cashier)
    
    def percent_of_total_customers_completed(self):
        if self.totalNumOfCustomers > 0:
            return len(self.completedCustomers)/self.totalNumOfCustomers
        return 0.
                  
    def run_simulation(self, numCashiers = 3, totalSimulationTime = 5000):
        assert self.customersPerMinute > 0
        assert numCashiers == int(numCashiers)
        for cashier in range(numCashiers):
            self.add_cashier()
        
        while self.time < totalSimulationTime:
            if self.time % 60 == 0:
                self.create_customers(self.customersPerMinute)
                self.new_customers_shop()
                self.move_new_customers_to_checkout()
                self.totalNumOfCustomers += self.customersPerMinute
            self.checkout_customers()
            
            self.time += 1
            
        return self.completedCustomers
    
    def reset_store(self):
        self.time                = 0  #seconds
        self.numCashiers         = 0
        self.totalNumOfCustomers = 0
        self.cashiers            = []
        self.newCustomers        = []
        self.completedCustomers  = []



