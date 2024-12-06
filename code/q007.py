input_str = input()
rowNum, colNum = [int(x) for x in input_str.split(',')]

multilist = []

for row in range(rowNum):
    row_list = []
    for col in range(colNum):
        row_list.append(row * col)
    multilist.append(row_list)

print(multilist)
print()
for row in multilist:
    print(' '.join(map(str, row)))
