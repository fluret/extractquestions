sentence = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
words = sentence.split()
result = [number for number in words if not number.isalpha() ]
print(result)

sentence = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
words = sentence.split()
result = [number for number in words if number.isnumeric()]
print(result)

state = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
st_list = [word for word in state.split() if word.isdigit()]
print(st_list)

import re

[i for i in "In 1984 there were 13 instances of a protest with over 1000 people attending".split() if re.match("[0-9]", i)]



import re

sentence = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
w_in_sentence = sentence.split()

pattern = r'[0-9]'

print([n for n in sentence if re.match(pattern, n)])

