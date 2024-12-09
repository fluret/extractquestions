values = input()
numbers = [str(int(x) ** 2) for x in values.split(",") if int(x) % 2 != 0]
# numbers = [str(int(x) ** 2) for x in values.split(",") if int(x) % 2]
print(",".join(numbers))
