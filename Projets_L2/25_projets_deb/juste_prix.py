###JUSTE PRIX###

import random as rd 

nb_parties = int(input("combien de parties"))
dico = {"joueur" : 0, "ordi" : 0}

for i in range(nb_parties):
    nb_deviner = rd.randint(0,100)
    nb_essaies = 10
    while nb_essaies > 0:
        n = int(input("quel nombre ?"))
        if n > nb_deviner:
            print("c'est moins")
        elif n < nb_deviner:
            print("c'est plus")
        else:
            print("Vous avez gagné")
            dico["joueur"] += 1
            break
        nb_essaies -= 1
        print("il vous reste",nb_essaies,"essaies")
    if nb_essaies < 0:
        print("vous avez perdu")
        dico["ordi"] += 1
print(dico)    
    

