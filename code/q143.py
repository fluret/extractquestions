list_a = [1, 2, 3,4,5,6,7,8,9]
list_b = [2, 7, 1, 12]

result = [(a, b) for a in list_a for b in list_b if a == b]
print(result)

print([(i,i) for i in list_a if i in list_b])