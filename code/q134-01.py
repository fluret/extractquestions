def synthese_familles(**kwargs):
    # On commence par créer un dictionnaire pour ranger les résultats
    synthese = {}
    clients = kwargs.values()
    # On traite chaque compte
    for c in clients:
        # Si le nom de famille n'a pas encore été trouvé
        if c["nom"] not in synthese:
            # On le crée dans le dictionnaire des résultats
            synthese[c["nom"]] = 0

        # Si l'épargne est présente dans le compte...
        if "epargne" in c:
            # On peut alors la rajouter au résultat
            synthese[c["nom"]] += c["epargne"]
    # for

    # Il faut maintenant trouver le plus pauvre et le plus riche
    (pauvre, riche) = (None, None)
    for famille, epargne in synthese.items():
        if pauvre is None or epargne < pauvre[1]:
            pauvre = (famille, epargne)
        if riche is None or epargne > riche[1]:
            riche = (famille, epargne)
    # for

    # On retourne les informations récupérées
    return (pauvre, riche)


# Test de la fonction
comptes = {
    "compte1": {"nom": "Boismoneau", "prenom": "stephane", "epargne": 2500},
    "compte2": {"nom": "Jambon", "prenom": "fred", "epargne": 5000},
    "compte3": {"nom": "Durois", "prenom": "nicolas", "epargne": 10000},
    "compte4": {"nom": "Gueux", "prenom": "phillipe", "epargne": 1250},
    "compte5": {"nom": "Duchan", "prenom": "alice", "epargne": 4530},
    "compte6": {"nom": "Lepenou", "prenom": "amed", "epargne": 2200},
    "compte7": {"nom": "Gueux", "prenom": "bernard"},
    "compte8": {"nom": "Jambon", "prenom": "steven", "epargne": 1670},
    "compte9": {"nom": "Gueux", "prenom": "sylvie", "epargne": 3},
    "compte10": {"nom": "Durois", "prenom": "berbard", "epargne": 300000},
}
print(synthese_familles(**comptes))
