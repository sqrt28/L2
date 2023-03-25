def deux_fois_somme(n):
    somme = 1
    for i in range(n):
        somme *= 2
    return somme

print(deux_fois_somme(30))