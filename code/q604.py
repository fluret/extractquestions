strings = ["apple", "Banana", "Cherry"]
distinct_case_insensitive_chars = tuple(set(char.lower() for string in strings for char in string))
print(strings)
print(distinct_case_insensitive_chars)