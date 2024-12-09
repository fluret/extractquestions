import itertools

string = input("> ")
width_length = int(input("What is the width of the groupings? "))


def grouper(string, width):
    iters = [iter(string)] * width
    return itertools.zip_longest(*iters, fillvalue="")


def displayer(groups):
    for x in groups:
        if x == "":
            continue
        else:
            print("".join(x))


displayer(grouper(string, width_length))
