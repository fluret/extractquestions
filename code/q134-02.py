def synthese_familles(comptes):
    # On commence par créer un dictionnaire pour ranger les résultats
    synthese = dict()

    # On traite chaque compte
    for c in comptes:
        # La méthode dict.get() renvoie une valeur par défaut si la clef demandée n'existe pas. Pratique pour gérer les éléments absents.
        synthese[c["nom"]] = synthese.get(c["nom"], 0) + c.get("epargne", 0)

    # On va récupérer d'un coup le minimum et maximum en passant par les fonctions min() et max()
    # On commence par créer la fonction qui pourra comparer deux familles
    cle_epargne = lambda d: d[1]
    # Une famille étant composé d'un nom et d'un montant, cette fonction ne traite que le montant

    # On peut maintenant demander immédiatement min et le max de la synthèse des familles
    # Chaque famille sera comparée par la fonction cle_epargne qui ne traite que les montants
    # Donc seuls les montants sont pris en compte dans la recherche des min et max
    (pauvre, riche) = min(synthese.items(), key=cle_epargne), max(
        synthese.items(), key=cle_epargne
    )

    # On retourne les informations récupérées
    return (pauvre, riche)


# Test
comptes = [
    {"nom": "Boismoneau", "prenom": "stephane", "epargne": 2500},
    {"nom": "Jambon", "prenom": "fred", "epargne": 5000},
    {"nom": "Durois", "prenom": "nicolas", "epargne": 10000},
    {"nom": "Gueux", "prenom": "phillipe", "epargne": 1250},
    {"nom": "Duchan", "prenom": "alice", "epargne": 4530},
    {"nom": "Lepenou", "prenom": "amed", "epargne": 2200},
    {"nom": "Gueux", "prenom": "bernard"},
    {"nom": "Jambon", "prenom": "steven", "epargne": 1670},
    {"nom": "Gueux", "prenom": "sylvie", "epargne": 3},
    {"nom": "Durois", "prenom": "berbard", "epargne": 300000},
]
print(synthese_familles(comptes))
