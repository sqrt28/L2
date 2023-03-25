
import random as rd
cartes = ["As","2","3","4","5","6","7","8","9","10", "Valet", "Dame" ,"Roi"]
couleur = ["Coeur", "Carreau", "Pique", "Trefle"]


def jeu_cartes(cartes,couleur):
    global jeu_de_cartes
    jeu_de_cartes = []
    for i  in range(13):
        for j in range(4):
            jeu_de_cartes.append(cartes[i] + " " + couleur[j])
    return jeu_de_cartes
jeu_cartes(cartes, couleur)

def Tirage_Cartes(liste):
    global l10
    l10 = []
    for i in range(10):
        l10.append(rd.choice(liste))
    return l10
Tirage_Cartes(jeu_de_cartes)

def Dico1_Cartes(cartes, couleurs, jeu, tirage):
    global dico1
    dico1 = {"cartes" : cartes, "couleurs" : couleurs, "jeu" : jeu, "tirage" : tirage}
    return dico1
Dico1_Cartes(cartes,couleur,jeu_de_cartes,l10)

def Dico2_Cartes(dico):
    liste_cartes = [rd.choice(dico)for i in range(10)]
    dico1["tirage2"] = liste_cartes
    return dico1


def Test_Tirage(dico):
    pass

    