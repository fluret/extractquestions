import re

phrase = input()
pattern = "\d+"
ans = re.findall(pattern, phrase)
print(ans)
