words = ["radar", "hello", "level", "world"]
palindromes = {word for word in words if word == word[::-1]}
print(words)
print(palindromes)