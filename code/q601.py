list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list3 = [5, 6, 7, 8]
distinct_elements_symmetric_diff = tuple(set(list1) ^ set(list2) ^ set(list3))
print(list1)
print(list2)
print(list3)
print(distinct_elements_symmetric_diff)