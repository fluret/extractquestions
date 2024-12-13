from itertools import chain
 
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
unique_ordered_elements_tuple = tuple(set(chain(list1, list2)))
print(list1)
print(list2)
print(unique_ordered_elements_tuple)