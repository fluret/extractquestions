list1 = [123, 456, 789]
list2 = [234, 567, 890]
digit_sum_tuples = tuple(set((x, y, sum(divmod(x, 10)) + sum(divmod(y, 10))) for x in list1 for y in list2))
print(list1)
print(list2)
print(digit_sum_tuples)