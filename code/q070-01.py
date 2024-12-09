class Personne(object):
    def __init__(self):
        self.genre = "unknown"

    def getGenre(self):
        print(self.genre)


class Homme(Personne):
    def __init__(self):
        self.genre = "Homme"


class Femme(Personne):
    def __init__(self):
        self.genre = "Femme"


sharon = Femme()
doug = Homme()
sharon.getGenre()
doug.getGenre()
