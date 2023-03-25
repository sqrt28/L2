import random as rd
import string

# question1
def genere_nom():
    """focntion qui renvoie 6 lettres au hasard de l'alphabet"""
    mot = string.ascii_lowercase
    a,b,c,d,e,f = rd.randint(0,25), rd.randint(0,25), rd.randint(0,25),rd.randint(0,25), rd.randint(0,25), rd.randint(0,25)
    return mot[a] + mot[b] + mot[c] + mot[d] + mot[e] + mot[f]
    
# question 2
def pokedex1():
    """renvoie un dictionnaire contenant 6 pokemons"""
    global dico_pokedex1
    dico_pokedex1 = {}
    for i in range(6):
        nom_pokemeon = genere_nom()
        dico_pokedex1[nom_pokemeon] = {"atk" : rd.randint(1,10),"def" : rd.randint(1,10)}
    return dico_pokedex1
pokedex1()

def pokedex2():
    global dico_pokedex2
    """renvoie un dictionnaire contenant 6 pokemons"""
    dico_pokedex2 = {}
    for i in range(6):
        nom_pokemeon = genere_nom()
        dico_pokedex2[nom_pokemeon] = {"atk" : rd.randint(1,10),"def" : rd.randint(1,10)}
    return dico_pokedex2
pokedex2()

# question 3
def combat(a1, d1, a2, d2): # prend en etrer deux tuples
    """simule un combat entre pokemon"""
    while d1 >= 0 and d2 >= 0:
        d2 -= a1
    if d2 >= 0:
        d1 -= a2
    print(d2)
    return (a1, d1, a2, d2)

# question 4
def combat_dresseur():
    
    l1 = []
    l2 = []
    a = 0
    b = 1
    #récupère les valeurs "attaque" et "défense"
    for values in dico_pokedex1.values():
        for i in values.values():
            l1.append(i)
    for values in dico_pokedex2.values():
        for j in values.values():
            l2.append(j)
            
    while (len(l1) >= 0) and (len(l2) >= 0):
        combat(l1[a],l1[b],l2[a],l2[b])
        if l1[b] < 0:
            l1.remove[l1[b]]
        if l2[b] < 0:
            l2.remove[l2[b]]
    return l1,l2
    

print(combat_dresseur())



