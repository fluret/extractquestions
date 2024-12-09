phrase = input().split()
ans = [word for word in phrase if word.isdigit()]  # using list comprehension method
print(ans)
