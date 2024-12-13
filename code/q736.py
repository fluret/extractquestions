# Decorator function
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called")
        func()
        print("Something is happening after the function is called")
    return wrapper
 
# Function to be decorated
@my_decorator
def msg():
    print("Hello world !")
 
# Call the decorated function
msg()