import re
class Utilisateur:
    rx = re.compile(r'^(?=.*[A-Z].*[A-Z])(?=.*[!@#$&amp;*])(?=.*[0-9].*[0-9])(?=.*[a-z].*[a-z].*[a-z]).{8}$')
    def __init__(self, identifiant, mdp):
        self.identifiant = identifiant
        self.mdp = mdp
        self.prenom = ""
        self.nom = ""
        self.email = ""
    
    def est_valide(self, mdp):
        return True if Utilisateur.rx.match(mdp) else False

    def get_mdp(self):
        return self.__mdp

    def motdepass(self):
        if self.est_valide():
            self.__mdp = self.mdp
            return True
        else:
            return False
            