class Student:
    def __init__(self, roll_number, name, percent):
        self.roll_number = roll_number
        self.name = name
        self.percent = percent
 
    def display_details(self):
        print("Roll Number :", self.roll_number)
        print("Name :", self.name)
        print("Percentage :", self.percent)
 
# Creating objects of the Student class with constructor initialization
s1 = Student(501, "Kim", 85.5)
s2 = Student(502, "Bob", 78.0)
s3 = Student(503, "Tin", 90.3)
 
print("Student 1 Details :")
s1.display_details()
 
print("\nStudent 2 Details :")
s2.display_details()
 
print("\nStudent 3 Details :")
s3.display_details()