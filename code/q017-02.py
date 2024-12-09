solde = 0
while True:
    action = input("Dépôt/Retrait/Solde/Quitter? D/R/S/Q: ").lower()
    if action == "d":
        depot = input("Combien souhaitez vous déposer ? ")
        solde = solde + int(depot)
    elif action == "r":
        retrait = input("Combien souhaitez vous retirer ? ")
        solde = solde - int(retrait)
    elif action == "s":
        print(solde)
    else:
        quit()