s = input()
d = {"Chiffres": 0, "Lettres": 0}
for c in s:
    if c.isdigit():
        d["Chiffres"] += 1
    elif c.isalpha():
        d["Lettres"] += 1
    else:
        pass

print("Lettres", d["Lettres"])
print("Chiffres", d["Chiffres"])
