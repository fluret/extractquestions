a = input()
total, tmp = 0, str()  # initialing an integer and empty string

for i in range(4):
    tmp += a  # concatenating 'a' to 'tmp'
    total += int(tmp)  # converting string type to integer type

print(total)
