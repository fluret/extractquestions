from textwrap import wrap

x = str(input(": "))
w = int(input())
z = list(wrap(x, w))
for i in z:
    print(i)
