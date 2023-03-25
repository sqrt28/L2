#print(type({10,20}))
#print(type((10,20)))
#print(type([10,20]))



#exercice 1

#print(type((10*3)//3))


3* (10/3)
#3*(10//3)
#(3*10)//3


#exercice 2




def zodiac():
    year = int(input("année?"))
    dico =  {0 : "singe",
1 : "coq",
2 : "chien",
3 : "porc",
4 : "rat",
5 : "bœuf",
6 : "tigre",
7 : "lapin",
8 : "dragon",
9 : "serpent",
10 : "cheval",
11 : "mouton"}
    
    print(dico.get(year % 12))

#print(zodiac())


def annee_bix(a):
    if (a % 4 == 0  and a % 100 != 0 or a % 400 == 0):
        return("année bissextile")
    else:
        return("ce n'est pas une année bissextile")

print(annee_bix(1900))


def moyenne_min_max():
    n = int(input("donner nombres"))
    u = 0
    l = []
    for i in range(n):
        a = int(input("donner des nombres faire la moyenne"))
        l.append(a)
        u += a
    print( "la moyenne est ", (u /n),"le min est", min(l),"le max est", max(l))

#moyenne_min_max()

def factorielle(n):
    #n = int(input("donner un chiifre pour calculer la factorielle"))
    i = 1
    res = 1
    while i <= n:
        res = i * res
        i +=1
    return res
  
       

#factorielle(5)

def afficher_etoile(n):
    for i in range(n+1):
        print("*"*i)

#afficher_etoile(5)
import random as rd
def tirage_aleatoire():
    tirage = []
    l = []
    for i in range(99):
        tirage.append(rd.randint(100,200))
    tirage.sort()
    for i in range(99):
        if tirage[i] % 2 == 0:
            l.append(tirage[i])
    for i in range(9):
        print(l[i])
#tirage_aleatoire()

#exercice 4

def mirroir_palyndrome(n):
    l=[]
    i = 0
    res = []
    for i in range(len(n)):
       l.append(n[i])
    for i in range(len(l)):
        res.append(l[-1])
        l.remove(l[-1])
    print( res)
    if l == res:
        print("palindrome")
#mirroir_palyndrome("abcd")

    
def get_mirroir(mot):
    mirroir = ""
    for i in range(len(mot)):
        mirroir = mirroir + mot[len(mot)-1-i]
    return mirroir

#get_mirroir("salut")

def is_palindrome(mot):
    for i in range(len(mot)//2):
        if mot[i] != mot[-i-1]:
           return False
    return True

#is_palindrome("radar")

#nb = int(input("ffff"))
#while (not is_palindrome(str(nb))):
   # nb = nb + int(get_mirroir(str(nb)))
#print(nb)