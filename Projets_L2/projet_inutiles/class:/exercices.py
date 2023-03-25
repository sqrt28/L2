import time

class Date:
    l_mois = ["janvier", "février", "mars", "avril", "mai", "juin",
              "juillet", "aout", "septembre", "octobre", "novembre", "decembre"]

    def __init__(self, jour: int, mois: int, annee: int):
        if 1 <= jour <= 31:
            self.jour = jour
        else:
            raise ValueError('Le jour doit être compris entre 1 et 31')
        if 1 <= mois <= 12:
            self.mois = mois
        else:
            raise ValueError('Le mois doit être compris entre 1 et 12')
        if annee > 1980:
            self.annee = annee
        else:
            raise ValueError("L'année doit être supérieure ou égale à 1980")

    def afficher(self):
        date = (self.jour, self.mois, self.annee)
        print(str(date[0]), str(Date.l_mois[self.mois]), str(self.annee))

    def __lt__(self, d):
        if self.annee < d.annee:
            return True
        elif self.annee > d.annee:
            return False
        else:
            if self.mois < d.mois:
                return True
            elif self.mois > d.mois:
                return False
            else:
                return self.jour < d.jour


#d1 = Date(30, 3, 2020)
#d2 = Date(11, 3, 2020)
#d1.afficher()
#d2.afficher()


class Chrono:
    def __init__(self):
        self.temps = 0
        self.temps_0 = time.time()
    
    def afficher(self):
        self.actualiser()
        print(str(self.temps), "s")

    def actualiser(self):
        self.temps += time.time() - self.temps_0

#c = Chrono()
#c.afficher()


class Personne:
    def __init__(self, age, taille, poids):
        self.age = age
        self.taille = taille
        self.poids = poids
        
    def imc(self):
        self._imc = (self.poids) / (self.taille ** 2)
        return self._imc
    
    def interprete(self):
        self.imc()
        if self._imc <= 18.5:
            print('imc de', self._imc, " insuffisance pondérale")
        elif self._imc  >= 30:
            print('imc de',self._imc, " obésité")
        else:
            print('imc de', self._imc, "ni obèse, ni maigre")
            
p1 = Personne(18,1.89,70)
p1.interprete()
        