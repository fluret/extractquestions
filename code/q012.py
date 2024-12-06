values = []
test = False
for i in range(1000, 3001):
    s = str(i)
    test = int(s[0]) % 2 == 0 and int(s[1]) % 2 == 0
    test = test and int(s[2]) % 2 == 0 and int(s[3]) % 2 == 0
    if test:
        values.append(s)
print(",".join(values))