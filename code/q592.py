list1 = [1, 2, 3]
list2 = [4, 5, 6]
product_tuples = tuple((x, y, x * y) for x in list1 for y in list2)
print(list1)
print(list2)
print(product_tuples)