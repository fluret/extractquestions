class SchoolHeightRecords:
    def __init__(self):
        self.student_records = {}
 
    def add_student(self, student_name, height):
        self.student_records[student_name] = height
 
    def remove_student(self, student_name):
        if student_name in self.student_records:
            del self.student_records[student_name]
            print(f"{student_name} Records Remove Success")
        else:
            print(f"{student_name} Not Found in Records")
 
    def find_student_height(self, student_name):
        if student_name in self.student_records:
            return self.student_records[student_name]
        else:
            return None
 
    def display_records(self):
        print("Student Height Records:")
        for student, height in self.student_records.items():
            print(f"{student} : {height} cm")
 
 
school_records = SchoolHeightRecords()
 
print("1. Add Student Height")
print("2. Remove Student Height")
print("3. Find Student Height")
print("4. Display All Records")
print("5. Quit")
 
while True:
 
    choice = int(input("\nEnter your Choice : "))
 
    if choice == 1:
        student_name = input("Enter Student Name : ")
        height = input("Enter Student Height (in cm) : ")
        school_records.add_student(student_name.upper(), height)
        print(f"{student_name}'s Height Added to Records.")
    elif choice == 2:
        student_name = input("Enter Student Name to Remove : ")
        school_records.remove_student(student_name.upper())
    elif choice == 3:
        student_name = input("Enter Student Name to find Height : ")
        height = school_records.find_student_height(student_name.upper())
        if height is not None:
            print(f"{student_name}'s Height : {height} cm")
        else:
            print(f"{student_name} Not Found in Records")
    elif choice == 4:
        school_records.display_records()
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please try again")