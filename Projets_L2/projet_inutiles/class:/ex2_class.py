class Calcul:
    def __init__(self,n):
        self.n = n
        
    def factorielle(self):
        pass
    
    def Somme(self):
        somme = 0
        for i in range(self.n+1):
            somme += i
        print(somme)
    
    def tableMult(self):
        l = list()
        for i in range(10):
            l.append(i*self.n)
        print(l)
    
c1 =  Calcul(100)
c1.Somme()       