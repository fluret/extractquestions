class Student:
    def __init__(self, roll_number, name, marks):
        self.roll_number = roll_number
        self.name = name
        self.marks = marks
 
    def __str__(self):
        return f"Roll Number : {self.roll_number}\nStudent Name : {self.name}\nMarks : {self.marks}"
 
students = [] # Create an array (list) of Student objects
 
students.append(Student(101, "Mithra", 85.5)) # Add students to the array
students.append(Student(102, "Akhil", 78.0))
students.append(Student(103, "Sathish", 92.5))
 
for student in students: # print individual student details
    print(student,"\n")
 
# Access and modify attributes of a student
student = students[0]
print("Before Update : ",student)
student.name = "Pooja"
student.marks = 90.0
print("\nAfter Update : ",student)