netAmount = 0
while True:
    s = input()
    if not s:
        break
    operation, amount = s.split(" ")
    amount = int(amount)
    if operation == "D":
        netAmount += amount
    elif operation == "W":
        netAmount -= amount
    else:
        pass

print(netAmount)
