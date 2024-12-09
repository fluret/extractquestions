n = int(input())
f = lambda x: f(x - 1) + 100 if x > 0 else 0
print(f(n))
