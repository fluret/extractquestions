total = 0
while True:
    s = input().split()
    if not s:  # break if the string is empty
        break
    cm, num = map(
        str, s
    )  # two inputs are distributed in cm and num in string data type

    if cm == "D":
        total += int(num)
    if cm == "W":
        total -= int(num)

print(total)
