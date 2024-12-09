def is_vowel(vowel):
    vowels = "aeiouAEIOU"
    if vowel in vowels:
        return True
    else:
        return False


print(is_vowel("a"))
print(is_vowel("b"))
print(is_vowel("A"))
print(is_vowel("B"))
