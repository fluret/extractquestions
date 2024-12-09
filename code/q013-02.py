""" Solution by: popomaticbubble
"""

import re

input_string = input("> ")
print()
counter = {
    "Lettres": len(re.findall("[a-zA-Z]", input_string)),
    "Chiffres": len(re.findall("[0-9]", input_string)),
}

print(counter)
