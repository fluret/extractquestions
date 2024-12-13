import math
numbers = [1, 2, 3, 4, 5]
factorial_tuples = tuple((x, math.factorial(x)) for x in numbers)
print(numbers)
print(factorial_tuples)