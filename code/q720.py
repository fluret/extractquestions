class ArmstrongChecker:
    def __init__(self, num):
        self.num = num
 
    def is_armstrong(self):        
        num_str = str(self.num)	# Convert the number to a string to count the digits        
        num_digits = len(num_str)	# Calculate the number of digits
        digit_sum = sum(int(digit) ** num_digits for digit in num_str)	# Calculate the sum of the nth powers of its digits        
        return digit_sum == self.num	# Check if the sum is equal to the original number
 
num = int(input("Enter a Number : "))
 
checker = ArmstrongChecker(num)
 
if checker.is_armstrong():
    print(f"{num} is an Armstrong Number")
else:
    print(f"{num} is not an Armstrong Number")