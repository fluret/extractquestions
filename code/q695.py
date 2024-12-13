text = "hello world"
char_counts = {char: text.count(char) for char in set(text) if not char.isspace()}
print(text)
print(char_counts)