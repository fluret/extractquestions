sentence = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
result = [letter for letter in sentence if letter not in 'a,e,i,o,u, " "']
print(result)

stringex4 = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
print(list(a for a in stringex4 if a not in ("a", "e", "i", "o", "u", " ")))

import string

stringex4 = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams, special characters: * ' and ()/"
print(
    list(
        a
        for a in stringex4
        if a not in ("a", "e", "i", "o", "u", " ")
        and (a in list(string.ascii_lowercase) or a in list(string.ascii_uppercase))
    )
)

sentence = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
consonant_list = [letter for letter in sentence if letter not in 'a, e, i, o, u, " "']
print(consonant_list)

string = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams, special characters: * ' and ()/"
print(
    [
        char
        for char in string
        if ("A" <= char <= "Z" or "a" <= char <= "z") and char not in "aeiouAEIOU"
    ]
)

# I would just propose to transforme the list in a set to have a unique count of each different consonnant :

some_string = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
voyelles = ["a", "e", "i", "o", "u", "y", " "]
consonnant = [c for c in some_string.lower() if c not in voyelles]
print(set(consonnant))

vowels_space = ["a", "e", "i", "o", "u", " "]
sentence = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
my_list = [letter for letter in sentence.lower() if letter not in vowels_space]

sentence = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
consonant = [
    consonant
    for consonant in sentence
    if consonant.lower() not in "aeiou" and consonant != " "
]
print(f"{consonant}")

vowels = "aeıioöuüAEIİOÖUÜ"
text = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
consontants = [i for i in text if i not in vowels]
print(consontants)
