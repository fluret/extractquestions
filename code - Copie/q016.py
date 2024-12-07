values = input()
numbers = [str(int(x)**2) for x in values.split(",") if int(x) % 2 != 0]
print(",".join(numbers))
