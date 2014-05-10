#simulate traffic on a single lane road

import Queue

class Car(object):
    def __init__(self, desiredSpeed, carInFront):
        self.desiredSpeed = speed
        self.curSpeed   = speed
        self.carInFront = carInFront
        self.location = 0

class Road(object):
    def __init__(self, distance):
        self.distance = distance
        self.carsOnRoad = Queue.deque()
    
    def add_car(self, car):
        self.carsOnRoad.appendleft(car)
    
    def rem_car(self):
        self.carsOnRoad.pop()
    
    def update_car_positions(self, data):
        if len(self.carsOnRoad == 0): return
        closestCar = self.carsOnRoad[-1]
        if closestCar.location >= self.distance:
            #update next car's speed to desiredSpeed
            data.add_car(self.rem_car())
            
        for car in self.carsOnRoad:
            #update speed
            #update location
            pass
                

class Data(object):
    def __init__(self):
        self.cars = []      #just collect objects for now...
    
    def add_car(self, car):
        self.cars.append(car)


