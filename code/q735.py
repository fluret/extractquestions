class MyClass:
	def __init__(self, value):
		self.value = value
 
def process_object(obj):    
	obj.value *= 2	# Modify the object or perform some operations
	return obj	 # Return the modified object
 
my_obj = MyClass(10)	# Create an object of MyClass
 
result_obj = process_object(my_obj) # Call the function and pass the object as an argument
 
print("Original Object :",my_obj.value)
print("Modified Object :",result_obj.value)