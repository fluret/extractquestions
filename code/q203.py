def cap_if_consonant(x):
    vowels = "aeiouAEIOU"
    for letter in vowels:
        if x[0] in vowels:
            return x
        else:
            return x.capitalize()


print(cap_if_consonant("great job!"))
