def sort_tuples(tuples_list):
    # Trier les tuples par nom, puis par âge, puis par taille
    return sorted(tuples_list, key=lambda x:(x[0], int(x[1]), int(x[2])))


# Entrée des tuples par la console
input_data = """Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85"""

# Conversion des données d'entrée en une liste de tuples
tuples_list = [tuple(item.split(',')) for item in input_data.split('\n')]

# Tri des tuples
sorted_tuples = sort_tuples(tuples_list)

# Affichage du résultat
print(sorted_tuples)
