text = "hello world"
char_frequency = {char: text.count(char) for char in set(text)}
print(text)
print(char_frequency)