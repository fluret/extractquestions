numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
multiples_of_3_squares = {x: x ** 2 for x in numbers if x % 3 == 0}
print(numbers)
print(multiples_of_3_squares)