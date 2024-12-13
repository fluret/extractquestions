from abc import ABC, abstractmethod
 
class Shape(ABC):#Abstract base class
    @abstractmethod
    def area(self):
        pass
 
class Circle(Shape):# Create a subclass of Shape
    def __init__(self):
        self.radius = float(input("Enter the Radius :"))
 
    def area(self):
        return 3.1415 * self.radius * self.radius
 
class Rectangle(Shape):# Create a subclass of Shape
    def __init__(self):
        self.length = float(input("Enter the Length :"))
        self.width = float(input("Enter the Width :"))
 
    def area(self):
        return self.length * self.width
 
 
# Create instances of the subclasses
cir = Circle()
rect = Rectangle()
 
# Call the area method on the objects
print("Area of Circle :", cir.area())
print("Area of Rectangle :", rect.area())