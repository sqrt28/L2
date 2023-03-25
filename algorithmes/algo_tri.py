#https://mathematice.fr/fichiers/cpge/infoprepaC24.pdf

import random as rd
import time
import copy
import matplotlib.pyplot as plt

tab_test = [rd.randint(0,20) for i in range(20)]

def tri_par_insertion(tab):
    for tc in range(0,len(tab)-1): #en python de 0,n-1
        temporaire = tab[tc+1]
        p = 0
        while tab[p] < temporaire :
            p += 1
        for i in range(tc,p-1,-1): #pas de -1 pour aller en décroissant
            tab[i+1] = tab[i]
        tab[p] = temporaire
    return tab
tri_par_insertion(tab_test)


def tri_par_permutation(tab):
    for tc in range(2,len(tab)+1):
        for i in range(len(tab),tc-1,-1):
            if tab[i-2] > tab[i-1]:
                a = tab[i-2]
                tab[i-2] = tab[i-1]
                tab[i-1] = a
    return tab
tri_par_permutation(tab_test)


def fusion(g, d):
    i1, i2 = 0, 0
    tableau_fusion = []
    while len(g) > i1 and len(d) > i2: #tant qu'il y a des cases
        if g[i1] < d[i2]:
            tableau_fusion.append(g[i1])
            i1 += 1
        else :
            tableau_fusion.append(d[i2])
            i2 += 1
    while len(g) > i1:
        tableau_fusion.append(g[i1])
        i1 +=1
    while len(d) > i2:
        tableau_fusion.append(d[i2])
        i2 +=1
    return tableau_fusion


def trifusion(tab):
    if len(tab) <= 1 :
        return tab
    r = len(tab) // 2
    tab1 = tab[:r]
    tab2 = tab[r:]
    g = trifusion(tab1) # partie de gauche
    d = trifusion(tab2) # partie de droite
    tableau = fusion(g, d)
    return tableau
trifusion(tab_test)


def partition(tab,g,d):
    pivot = tab[g]
    i=g+1
    j=d
    while i<=j:
        while i<len(tab) and tab[i]<=pivot:
            i=i+1
        while tab[j]>pivot:
            j=j-1
        if i<j:
            tab[i],tab[j] = tab[j],tab[i]
            i=i+1
            j=j-1
    tab[g],tab[j]= tab[j],tab[g]
    return j

def tri_rapide(tab,g,d):
    if g<d:
        j=partition(tab,g,d)
        tri_rapide(tab,g,j-1)
        tri_rapide(tab,j+1,d)
    return tab

print(tri_rapide((tab_test),0,19))

def duree(tab,algo):
    debut = time.time()
    if algo == 1:
        tri_par_insertion(tab)
    elif algo == 2:
        tri_par_permutation(tab)
    fin = time.time()
    return fin - debut
duree(tab_test,2)

"""" afficher une courbe exemple de courbe
x = []
y = []
for i in range(100,1000,10):
    x.append(i)
    y.append(i*i)
fig = plt.figure()
ax = plt.axes()
plt.plot(x,y, "r-", label="y=x^2")
plt.legend(loc="upper left")
plt.xlabel("x")
plt.ylabel("y = x^2")
plt.show()"""

# afficher une courbe
"""x = []
yinsertion = []
ypermutation = []
for i in range(100,1000,10):
    tab = [rd.randint(0,10000)for j in range(i)]
    tabcp = tab.copy()
    x.append(i)
    yinsertion.append(duree(tabcp(1)))
    tabcp = tab.copy()
    ypermutation.append(duree(tabcp,2))
fig = plt.figure()
ax = plt.axes()
plt.plot(x,yinsertion, "r-", label="insertion")
plt.plot(x,ypermutation, "b-", label="permutation")
plt.legend(loc="upper left")
plt.xlabel("Taille des tableaux à trier")
plt.ylabel("Temps en seconde")
plt.show()"""

