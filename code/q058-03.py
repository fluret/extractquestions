idx = 0


def bs(num, num_list):
    global idx
    if len(num_list) == 1:
        if num_list[0] == num:
            return idx
        else:
            return "No exit in the list"
    elif num in num_list[: len(num_list) // 2]:
        return bs(num, num_list[: len(num_list) // 2])
    else:
        idx += len(num_list) // 2
    return bs(num, num_list[len(num_list) // 2 :])


print(bs(66, [1, 5, 8, 10, 12, 13, 55, 66, 73, 78, 82, 85, 88, 99, 100]))
