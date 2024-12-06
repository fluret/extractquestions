def f(n):
    return n if n <= 1 else f(n - 1) + f(n - 2)


n = int(input("Entrez un nombre : "))
print(f(n))
