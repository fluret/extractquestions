def check(x):  # converts binary to integer & returns zero if divisible by 5
    total, pw = 0, 1
    reversed(x)

    for i in x:
        total += pw * (ord(i) - 48)  # ord() function returns ASCII value
        pw *= 2
    return total % 5


data = input().split(",")  # inputs taken here and splited in ',' position
lst = []

for i in data:
    if check(i) == 0:  # if zero found it means divisible by zero and added to the list
        lst.append(i)

print(",".join(lst))
