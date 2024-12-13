class Student:
	def __init__(self):
		self.student_details = {}
 
	@property
	def input_student_details(self):	# input student details
		roll_number = input("Enter Roll Number : ")
		name = input("Enter Student Name : ")
		marks = float(input("Enter Marks : "))
		self.student_details[roll_number] = {'name': name, 'marks': marks}
		print("Marks Added successfully")
 
	def update_student_marks(self):	  # update student marks
		roll_number = input("Enter Roll Number of the Student to Update Marks : ")
		if roll_number in self.student_details:
			new_marks = float(input("Enter New Marks : "))
			self.student_details[roll_number]['marks'] = new_marks
			print("Marks updated successfully")
		else:
			print("Student not found")
 
	def print_student_details(self):	# print student details
		roll_number = input("Enter Roll Number of the student to view details : ")
		if roll_number in self.student_details:
			student = self.student_details[roll_number]
			print("Roll Number :", roll_number)
			print("Student Name :", student['name'])
			print("Marks :", student['marks'])
		else:
			print("Student not found")
 
obj = Student()
 
while True:
    print("\n ********* Student Management System *********  ")
    print("\n1. Input Student Details")
    print("2. Update Student Marks")
    print("3. Print Student Details")
    print("4. Exit")
 
    choice = input("\nEnter your Choice (1 to 4): ")
 
    if choice == '1':
        obj.input_student_details
    elif choice == '2':
        obj.update_student_marks()
    elif choice == '3':
        obj.print_student_details()
    elif choice == '4':
        print("Exiting the program")
        break
    else:
        print("Invalid Choice. Please Try Again !!!")