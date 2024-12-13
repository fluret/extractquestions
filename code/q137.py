some_string = "the slow solid squid swam sumptuously through the slimy swamp"
spaces = [s for s in some_string if s == " "]
print(len(spaces))

res = sum([1 for x in some_string if x == " "])
