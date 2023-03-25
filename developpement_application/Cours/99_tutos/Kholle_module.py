"""fcts pour la kholle (si besoin)"""
import string

def liste_alphabet(a):
    """créer une liste qui contient les lettres de l'alphabet en minuscule ou majujucle selon la demande"""
    l = []
    if a == "M":
        l = list(string.ascii_uppercase)
    else:
        l = list(string.ascii_lowercase)
    return l

def annee_bix(a):
    """ renvoie  vraie si annee est bix sinon faux """
    if a % 4 == 0 or (a % 100 == 0 and a % 400 == 0) : 
        return True
    else:
        return False

def moy_min_max():
    """renvoie le max, le mix, la somme et la moyenne des nombres rentrés par user"""
    l = list()
    somme = 0
    moyenne = 0
    n = 0
    while n != -1:
        n = int(input("saississez une valeur supérieur à 0 (-1 pour s'arreter) : "))
        if n != -1:
            l.append(n)
            somme += n
    moyenne = somme / len(l)
    return ("le max est", max(l), "le min est", min(l),"la somme est de", somme, "la moyenne est de", moyenne)

