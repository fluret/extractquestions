class Student:
    def __init__(self): #Constructor
        self.name = ""
        self.total = ""
        self.per = 0
 
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name
 
    def setTotal(self,total):
        self.total = total
    def getTotal(self):
        return self.total
 
    def setPercentage(self,per):
        self.per = per
    def getPercentage(self):
        return self.per
 
# Get user input for name, total, and percentage
name = input("Enter a Name :")
total = int(input("Enter a Total :"))
per = float(input("Enter a Percentage :"))
 
s = Student()
 
#Set the attributes using setter methods
s.setName(name)
s.setTotal(total)
s.setPercentage(per)
 
# Get the attributes using getter methods
n = s.getName()
t = s.getTotal()
p = s.getPercentage()
 
print("\nDisplaying Student Details")
print("Name :", n)
print("Total :", t)
print("Percentage :", p)