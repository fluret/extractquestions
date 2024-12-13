string = "Hello, world!"
twice_chars = {char for char in string if string.count(char) == 2}
print(string)
print(twice_chars)