import random as rd

nb_parties = int(input("cb de parties?"))
p_users = 0
p_ordi = 0


def play():
    global p_ordi, p_users
    l = ["ciseaux", "papier", "pierre"]
    n = input("papier? pierre? ciseaux?")
    a = rd.choice(l)
    print("ordi", a)
    print("user", n)
    if n == "papier":
        if a == "pierre":
            print("user a gagné")
            p_users += 1
        if a == "ciseaux":
            print("ordi a gagné")
            p_ordi += 1
        if a == "papier":
            print("égalité")
    if n == "pierre":
        if a == "pierre":
            print("égalité")
        if a == "ciseaux":
            print("user a gagné")
            p_users += 1
        if a == "papier":
            print("ordi a gagné")
            p_ordi += 1
    if n == "ciseaux":
        if a == "pierre":
            print("ordi a gagné")
            p_ordi += 1
        if a == "ciseaux":
            print("égalité")
        if a == "papier":
            print("user a gagné")
            p_users += 1


for i in range(nb_parties):
    play()

if p_ordi > p_users:
    print("La partie de", nb_parties, "manches est terminée", "ordi a gané")
elif p_ordi < p_users:
    print("La partie de", nb_parties, "manches est terminée", "user a gagné")
else:
    print("La partie de", nb_parties, "manches est terminée", "égalité")
