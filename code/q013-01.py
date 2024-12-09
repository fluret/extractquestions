word = input()
letter, digit = 0, 0

for i in word:
    if i.isalpha():  # returns True if alphabet
        letter += 1
    elif i.isnumeric():  # returns True if numeric
        digit += 1
print(
    f"Lettres {letter}\nChiffres {digit}"
)  # two different types of formating method is shown in both solution
