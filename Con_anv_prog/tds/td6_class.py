# exercice 1
print("Exercice1\n")


class Domino(object):
    def __init__(self, faceA, faceB):
        self.faceA = faceA
        self.faceB = faceB

    def affiche_points(self):
        #print("faceA =", self.faceA,"faceB =",self.faceB)
        print("faceA : {0} faceB : {1}".format(self.faceA, self.faceB))

    def valeur(self):
        return self.faceA + self.faceB


obj1 = Domino(1, 2)
obj1.affiche_points()
obj1.valeur()

liste_dominos = list()
for indice in range(7):
    liste_dominos.append(Domino(6, indice))

somme = 0
for indice in liste_dominos:
    indice.affiche_points()
    somme += indice.valeur()
print(somme)


# exercice 2
print("Exercice2\n")


class CompteBancaire(object):
    def __init__(self, nom="Dupont", solde=1000):
        self.nom = nom
        self.solde = solde

    def depot(self, somme):
        self.solde += somme

    def retrait(self, somme):
        self.solde -= somme

    def affiche(self):
        print("Le solde de {0} est de {1}".format(self.nom, self.solde))


compte1 = CompteBancaire()
compte2 = CompteBancaire("sam", 2000)


compte1.depot(200)
compte2.depot(25)
compte2.retrait(300)

compte1.affiche()
compte2.affiche()

# Exercice 3
print("Exercice3\n")


class Voiture(object):
    def __init__(self, marque="Ford", couleur="rouge"):
        self.marque = marque
        self.couleur = couleur
        self.pilote = "personne"
        self.vitesse = 0

    def choix_conducteur(self, nom):
        self.pilote = nom

    def accelerer(self, taux, duree):
        if self.pilote != "personne":
            self.vitesse += taux * duree
        else:
            print("Cette voiture n'a pas de pilote")

    def affiche_tout(self):
        print("Cette {0} de couleur {1} est piloté par {2}, vitesse = {3} m/s".format(
            self.marque, self.couleur, self.pilote, self.vitesse))


auto1 = Voiture("Peugeot", "bleu")
auto2 = Voiture(couleur="verte")
auto3 = Voiture("Mercedes")

auto1.choix_conducteur("Roméo")
auto2.choix_conducteur("Juliette")

auto2.accelerer(1.8, 12)
auto3.accelerer(1.9, 11)

auto2.affiche_tout()
auto3.affiche_tout()
