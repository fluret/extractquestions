class Student:
    def __init__(self, student_id, name, per):
        self.student_id = student_id
        self.name = name
        self.per = per
 
    def __str__(self):
        return "Student ID : " + str(self.student_id) + "\nStudent Name : " + self.name + "\nPercentage : " + str(self.per)
 
# Create an array (list) of Student objects
students = [
	    Student(101, "Mithra", 85.5),
	    Student(102, "Akhil", 78.0),
	    Student(103, "Tiya", 92.5),
	    Student(104, "Ramesh", 84.5),
	    Student(105, "Sam Kumar", 65.5)
	   ]
 
def search_student_by_id(student_id):	# search for a student by ID
    for student in students:
        if student.student_id == student_id:
            return student
    return None
 
# Print all student IDs
print("*** Student IDs ***")
for student in students:
    print(student.student_id)
 
search_id = int(input("\nEnter Student ID to Search : "))
 
found_student = search_student_by_id(search_id) # Search for the student by ID
 
if found_student:
    print("Student Found")
    print(found_student)
else:
    print("Student Not Found")