def is_two(x):
    if x == 2 or x == "2":
        return True
    else:
        return False


print(is_two(2))
print(is_two("2"))
print(is_two(3))
print(is_two("3"))
