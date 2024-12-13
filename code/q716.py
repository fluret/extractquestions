class Details:
    def __init__(self):
        self.idn = 0
        self.name = ""
        self.gender = ""
 
    def setDetails(self):
        self.idn = input("Enter the ID Number : ")
        self.name = input("Enter the Name : ")
        self.gender = input("Enter the Gender : ")
 
    def showDetails(self):
        print("ID : ",self.idn)
        print("Name : ",self.name)
        print("Gender : ",self.gender)
 
class Student(Details):
    def __init__(self):
        self.total = 0
        self.per = 0
 
    def setStudent(self):
        self.setDetails()
        self.total = int(input("Enter the Total Mark : "))
        self.per = float(input("Enter the Percentage : "))
 
    def showStudent(self):
        self.showDetails()
        print("Total : ",self.total)
        print("Percentage : ",self.per)
 
class Staff(Details):
    def __init__(self):
        self.depart = ""
        self.salary = ""
 
    def setStaff(self):
        self.setDetails()
        self.depart = input("Enter the Department : ")
        self.salary = float(input("Enter the Salary : "))
 
    def showStaff(self):
        self.showDetails()
        print("Department : ",self.depart)
        print("Salary : ",self.salary)
 
print("Student Details : ")
stu = Student()
stu.setStudent()
stu.showStudent()
 
print("\nStaff Details : ")
stf = Staff()
stf.setStaff()
stf.showStaff()