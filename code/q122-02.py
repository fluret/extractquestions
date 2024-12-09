lst = [12, 24, 35, 70, 88, 120, 155]
print([i for i in lst if lst.index(i) not in range(2, 5)])
