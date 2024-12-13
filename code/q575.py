numbers = [10, -5, 20, -15, 30]
positive = tuple(x for x in numbers if x >= 0)
negative = tuple(x for x in numbers if x < 0)
print(numbers)
print(positive)
print(negative)