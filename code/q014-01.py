word = input()
upper, lower = 0, 0

for i in word:
    if "a" <= i and i <= "z":
        lower += 1
    if "A" <= i and i <= "Z":
        upper += 1

print("Majuscules {0}\nMinuscules {1}".format(upper, lower))
