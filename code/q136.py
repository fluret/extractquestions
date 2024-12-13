three = [n for n in range(0,1000) if '3' in str(n)]
print(three)

x = [i for i in range(1, 1001) if str(i).find("3") != -1]
y = [i for i in range(1, 1001) if str(i).count("3") > 0]
z = [i for i in range(1, 1001) if '3' in str(i)]

print("x ->", x, len(x), "\n")
print("y ->", y, len(y), "\n")
print("z ->", z, len(z))