string = "Hello, world!"
non_whitespace_chars = {char for char in string if not char.isspace()}
print(string)
print(non_whitespace_chars)