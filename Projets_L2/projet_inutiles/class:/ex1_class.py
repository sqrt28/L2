class CompteBancaire:
    def __init__(self,numeroCompte : int, nom : str, solde):
        self.numeroCompte = numeroCompte
        self.nom = nom
        self.solde = solde
    
    def Versement(self,argent):
        self.solde += argent
    
    def Retrait(self,argent):
        if self.solde < 0:
            print("Retrait impossible pas assez d'argent")
        self.solde -= argent
    
    def Agios(self):
        self.solde =self.solde*95/100
    
    def afficher(self):
        print("Compte numéro : " , self.numeroCompte)
        print("Nom : ", self.nom)
        print("Solde  : ", self.solde , " Euro ")
        print("Sauf erreur ou omisssion ! ")
        

Compte1 = CompteBancaire(1376, "BARBOSA", 2000)
Compte1.afficher()
Compte1.Versement(1800)
Compte1.Retrait(200)
Compte1.afficher()