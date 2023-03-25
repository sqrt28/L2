# pendu

mot = "hello"
vies = 10
t = ["_" for i in range(len(mot))]


def play():
    global t
    n = input("lettre?")
    for i in range(len(mot)):
        if mot[i] == n:
            t[i] = n
    return t


def verif():
    for i in range(len(mot)):
        if t[i] != mot[i]:
            return False
    return True


while vies != 0:
    print(play())
    if verif() is True:
        print("bravo")
        break
    vies -= 1
    print("il reste", vies)
