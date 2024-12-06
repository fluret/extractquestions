class Person:
    # Define the class parameter "name"
    name = "Nom non attribué"
    
    def __init__(self, name = None):
        if name is None:
            self.name = self.name
        else:
            self.name = name

jeffrey = Person("Jeffrey")
print(f"Person.name : {Person.name} et jeffrey.name : {jeffrey.name}")


nico = Person()
print(f"Person.name : {Person.name}, nico.name : {nico.name}")
nico.name = "Nico"
print(f"Person.name : {Person.name}, nico.name : {nico.name}")