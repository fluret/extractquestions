input_str = input()
dimensions = [int(x) for x in input_str.split(',')]
rowNum = dimensions[0]
colNum = dimensions[1]

multilist = [[row * col for col in range(colNum)] for row in range(rowNum)]

print(multilist)
print()
for row in multilist:
    print(' '.join(map(str, row)))
