### code départ
class Person:
    total_people = 0  # Class variable to keep track of the total number of people

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.total_people += 1  # Increment the total_people count for each new instance

    @classmethod
    def get_total_people(cls):
        return cls.total_people

# Creating instances of Person
person1 = Person("Alice", 25)
person2 = Person("Bob", 16)

# Using the class method to get the total number of people
total_people = Person.get_total_people()
print(f"Total People: {total_people}")
### correction
# Your code here

class MathOperations:
    pi = 3.14159

    @classmethod
    def calculate_circle_area(cls, radius):
        area = cls.pi * radius ** 2
        return area

circle_area = MathOperations.calculate_circle_area(5)

print(f"Circle Area: {circle_area}")
### test.py
import pytest
from app import MathOperations

@pytest.mark.it("The 'MathOperations' class should exist")
def test_math_operations_class_exists():
    try:
        assert MathOperations
    except AttributeError:
        raise AttributeError("The class 'MathOperations' should exist in app.py")


@pytest.mark.it("The MathOperations class includes the 'calculate_circle_area' class method")
def test_math_operations_has_calculate_circle_area_class_method():
    assert hasattr(MathOperations, "calculate_circle_area")


@pytest.mark.it("The 'calculate_circle_area' class method should return the expected circle area")
def test_calculate_circle_area_class_method_returns_expected_area():
    result = MathOperations.calculate_circle_area(5)
    assert result == 78.53975

@pytest.mark.it("The 'calculate_circle_area' class method should return the expected circle area. Testing with different values")
def test_calculate_circle_area_class_method_returns_expected_area_for_radius_10():
    result = MathOperations.calculate_circle_area(10)
    assert result == 314.159