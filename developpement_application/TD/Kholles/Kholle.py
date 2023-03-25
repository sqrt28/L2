#question1
import string
import random as rd
portefeuille = {}
capital = 100000

#question2
def genere_titre():
    global n
    mot = string.ascii_uppercase
    liste = [char for char in mot]
    a = rd.randint(0,26)
    b = rd.randint(0,26)
    c = rd.randint(0,26)
    return liste[a] + liste[b] + liste[b]
    
#question3
def genere_cours():
    return rd.uniform(0,500)


#question4
def achat(x):
    global somme, capital, dico, n
    dico = {"nombre": 0, "cours": 0}
    somme = 0
    n = genere_titre()
    v = genere_cours()
    if x * v < capital:
        dico["nombre"] += x
        dico["cours"] = v
        somme += (x*v)
        capital -= somme
    return dico

def nombre_actions(a):
    i = 0
    while i < a:
        achat(rd.randint(0,20))
        i+=1
        portefeuille[n] = dico
    return portefeuille

print(nombre_actions(2))
print(capital)

"""#question5
def variation():
    x = rd.uniform(0.5,2)
    for key in portefeuille:
        portefeuille[key] = portefeuille.get(key) * x  # problème dictionnaire dans un dictionnaire
    return portefeuille
variation()"""