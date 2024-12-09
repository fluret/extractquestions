def is_consonant(consonant):
    vowels = "aeiouAEIOU"
    if consonant not in vowels:
        return True
    else:
        return False
    
print(is_consonant("a"))
print(is_consonant("b"))
print(is_consonant("A"))
print(is_consonant("B")) 