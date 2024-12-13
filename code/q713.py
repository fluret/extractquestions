#Abstract Class
class Vehicle:
    def acclerate(self,name):
        pass
    def park(self,name):
        pass
 
class Bike(Vehicle):
    def acclerate(self, name):
        print(name,"is accelrating @ 60kmph")
    def park(self, name):
        print(name,"is parked at two wheeler parking")
 
class Car(Vehicle):
    def acclerate(self, name):
        print(name,"is accelrating @ 90kmph")
    def park(self, name):
        print(name,"is parked at four wheeler parking")
 
 
c = Car()
c.acclerate("Car")
c.park("Car")
 
b=Bike()
b.acclerate("Bike")
b.park("Bike")