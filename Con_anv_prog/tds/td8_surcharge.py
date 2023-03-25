
#exercice1
print("Exercice1:\n")

class CString(object):
    nombreStr = 0

    def __init__(self, char):
        self.char = char
        self.taille = len(self.char)
        CString.nombreStr += 1

    def get_chaine(self):
        return self.char
    
    def get_taille(self):
        return self.taille
    
    def __add__(self, lettre):
        return (CString(self.char + lettre.char))
    
    
    def __gt__(self,chaine):
        if self.get_chaine() > chaine.get_chaine():
            return self
        else:
            return chaine
        
    def __le__(self,chaine):
        return self.get_chaine() <= chaine.get_chaine()
    
    def __iadd__(self,string):
        self.char += string
        self.taille += len(string)
        return self
    
    def __str__(self):
        return "La chaine de caractères est {0} et est de taille {1}".format(self.get_chaine(),self.get_taille())
        

            
    def nbrChaines():
        return CString.nombreStr
    

s1 = CString("sa")
s2 = CString("m")

s1+s2
s3 = s1<s2
print(s3.get_chaine())
print(s1 <= s2)
s1 += "m"
print(s1.get_chaine())
print(s1)
    
#Exercice2:
print("\nExercice2:\n")

class Vecteur(object):
    def __init__(self,liste_entier : list):
        self.liste_entier = liste_entier
        self.taille = len(liste_entier)
    
    def get_liste(self):
        return self.liste_entier
    
    def get_taille(self):
        return self.taille
    
    def set_liste(self,nvListe : list):
        self.liste_entier = nvListe
        
    def get_val(self,ind : int):
        if ind < self.get_taille():
            return self.liste_entier[ind]
    
    def set_val(self, ind : int, num : int):
        if ind < self.get_taille():
            self.liste_entier[ind] = num
    
    def __add__(self,liste : list):
        return Vecteur(self.get_liste() + liste.get_liste())
       
    
    def __iadd__(self,val : int):
        self.liste_entier += [val]
        return self
    
    def __sub__(self,liste):
        ele = 0
        while len(liste.liste_entier) >= 1:
            if liste.liste_entier[ele] in self.liste_entier:
                self.liste_entier.remove(liste.liste_entier[ele])
            else:
                liste.liste_entier.remove(liste.liste_entier[ele])
        Vecteur(self)
        
    def __isub__(self,val):
        for i in self.liste_entier:
            if i == val:
                self.liste_entier.remove(i)
        return self
        

l1 = Vecteur([1,2,3,4])
l2 = Vecteur([14,3,9,1])
l1 += 3
l1 -= 2
l3 = l1+l2
print(l1.get_liste())


l4 = l2 - l1
print(l4)