s = input()
for letter in range(ord("a"), ord("z") + 1):  # ord() gets the ascii value of a char
    letter = chr(letter)  # chr() gets the char of an ascii value
    cnt = s.count(letter)
    if cnt > 0:
        print(f"{letter},{cnt}")
