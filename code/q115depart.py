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
