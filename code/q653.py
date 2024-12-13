import random
 
numbers = {1, -2, 3, -4, 5}
positive_numbers = {x for x in numbers if x >= 0}
print(numbers)
print(positive_numbers)