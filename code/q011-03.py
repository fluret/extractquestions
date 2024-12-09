data = input().split(",")
data = list(
    filter(lambda i: int(i, 2) % 5 == 0, data)
)  # lambda is an operator that helps to write function of one line
print(",".join(data))
