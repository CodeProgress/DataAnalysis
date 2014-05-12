#simulate traffic on a single lane road

import Queue
import random
import pylab

class Car(object):
    def __init__(self, desiredSpeed, carInFront):
        self.desiredSpeed   = desiredSpeed
        self.curSpeed       = desiredSpeed
        self.carInFront     = carInFront
        self.location       = 0.              #also measures distance traveled
        self.timeOnRoad     = 0.
        self.carLength      = .002           #car length is about 1/500 of a mile
        self.timeTolerance  = 1/3600.
        self.averageSpeed   = 0.
        self.timeTailgating = 0.
    
    def get_needed_spacing(self):
        return self.curSpeed/10. * self.carLength 
    
    def is_too_close(self):
        if self.carInFront == None:
            return False
        distanceToCarInFront = self.carInFront.location - self.location
        if distanceToCarInFront < self.get_needed_spacing():
            return True
        return False
    
    def move(self):
        """move equivalent of distance traveled in speed * tolerance
        example: 1/3600. translates to distance in one second"""
        if self.is_too_close():
            self.location = max(0, self.carInFront.location - self.get_needed_spacing())
            self.curSpeed = min(self.carInFront.curSpeed, self.desiredSpeed)
        else:
            self.location += self.curSpeed * self.timeTolerance
            self.curSpeed = self.desiredSpeed
    
    def incr_time_on_road(self):
        if self.location > 0:
            self.timeOnRoad += self.timeTolerance
        if self.is_too_close():
            self.timeTailgating += self.timeTolerance    
        
    def calc_average_speed(self, distance):
        self.averageSpeed = self.location/self.timeOnRoad
    
    def __str__(self):
        return    'Desired speed    = {} \
                    \n Current speed = {} \
                    \n Car in front  = {} \
                    \n Location      = {} \
                    \n Time on road  = {} \
                    \n Average speed = {} \
                    \n'.format(self.desiredSpeed,
                                self.curSpeed,
                                self.carInFront,
                                self.location,
                                self.timeOnRoad,
                                self.averageSpeed) 
    
class Road(object):
    def __init__(self, distance, numCars, speedMu, speedSigma, minSpeed = 0):
        self.carsOnRoad    = Queue.deque()
        self.distance      = distance      #miles
        self.numCars       = numCars
        self.speedMu       = speedMu
        self.speedSigma    = speedSigma
        self.minSpeed      = minSpeed
        self.Data          = Data()
        self.totalTime     = 0
        
    def add_car(self, car):
        self.carsOnRoad.appendleft(car)
    
    def add_random_car(self):
        randomSpeed = max(random.gauss(self.speedMu, self.speedSigma), self.minSpeed)
        if len(self.carsOnRoad) == 0:
            carInFront = None
        else:
            carInFront = self.carsOnRoad[-1]
        car = Car(randomSpeed, carInFront)
        self.add_car(car)
    
    def rem_car(self):
        return self.carsOnRoad.pop()
    
    def adjust_speed(self, car):
        if car.carInFront == None or not car.is_too_close(self.get_needed_spacing(car)):
            car.curSpeed = car.desiredSpeed
        else:
            car.curSpeed = car.carInFront.curSpeed
    
    def update_car_positions(self):
        if len(self.carsOnRoad) == 0: return

        #see if closest car to end needs to be removed
        while True:
            closestCar = self.carsOnRoad[-1]
            if closestCar.location >= self.distance:
                closestCar.calc_average_speed(self.distance)
                self.Data.add_car(self.rem_car())
                if len(self.carsOnRoad) == 0: 
                    return
                else:
                    self.carsOnRoad[-1].carInFront = None
            else:
                break
            
        for car in self.carsOnRoad:
            car.move()
            car.incr_time_on_road()
        
        return
    
    def run_simulation(self, numSims):
        """returns the data object that holds all final car data"""
        for i in range(numSims):
            for i in range(self.numCars):
                self.add_random_car()
            
            while len(self.carsOnRoad) != 0:
                self.update_car_positions()
        
        return self.Data

class Data(object):
    def __init__(self):
        self.cars = []      #just collect objects for now...
    
    def add_car(self, car):
        self.cars.append(car)
    
    def plot_data(self):
        desiredSpeeds = [x.desiredSpeed for x in self.cars]
        pylab.scatter(desiredSpeeds, [x.timeOnRoad for x in self.cars], label = "Total Time on Road")
        pylab.scatter(desiredSpeeds, [x.timeTailgating for x in self.cars], color = 'red', label = "Time Tailgating")
        pylab.xlabel("Desired Speed")
        pylab.ylabel("Time On Road")
        pylab.legend()
        pylab.show()

#for i in myRoad.Data.cars: print i      

myRoad = Road(5, 50, 65, 5, 55)
myRoad.run_simulation(10)
myRoad.Data.plot_data()

