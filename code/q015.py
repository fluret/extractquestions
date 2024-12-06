a = input("Entrez un chiffre : ")
n1 = int(f"{a}")
n2 = int(f"{a}{a}")
n3 = int(f"{a}{a}{a}")
n4 = int(f"{a}{a}{a}{a}")

print(f"Le résultat de {a} + {a}{a} + {a}{a}{a} + {a}{a}{a}{a} est :")
print(f"{n1 + n2 + n3 + n4:,}".replace(",", " "))