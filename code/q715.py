class Details:
    def __init__(self):
        self.name = ""
        self.total = 0
        self.per = 0
 
    def setData(self,name,total,per):
        self.name = name
        self.total = total
        self.per = per
 
    def showData(self):
        print("Name :", self.name)
        print("Total :", self.total)
        print("Percentage :", self.per)
 
class Student(Details): #Inheritance
    def __init__(self):
        self.Grade = ""
 
    def setStudent(self,name,total,per,grade):
        self.setData(name,total,per)
        self.grade = grade
 
    def showStudent(self):
        self.showData()
        print("Grade :", self.grade)
 
 
e=Student()
e.setStudent("Kim",430,86.00,'B')
e.showStudent()