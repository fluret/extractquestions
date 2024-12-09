def generate(n):
    for i in range(n + 1):
        if (
            i % 35 == 0
        ):  # 5*7 = 35, if a number is divisible by a & b then it is also divisible by a*b
            yield i


n = int(input())
resp = [str(i) for i in generate(n)]
print(",".join(resp))
