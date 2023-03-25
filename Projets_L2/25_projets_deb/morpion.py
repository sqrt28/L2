### PROJET MORPION ###

def terminer():
    global arret
    arret = True
    if "_" in jeu_morpion:
        arret = False
    return arret


def ajouter(n, p):
    choix_case = input("quel case " + str(p) + " ?: ")
    jeu_morpion[int(choix_case)] = n
    return afficher()

def afficher():
    print(" " + jeu_morpion[0] + " | " + jeu_morpion[1] + " | " + jeu_morpion[2] + " ")
    print("---+---+---")
    print(" " + jeu_morpion[3] + " | " + jeu_morpion[4] + " | " + jeu_morpion[5] + " ")
    print("---+---+---")
    print(" " + jeu_morpion[6] + " | " + jeu_morpion[7] + " | " + jeu_morpion[8] + " ")


def verif():
    global arret, p1, p2
    for i in range(0, len(jeu_morpion)-2, 3):
        if (jeu_morpion[i] == jeu_morpion[i+1] == jeu_morpion[i+2] != "_"):
            arret = True
            if jeu_morpion[i] == "x":
                dico_score[p1] += 1
            else:
                dico_score[p2] += 1
            return arret, (print("la manche est gagnée pour", jeu_morpion[i]))
    i = 0
    while i < 3:
        if (jeu_morpion[i] == jeu_morpion[i+3] == jeu_morpion[i+6] != "_"):
            arret = True
            if jeu_morpion[i] == "x":
                dico_score[p1] += 1
            else:
                dico_score[p2] += 1
            return arret, (print("la manche est gagnée pour", jeu_morpion[i]))
        i += 1

    if (jeu_morpion[0] == jeu_morpion[4] == jeu_morpion[8] != "_") or (jeu_morpion[2] == jeu_morpion[4] == jeu_morpion[6] != "_"):
        arret = True
        if jeu_morpion[4] == "x":
            dico_score[p1] += 1
        else:
            dico_score[p2] += 1
        return arret, (print("la manche est gagnée pour", jeu_morpion[0] or jeu_morpion[2]))


def play():
    global condition, dico_score, p1, p2, jeu_morpion, arret
    p1 = input("votre prénom joueur 1 (croix) ?")
    p2 = input("votre prénom joueur 2 (rond) ?")
    nb_parties = input("combien de parties vous voulez jouer ?")
    dico_score = {p1: 0, p2: 0}
    condition = False
    for i in range(int(nb_parties)):
        print("nouvelle manche")
        arret = False
        jeu_morpion = ["_", "_", "_",
                       "_", "_", "_",
                       "_", "_", "_"]
        while arret == False:
            if condition == False and arret == False:
                condition = True
                ajouter("x", p1)
                terminer()
                verif()

            elif condition == True and arret == False:
                condition = False
                print(ajouter("o", p2))
                terminer()
                verif()
        print("fin de la manche")
    return (print("fin de la partie"), dico_score)


print(play())
