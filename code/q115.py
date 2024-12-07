### code départ
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def is_adult(age):
        return age >= 18

# Creating instances of Person
person1 = Person("Alice", 25)
person2 = Person("Bob", 16)

# Using the static method to check if a person is an adult
is_adult_person1 = Person.is_adult(person1.age)
is_adult_person2 = Person.is_adult(person2.age)
print(f"{person1.name} is an adult: {is_adult_person1}")
print(f"{person2.name} is an adult: {is_adult_person2}")
### correction
# Your code here

class MathOperations:

    @staticmethod
    def add_numbers(num1, num2):
        return num1 + num2

# You can call the static method without creating an instance
sum_of_numbers = MathOperations.add_numbers(10, 15)

print(f"Sum of Numbers: {sum_of_numbers}")
### test.py
import pytest
from app import MathOperations

@pytest.mark.it("The 'MathOperations' class should exist")
def test_math_operations_class_exists():
    try:
        assert MathOperations
    except AttributeError:
        raise AttributeError("The class 'MathOperations' should exist in app.py")

@pytest.mark.it("The MathOperations class includes the 'add_numbers' static method")
def test_math_operations_has_add_numbers_static_method():
    assert hasattr(MathOperations, "add_numbers")

@pytest.mark.it("The 'add_numbers' static method should return the expected sum")
def test_add_numbers_static_method_returns_expected_sum():
    result = MathOperations.add_numbers(5, 7)
    assert result == 12

@pytest.mark.it("The 'add_numbers' static method should return the expected sum. Testing with different values")
def test_add_numbers_static_method_returns_expected_sum_for_different_values():
    result = MathOperations.add_numbers(10, 20)
    assert result == 30