list_a = [1, 2, 3, 4, 3, 4]
list_b = [2, 3, 4, 5, 1]
common = [a for a in list_a if a in list_b]
print(common)

list_a = 1, 2, 3, 4, 3, 4
list_b = 2, 3, 4, 5
my_list = [element_b for element_b in list_b for element_a in list_a if element_b == element_a]
print(my_list)

common_numbers = []
def f(x):
    common_numbers.append(x)
    return x

list_a = 1, 2, 3, 4, 3, 4 
list_b = 2, 3, 4, 5,
my_list = [f(element_b) for element_b in list_b for element_a in list_a if element_b == element_a and element_b not in common_numbers]
print(my_list)

list_a = [1, 2, 3, 4, 3, 4]
list_b = [2, 3, 4, 5, 1]
common = []
[common.append(a) for a in list_a if a in list_b and a not in common]
print(common)