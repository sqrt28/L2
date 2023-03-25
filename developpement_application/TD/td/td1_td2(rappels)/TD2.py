#TD2 : RAPPEL DES FONCTIONS ET LISTES
import random as rd

#EXERCICE 1
def annee_bix(a):
    "détermine si l'année est bissextile ou pas"
    if (a % 4 == 0  and a % 100 != 0 or a % 400 == 0):
        return True
    else:
        return False
annee_bix(1900)

def nbre_days_months(m,a):
    "Donne le nombre de jours dans un mois pour une année précis"
    mois = {1 : "31 jours", 2 : "28 jours", 3 : "31 jours", 4 :"30 jours", 5 : "31 jours",6 : "30 jours", 7 : "31 jours", 8 : "31 jours", 9 :"30 jours", 10:"31 jours",11:"30 jours",12:"31 jours"}
    if m == 2:
        if annee_bix(a):
            return "29 jours"
    return mois[m]
nbre_days_months(2,2004)

def nbjours_correction(m,a):
    if m == 4 or m == 6 or m ==11:
        return(30)
    elif m != 2:
        return (31)
    if annee_bix(a):
        return (29)
    else:
        return (28)
nbjours_correction(2,2004)

def date_valide(j,m,a):
    "vérifie si la date est valide ou pas"
    l = [31,28,31,30,31,30,31,31,30,31,30,31]
    if j <= l[m-1]:
        if m == 2 and (a % 4 == 0  and a % 100 != 0 or a % 400 == 0):
            if j <=29:
                return True
            else:
                return False
        return True
    else:
        return False
date_valide(29, 2, 1900)

#EXERCICE 2
def liste_moyenne_min_max():
    global l
    l = []
    for i in range(10):
        l.append(rd.randint(10,100))
    return l,max(l), min(l), sum(l)/ len(l)    
liste_moyenne_min_max()

def paire_impaire():
    global l
    paire = []
    impaire = []

    for i in range(len(l)-1):
        if l[i] % 2 == 0 :
            paire.append(l[i])
        else:
            impaire.append(l[i])
    return paire, impaire
paire_impaire()

def trier():
    global l
    l.sort()

def inverser():
    global l
    l.reverse()

def jeu_de_carte():
    "jeu de carte"
    global l_jeu
    l_jeu = []
    for i in range(1,53):
        l_jeu.append(i)
    return  l_jeu
jeu_de_carte()

def coupe_de_jeu():
    " coupe le jeu de carte en deux"
    global l_jeu
    n = rd.randint(1,53)
    l_jeu_coupé = []
    for i in range(n,52):
        l_jeu_coupé.append(l_jeu[i])
    for i in range(0,n):
        l_jeu_coupé.append(l_jeu[i])
    #for i in range(52-n):
        #l_jeu_coupé.append(l_jeu[i])  
    return n, l_jeu_coupé
coupe_de_jeu()

def coupe_correction(cartes,i):
    return cartes[i-1:] + cartes[:i-1]
coupe_correction(l_jeu,8)
        
#EXERCICE 3
def moyenne_eleves(epreuves, etudiants):
    "moyenne des notes des élèves pour un nombre d'épreuves données"
    l_epreuves = []
    l_moyenne = []
    for i in range(epreuves):
        l_epreuves.append([])
        for j in range(etudiants):
            l_epreuves[i].append(rd.randint(0,20))
    for i in range(epreuves):
        l_moyenne.append(sum(l_epreuves[i])/len(l_epreuves[i]))
    return l_moyenne
moyenne_eleves(10,10)

def calcul_notes(nb_epreuves,nb_etudiants):
    moyenne_notes = []
    for epreuve in range(nb_epreuves):
        notes_epreuve = []
        for etudiant in range(nb_etudiants):
            notes_epreuve.append(rd.randint(0,20))
    moyenne_notes.append(sum(notes_epreuve)/len(notes_epreuve))
    return moyenne_notes
print(calcul_notes(10,10))

#EXERCICE 4
def nombre_premiers(n):
    "crible d'érastosthène (nombres premiers)"
    crible = [True] * n
    crible[0] = False
    for i in range(2,n):
        if(crible[i]):
            for j in range(i+1, n):
                if(j%i == 0):
                    crible[j] = False
    for i in range(n):
        if (crible[i]):
            print(i)

nombre_premiers(100)

#print(crible(100))
    
#EXERCICE 5
carre_mag = [[1, 8, 11, 14], [15, 10, 5, 4], [6, 3, 16, 9], [12, 13, 2, 7]]
carre_pas_mag = [[10, 8, 11, 14], [15, 10, 5, 4], [6, 3, 16, 9], [12, 13, 2, 7]]

def ecrire_as_carre(l_carre):
    "écrit le carré magique!!"
    return( l_carre[0],"\n",l_carre[1], "\n",l_carre[2],"\n",l_carre[3])
ecrire_as_carre(carre_mag)

def carre_affiche(carre):
    for i in range(len(carre)):
        for j in range(len(carre)):
            print(carre[i][j], end= "\n")
    print()
carre_affiche(carre_mag)

def test_lignes_carre(a):
    return True if sum(a[0]) == sum(a[1]) == sum(a[2]) == sum(a[3]) else False

def test_colonnes_carre(a):
    return True if ((a[0][0] + a[1][0] + a[2][0] + a[3][0])==(a[0][1] + a[1][1] + a[2][1] + a[3][1])==(a[0][2] + a[1][2] + a[2][2] + a[3][2])==(a[0][3] + a[1][3] + a[2][3] + a[3][3])) else False

def test_diago_carre(a):
    return True if ((a[0][0] + a[1][1] + a[2][2] + a[3][3])==(a[3][0] + a[2][1] + a[1][2] + a[0][3])) else False

def verify_carre_magique(a):
    "vérifie si le carré est magique"
    return True if (test_lignes_carre(a) and test_colonnes_carre(a) and test_diago_carre(a)) else False
    # if faut  comparer la somme ligne colonne et diago
print(verify_carre_magique(carre_pas_mag))



