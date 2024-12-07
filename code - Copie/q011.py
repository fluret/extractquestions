value = []
items = [x for x in input().split(',')]
for p in items:
    intp = int(p, 2)
    print(intp)
    if not intp % 5:
        value.append(p)

print(','.join(value))
