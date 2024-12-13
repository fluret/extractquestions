numbers = [123, 456, 789]
digit_sums = tuple(sum(int(digit) for digit in str(num)) for num in numbers)
print(numbers)
print(digit_sums)