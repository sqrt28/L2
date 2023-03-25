# TD3 et TD4 : Fonctions récursives, liste en compréhension, dictionnaires
import random as rd
import string


# Exercice 1 : Les fonctions récursives


def Fibonacci_for(n):
    "suite de fibonacci avec boucle for"
    liste = [0,1]
    for i in range(2,n):
        liste.append((liste[i-1])+(liste[i-2]))
    return liste
(Fibonacci_for(10))

def Fibonacci_while(n):
    "suite de fibonacci avec boucle while"
    assert n > 0 #n doit etre strictement positif
    liste = [0,1]
    i = 2
    while i != n :
        liste.append((liste[i-1])+(liste[i-2]))
        i += 1
    return liste
(Fibonacci_while(2))

def Fibonacci_recursive(n):
    "suite de fibonacci avec recursivitée"
    if n < 0:
        return "n cannot be negative"
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return Fibonacci_recursive(n-1)+ Fibonacci_recursive(n-2)
    
Fibonacci_recursive(6)


def factorielle(n):
    "renvoie la factorielle d'un nombre"
    if n < 0 :
        return "n cannot be negative"
    if (n == 0) :
        return 1
    elif (n == 1) :
        return 1
    else:
        return n * factorielle(n-1) 
    
factorielle(4)

def recursive_PGCD(a, b) :
    "renvoie le plus grand diviseur commun"
    if b == 0:
        return a
    else:
        r = a % b
        return recursive_PGCD(b,r)
            
    
    
recursive_PGCD(15,50)


def pyramide_inverse(n,s):
    if n < 1:
        return None
    for i in range(n):
        print(s, end="")
    print()
    return pyramide_inverse(n-1,s)


def puissance(x,n):
    if n < 2 :
        return x
    return x * puissance(x,n)


def puissance_rapide(x,n):
    "à compléter"
    if n < 2 :
        return x
    if n % 2 == 0:
        return puissance_rapide(x,n/2) * puissance_rapide(x,n)


# Exercice 2 : Dictionnaire

dico = {}
dico["nom"] = "toto"
dico["prénom"] = "titi"
dico["age"] = 20
dico["adresse"] = 404
dico["age"] = 18
dico.pop("age") #supprime
print(dico)
for key in dico:
    if key == "prénom":
        print(" oui prénom")
    if key == "age":
        print("oui age")
dico.keys()
dico.values()
dico.items()

liste1 = [i for i in range(0,11)]
liste2 = [i for i in range(-10,1)]
dico_positif_negatif = {"nombres positifs" : None, "nombres négatifs" :None}
dico_positif_negatif["nombres positifs"] = liste1
dico_positif_negatif["nombres négatifs"] = liste2
print(dico_positif_negatif)

def aleatoire_dico_nombres(n):
    for i in range(n):
        aleatoire = rd.randint(-5,5)
        if aleatoire >= 0:
            dico_positif_negatif["nombres positifs"].append(i)
        elif aleatoire < 0:
            dico_positif_negatif["nombres négatifs"].append(i)
    return dico_positif_negatif
aleatoire_dico_nombres(5)


def carre_cube():
    #dico_positif_negatif["nombres positifs"] = [i**2 for i in range(dico_positif_negatif["nombres positifs"])]
    return dico_positif_negatif
carre_cube()



# liste en comprehension liste = [x for i in range(9)] exemple
#EXERCICE 3

def occurence(chaine):
    dico = dict()
    for char in chaine :
        dico[char] = chaine.count(char)
    
    return dico
occurence("Antanannarivo")

mots = ['eddard', 'catelyn', 'robb', 'sansa', 'arya', 'brandon', 'rickon', 'theon', 'rorbert', 'cersei', 'tywin', 'jaime', 'tyrion', 'shae', 'bronn', 'lancel', 'joffrey', 'sandor', 'varys', 'renly']

def mots_position1(liste, let, pos):
    """return les mots qui ont la lettre let à la position pos dans la liste"""
    liste_mots = []
    for mot in liste:
        if (pos < len(mot)):
            if mot[pos] == let:
                liste_mots.append(mot)
    return liste_mots
mots_position1(mots, "c",0)


def mots_position2(liste, let, pos):
    "meme que mots_position1 mais avec liste en compréhension"
    #new_liste = [ mot for mot in liste ((if pos < len(mot)) and (if mot[pos] == let))]
    #return new_liste
mots_position2(mots,"c",0)

def dictionnaire_new(liste):
    dico = dict()
    for mot in liste:
        i = 0
        for char in mot:
            if (i,char) not in dico:
                dico[(i,char)] = mots_position2(liste, char, i)
            i += 1
    return dico
dictionnaire_new(mots)

def mots_position3(dico, let, pos):
    return dico[(let,pos)]
#mots_position3(dico,"a",2)


#exercice 4

liste_TD = ["a","c","b","e","f","g","h","i","j","k","l","m","n","o","p"]
elements = string.ascii_lowercase[:15]
print(elements)

size_groupe = len(elements) // 5
liste_groupe = []
i = 0
while i + size_groupe <= len(elements):
    liste_groupe.append(elements[i:i+size_groupe])
    i += size_groupe
print(liste_groupe)

# refaire avec un for
liste_groupe2 = []
for i in range(0,len(elements), size_groupe):
    liste_groupe2.append(elements[i:i+size_groupe])
print(liste_groupe2)

"""def create_group(liste):
    size_groupe = len(liste) // 5
    liste_groupe = []
    copie_liste = liste.copy()
    i = 0
    while i + size_groupe <= len(liste):
        sous_groupe = []
        for j in range(size_groupe):
            index_elem = copie_liste.index(rd.choice(copie_liste))
            sous_groupe.append(copie_liste.pop(index_elem))
        liste_groupe.append(sous_groupe)
        i += size_groupe
    return liste_groupe"""
        
#create_group(elements)
dico_groupes_eleves = {}
i = 0
j = 1
#rd.shuffle(elements)
while i + size_groupe <= len(elements):
    dico_groupes_eleves["Groupe"+ str(j)] = elements[i:i+size_groupe]
    i += size_groupe
    j += 1



size_groupe = len(elements) // 5
listes_notes = []
for index in range(len(elements)):
    listes_notes.append(rd.randint(20))

dico_notes_eleves = {}
i = 0
j = 1
#rd.shuffle(elements)
while i + size_groupe <= len(elements):
    dico_notes_eleves["Groupe"+ str(j)] = elements[i:i+size_groupe]
    i += size_groupe
    j += 1



print("dico_groupes_eleves", dico_groupes_eleves)
print("notes_eleves", dico_notes_eleves)
