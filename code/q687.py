text = "Hello123"
ascii_values = {char: ord(char) for char in text if char.isalpha()}
print(text)
print(ascii_values)