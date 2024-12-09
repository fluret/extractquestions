def user_input():
    while True:
        s = input()
        if not s:
            return
        yield s


for line in map(str.upper, user_input()):
    print(line)
