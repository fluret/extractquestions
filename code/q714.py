import math
class Shape: #Interface
    def input(self):pass
    def process(self):pass
    def output(self):pass
 
class Circle(Shape):
    def __init__(self,rad=0.0):
        self.radius = rad
        self.area = 0.0
 
    def setdata(self):
        self.radius = float(input("Enter radius :"))
 
    def circle_area(self):
        self.area = math.pi*math.pow(self.radius,2)
 
    def getdata(self):
        print("Circle Area :",self.area)
 
class Rectangle(Shape):
    def __init__(self,len=0,bre=0):
        self.len = len
        self.bre = bre
        self.area = 0
 
    def setdata(self):
        self.len = int(input("Enter Length :"))
        self.bre = int(input("Enter Breadth :"))
 
    def rect_area(self):
        self.area = self.len*self.bre
 
    def getdata(self):
        print("Rectangle Area :",self.area)
 
c = Circle()
c.setdata()
c.circle_area()
c.getdata()
 
r = Rectangle()
r.setdata()
r.rect_area()
r.getdata()