class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
# Create an array of Person objects
people = [
    Person("Kim", 21),
    Person("Sam", 30),
    Person("Charlie", 29),
    Person("Bob", 25),
    Person("Tiya", 27),
]
 
# Define a function to filter people older than a certain age
def is_older_than_25(person):
    return person.age > 25
 
# Use the filter() method to search for people older than 25
filtered_people = filter(is_older_than_25, people)
 
# Convert the filtered result to a list (optional)
filtered_people_list = list(filtered_people)
 
# Display the filtered results without f-strings
print("People older than 25 :")
for person in filtered_people_list:
    print("Name :", person.name)
    print("Age :", person.age)