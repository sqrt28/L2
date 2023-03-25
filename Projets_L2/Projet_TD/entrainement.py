import string
import numpy as np

def verif_maj(phrase):
    lettres_alpha_maj = list(string.ascii_uppercase)
    for i in phrase:
        if i in lettres_alpha_maj:
            return True
    return False
  
  
a = "ici il fAit beau"  
verif_maj(a)

def nbrValeurDict(dico):
    cpt = 0
    for i in dico.values():
        for j in i:
            cpt +=1
    return cpt
    
    
abc = {"j1" : [1,2], "j2" : [2,3,7]}

nbrValeurDict(abc)

l = [0,2,4]
def moyenne_liste(liste):
    somme = 0
    for i in liste:
        somme += i 
    return somme / len(liste)   
print(moyenne_liste(l))




def sayhello(*name):
    print("hello",name)

print(sayhello("sam","ilona"))

print(0.1 + 0.2 == 0.3)
a = (1,2)+(2,4)
print(a)

 




a = np.array([[0,0,0],[0,0,0]])
print(a)

b = np.zeros([3,3])
print(b)

c = np.ones([3,3])
print(c)

d = np.full([3,3,],9)
print(d)

print(d.size)
print(d.shape)
#d.reshape((3,3))
print(type(d))

w = np.arange(0,10,2)
print(w)

z = np.linspace(0,1,5)
print(z)

print(w[w>4])

a = (1,3,4)
print(type(a))
print(a[0]*2)