###Class###

class EtreVivant:
    ESPECE_ETRE_VIVANT =  "etre vivant non identifié"
    
    def AfficherInfosEtreVivant(self):
        print("info etre vivant : " + Personne.ESPECE_ETRE_VIVANT)

class Chat(EtreVivant):
    ESPECE_ETRE_VIVANT =  "Chat (Mammifère félin)"
    
    def AfficherInfosEtreVivant(self):
        print("info etre vivant : " + Personne.ESPECE_ETRE_VIVANT)

class Personne(EtreVivant):
    ESPECE_ETRE_VIVANT = "Humain (Mamifèree homo sapiens"
    def __init__(self, nom : str = "", age : int = 0):
        self.nom = nom
        self.age = age
        if  self.nom == "":
            self.DemandeNom()
        print("constructeur personne" + self.nom)
        
    def SePresenter(self):
        info_personne = "Bonjour je m'appelle " + self.nom
        if self.age != 0:
            info_personne += ", j'ai " + str(self.age) + " ans"
        print(info_personne)
        
        if self.age != 0:
            if self.EstMajeur():
                print("Je suis majeur")
            else:
                print("Je suis mineur")  
        
    def EstMajeur(self):
        return self.age >= 18
    
    def DemandeNom(self):
        self.nom = input("nom de la personne: ")
        

class Etudiant(Personne):
    def __init__(self, nom : str, age : int, etude : str):
        super().__init__(nom,age)
        self.etude = etude
    
    def SePresenter(self):
        super().SePresenter()
        print("Je suis étudiant en " + self.etude)
        
#personne1 = Personne("Jean",20)
#personne2 = Personne("Paul",15)
#personne3 = Personne()
#personne1.SePresenter()
#personne2.SePresenter()
#personne3.SePresenter()

liste_personnes = [Personne("Jean",20),
                   Personne("Paul",15),
                   Personne("Zoe",39)]

for personne in liste_personnes:
    personne.SePresenter()
    personne.AfficherInfosEtreVivant()


etudiant1 = Etudiant("sam",19,"informatique")
etudiant1.SePresenter()