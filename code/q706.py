import string
 
char_alphabet_position = {char: string.ascii_lowercase.index(char) + 1 for char in string.ascii_lowercase}
print(char_alphabet_position)