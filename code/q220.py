fruits = ["mango", "kiwi", "strawberry", "guava", "pineapple", "mandarin orange"]
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)