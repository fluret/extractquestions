import string
 
text = "Hello, world! How's everything?"
cleaned_text = {char for char in text if char not in string.punctuation}
print(text)
print(cleaned_text)