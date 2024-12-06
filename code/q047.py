class American:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"{self.name} is an American."


class NewYorker(American):
    def describe(self):
        parent_description = super().describe()
        return f"{parent_description} Specifically, {self.name} is a New Yorker."


# Exemple d'utilisation
anAmerican = American("John")
aNewYorker = NewYorker("Jane")

print(anAmerican.describe())  # Affichera "John is an American."
print(
    aNewYorker.describe()
)  # Affichera "Jane is an American. Specifically, Jane is a New Yorker."
