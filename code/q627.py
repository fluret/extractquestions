string = "Hello, world!"
non_alphanumeric = {char for char in string if not char.isalnum()}
print(string)
print(non_alphanumeric)