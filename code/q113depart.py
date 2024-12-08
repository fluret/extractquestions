class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"{self.name}, {self.age} years old, {self.gender}"


# Create an instance of the Person class
person1 = Person("Juan", 25, "Male")

# Print the information of the person using the __str__ method
print(person1)  # Output: Juan, 25 years old, Male
