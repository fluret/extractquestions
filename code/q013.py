word = input()
letter, digit = 0, 0

for i in word:
    if ("a" <= i and i <= "z") or ("A" <= i and i <= "Z"):
        letter += 1
    if "0" <= i and i <= "9":
        digit += 1

print("Lettres {0}\nChiffres {1}".format(letter, digit))
