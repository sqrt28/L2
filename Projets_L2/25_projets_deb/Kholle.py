from getpass import getpass


def enregistrer_joueurs():
    global nom1, nom2
    nom1 = input("nom joeur1?")
    nom2 = input("nom joeur2?")
    joueurs = (nom1, nom2)
    return joueurs


def proposition_mot(joueurs, tour):
    if tour % 2 == 0:
        print(joueurs[0])
        mot = getpass("entrez un mot à deviner")
    else:
        print(joueurs[1])
        mot = getpass("entrez un mot à deviner")
    return mot


def lancer_jeu():
    joueurs = enregistrer_joueurs()
    score_j1 = 0
    score_j2 = 0
    nb_parties = input("nb de parties ?")

    for i in range(int(nb_parties)):
        global mot_dev
        mot = proposition_mot(joueurs, i)
        mot_dev = ["_" for i in range(0, len(mot))]
        vies = 10
        if i % 2 == 0:
            print(joueurs[1], "à vous de deviner")
        else:
            print(joueurs[0], "à vous de deviner")

        while 1:
            lettre = input("lettre?")
            print(mise_a_jour(mot, lettre))
            if c == False:
                vies -= 1
            if fin_jeu(mot, vies) == 1:
                print("il vous reste", vies, "vies")
            elif fin_jeu(mot, vies) == 2:
                print("vous avez perdu la manche")
                if i % 2 == 0:
                    score_j1 += 1
                else:
                    score_j2 += 1
                break
            elif fin_jeu(mot, vies) == 0:
                if i % 2 == 0:
                    score_j2 += 1
                else:
                    score_j1 += 1
                print("vous avez gagné la manche")
                break

    if score_j1 > score_j2:
        print(joueurs[0], "a gagné la partie")
    elif score_j1 < score_j2:
        print(joueurs[1], "à gagné la partie")
    elif score_j1 == score_j2:
        print("égalitée")
    print(joueurs[0], score_j1, joueurs[1], score_j2)


def mise_a_jour(mot, lettre):
    global c
    c = False
    for i in range(len(mot)):
        if lettre == mot[i]:
            mot_dev[i] = lettre
            c = True
    return mot_dev


def fin_jeu(mot, vies):
    verif = ""
    for i in mot_dev:
        verif += i
    if mot == verif:
        return 0
    else:
        if vies != 0:
            return 1
        else:
            return 2


lancer_jeu()
