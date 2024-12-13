class Person:	# Base class
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def display_info(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
 
class Student(Person):	# Intermediate class inheriting from Person
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
 
    def display_student_info(self):
        super().display_info()
        print("Student ID : ",self.student_id)
 
 
class GraduateStudent(Student):	 # Derived class inheriting from Student
    def __init__(self, name, age, student_id, research_topic):
        super().__init__(name, age, student_id)
        self.research_topic = research_topic
 
    def display_graduate_info(self):
        super().display_student_info()
        print("Research Topic : ",self.research_topic)
 
# Create an instance of GraduateStudent
graduate_student = GraduateStudent("Alice", 25, "STU001", "Machine Learning")
 
# Display information using the multilevel inheritance
graduate_student.display_graduate_info()