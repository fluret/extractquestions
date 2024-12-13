class PrimeChecker:
    def __init__(self, num):
        self.num = num
 
    def is_prime(self):
        if self.num <= 1:
            return False
        if self.num == 2:
            return True
        if self.num % 2 == 0:
            return False
 
        # Check for divisibility from 3 to the square root of the number
        for i in range(3, int(self.num**0.5) + 1, 2):
            if self.num % i == 0:
                return False
 
        return True
 
num = int(input("Enter a Number : "))
 
checker = PrimeChecker(num)# Create an instance of PrimeChecker
 
if checker.is_prime():
    print(f"{num} is a Prime Number")
else:
    print(f"{num} is not a Prime Number")