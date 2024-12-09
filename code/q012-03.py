def check(element):
    return all(
        ord(i) % 2 == 0 for i in element
    )  # all returns True if all digits i is even in element


lst = [
    str(i) for i in range(1000, 3001)
]  # creates list of all given numbers with string data type
lst = list(
    filter(check, lst)
)  # filter removes element from list if check condition fails
print(",".join(lst))
