class Voiture():
    voitures_crees = 0
    def __init__(self, marque):
        Voiture.voitures_crees += 1
        self.marque = marque





voiture_01 = Voiture("citroen")
voiture_02 = Voiture("renault")
print(Voiture.voitures_crees)
print(voiture_01.marque)