class Personne(object):
    def getGenre(self):
        return "Unknown"


class Homme(Personne):
    def getGenre(self):
        return "Homme"


class Femme(Personne):
    def getGenre(self):
        return "Femme"


aHomme = Homme()
aFemme = Femme()
print(aHomme.getGenre())
print(aFemme.getGenre())
