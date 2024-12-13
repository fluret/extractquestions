class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
def find_elder(person1, person2):
    if person1.age > person2.age:
        return person1
    elif person2.age > person1.age:
        return person2
    else:
        return None
 
# Create two Person objects
person1 = Person("Sathish", 27)
person2 = Person("Pooja", 25)
 
# Find the elder person
elder = find_elder(person1, person2)
 
if elder is None:
    print("Both persons are of the same age")
else:
    print(f"Elder Person \nName : {elder.name} \nAge : {elder.age}")