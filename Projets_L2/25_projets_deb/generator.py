###generator de mdp###

# librairies
import random as rd
import string


l_caractors = list(string.ascii_letters+string.punctuation+string.digits)

# def
def generator(leng):
    l = []
    mdp = ""
    for i in range(leng):
        mdp += rd.choice(l_caractors)
    liste_de_mdp.append(mdp)


# Programme
liste_de_mdp = list()
cb = int(input("nombre de mdp? "))
leng = int(input("longueur du mdp? "))
i = 0

while i != cb:
    generator(leng)
    i += 1

print(liste_de_mdp)
