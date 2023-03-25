import random as rd


def devine():
    global deviner, ordi, user,v1,v2
    l = [0,100]
    if ordi > deviner:
        l[1] = ordi
        ordi = rd.randint(l[0],l[1])
    elif ordi < deviner:
        l[0] = ordi
        ordi = rd.randint(l[0],l[1])
    if user > deviner:
        print("it's less")
        user = int(input("choice a number "))
    elif user < deviner:
        print("it's more")
        user = int(input("choice a number "))
    return ordi, user


def play():
    global deviner, ordi, user, v1, v2
    parties = int(input("How many rounds do you want play?"))
    for partie in range(parties):
        deviner = rd.randint(0, 100)
        ordi = rd.randint(0, 100)
        user = int(input("choice a number "))
        v1 = 0
        v2 = 0
        while ordi != deviner and user != deviner:
            devine()
            if ordi == deviner:
                print("computer you win",deviner)
            elif user == deviner:
                print("user you win",deviner)
play()
