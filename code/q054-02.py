def fibo(n):
    if n < 2:
        return n
    return fibo(n - 1) + fibo(n - 2)


def print_fiblist(n):
    fib_list = [(str(fibo(i))) for i in range(0, n + 1)]
    return print(",".join(fib_list))


n = int(input())
print_fiblist(n)
