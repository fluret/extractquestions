class Person:
    total_people = 0  # Class variable to keep track of the total number of people

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.total_people += (
            1  # Increment the total_people count for each new instance
        )

    @classmethod
    def get_total_people(cls):
        return cls.total_people


# Creating instances of Person
person1 = Person("Alice", 25)
person2 = Person("Bob", 16)

# Using the class method to get the total number of people
total_people = Person.get_total_people()
print(f"Total People: {total_people}")
