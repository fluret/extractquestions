n = int(input())
f = lambda x: 0 if x == 0 else 1 if x == 1 else f(x - 1) + f(x - 2)
print(",".join([str(f(x)) for x in range(0, n + 1)]))
