list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = tuple(x for x in list1 if x in list2)
print(list1)
print(list2)
print(common)