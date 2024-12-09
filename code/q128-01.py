import textwrap

string = input()
width = int(input())

print(textwrap.fill(string, width))
