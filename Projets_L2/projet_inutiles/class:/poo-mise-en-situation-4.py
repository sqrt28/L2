# POO EXERCICE DE MISE EN SITUATION 4

# ---
class Personne:
    def __init__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom)

# ---

nb_personne = 3
noms = []
liste_personne = []
for i in range(nb_personne):
    nom = (input("nom de la personne "+str(i)+": "))
    liste_personne.append(Personne(nom))
    
for personne in liste_personne:
    personne.SePresenter()