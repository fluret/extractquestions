lst = [str(i) for i in range(1000, 3001)]
lst = list(
    filter(lambda i: all(ord(j) % 2 == 0 for j in i), lst)
)  # using lambda to define function inside filter function
print(",".join(lst))
