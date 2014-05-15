#Checkout Line Simulation

'''
Questions this simulation hope to answer:

For every additional register, how much faster is the checkout time?

Is it faster to have one line that sends the customers to the next available
register, or to have people pick a line and stick with it?

Does switching lines help?

What is the relationship between checkout time and total itemsPerSecond across
all cashiers vs checkout time vs number of cashiers?

'''


import random
import collections

class Register(object):
    def __init__(self, itemsPerSecond):
        self.itemsPerSecond = itemsPerSecond
        #self.isWorking      = True
    

class Store(object):
    def __init__(self, numRegisters):
        self.registers = []
        for i in range(numRegisters):
            self.registers.append(collections.deque)
    
    def find_shortest_line(self):
        return min(self.registers, key = len)
    
    def join_line(self, customer, registerNumber):
        self.registers[registerNumber].append(customer)
        
    def rem_from_line(self):
        """returns the customer object of the next in line"""
        return self.registers.popleft()
    
    
class Customer(object):
    def __init__(self, numItems):
        self.numItems        = numItems
        self.timeInLine      = 0
        self.timeCheckingOut = 0
        self.totalTime       = 0
        #self.paymentProblem  = False
    
        
        