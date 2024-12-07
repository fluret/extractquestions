s = input()
d = {"Majuscules": 0, "Minuscules": 0}
for c in s:
    if c.isupper():
        d["Majuscules"] += 1
    elif c.islower():
        d["Minuscules"] += 1
    else:
        pass

print("Majuscules", d["Majuscules"])
print("Minuscules", d["Minuscules"])
