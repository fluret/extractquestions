class Number:
    def __init__(self, value):
        self.value = value
 
    def __str__(self):
        return str(self.value)
 
    def __gt__(self, other):
        return self.value > other.value
 
# Create two Number objects
number1 = Number(5)
number2 = Number(3)
 
# Compare the two numbers using the > operator in an expression
res = number1 > number2
 
if res:
    print(number1, "is greater than", number2)
else:
    print(number1, "is not greater than", number2)