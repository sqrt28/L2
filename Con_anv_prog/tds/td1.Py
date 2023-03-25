
#exercice 1:
maListe = [19,5,12,8,3,7,2,15]
taille = len(maListe)
minimum = maListe[0]
maximum = maListe[0]
listePairs = list()
listeImpairs = list()
listeR = list()
somme = 0
i = 0
while i < taille:
    valeur = maListe[i]
    if valeur < minimum:
        minimum = valeur
    if valeur > maximum:
        maximum = valeur
    somme += valeur
    if valeur % 2 == 0:
        listePairs.append(valeur)
    else:
        listeImpairs.append(valeur)
    
    i+=1
        
print("max:",maximum,"min:",minimum)
print("moyenne:",somme/taille)
print(listeImpairs,listePairs)

if len(listePairs) > len(listeImpairs):
    liste_plus_grande = len(listePairs)
else:
    liste_plus_grande = len(listeImpairs)
    
for i in range(liste_plus_grande):
    try:
        listeR.append(listeImpairs[i])
    except:
        pass
    try:
        listeR.append(listePairs[i])
    except:
        pass
print(listeR)

listeR2 = listeR[:]
print(listeR2)
    