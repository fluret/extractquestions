s = "abcdefgabc"
for i in sorted(set(s)):
    print(f"{i}, {s.count(i)}")
