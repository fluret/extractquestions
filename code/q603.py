list1 = [123, 456, 789]
list2 = [234, 567, 890]
digit_sum_tuples = tuple((x, y, sum(int(digit) for digit in str(x)) + sum(int(digit) for digit in str(y))) for x in list1 for y in list2)
print(list1)
print(list2)
print(digit_sum_tuples)