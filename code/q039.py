tp = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
li = []
for i in tp:
    if i % 2 == 0:
        li.append(i)

tp2 = tuple(li)
print(tp2)
