class DivisibleBySeven:
    def __init__(self, n):
        self.n = n

    def generator(self):
        for i in range(0, self.n + 1):
            if i % 7 == 0:
                yield i

# Exemple d'utilisation
n = int(input("Entrez la valeur de n : "))
divisible_by_seven = DivisibleBySeven(n)

for number in divisible_by_seven.generator():
    print(number)

