class Student:
	# Class variable to keep track of the number of objects created
	count = 0
 
	def __init__(self,name,age):
		self.name = name
		self.age = age
		Student.count += 1 # Increment the count when an object is created
 
	def GetDetails(self):
		print("Name :",self.name)
		print("Age :",self.age)
 
# Create instances of MyClass
s1 = Student("Sam Kumar",21)
s2 = Student("Tiya",20)
s3 = Student("Sathish",19)
s3 = Student("Deepika",21)
 
# Print the number of objects created
print("Number of Objects : ", Student.count)