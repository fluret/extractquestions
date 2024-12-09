import textwrap

string = input("")
print("\n".join(textwrap.wrap(string, width=int(input("")))))
