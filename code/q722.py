class PalindromeChecker:
    def __init__(self, num):
        self.num = num
 
    def is_palindrome(self):
        num_str = str(self.num)
        reversed_str = num_str[::-1]  # Reverse the string        
        return num_str == reversed_str	# Check if the reversed string is equal to the original string
 
 
num = int(input("Enter a Number : "))
 
checker = PalindromeChecker(num)
 
if checker.is_palindrome():
    print(f"{num} is a Palindrome Number")
else:
    print(f"{num} is not a Palindrome Number")