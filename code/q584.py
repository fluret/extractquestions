numbers = [10, 15, 20, 25]
distinct_divisors = tuple({divisor for divisor in range(1, num+1) if num % divisor == 0} for num in numbers)
print(numbers)
print(distinct_divisors)