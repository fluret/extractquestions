values = []

for i in range(1000, 3001):
    s = str(i)
    if all(int(digit) % 2 == 0 for digit in s):
        values.append(s)

print(",".join(values))
