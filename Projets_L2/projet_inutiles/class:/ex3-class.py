class Rectangle:
    def __init__(self,longueur,largeur):
        self.longueur = longueur
        self.largeur = largeur
    
    def perimetre(self):
        perimetre = 2*(self.longueur + self.largeur)
        print("Le périmètre du rectangle est de",perimetre,"cm")
        
    def surface(self):
        surface = self.longueur * self.largeur
        print("La surface est de", surface, "cm¨2")
        


class Parallelepipede(Rectangle):
    def __init__(self,longueur,largeur,hauteur):
        super().__init__(longueur,largeur)
        self.hauteur = hauteur
    
    def volume(self):
        volume = self.longueur * self.largeur * self.hauteur
        print("Le volume est de", volume)
        
        
rectangle1 = Rectangle(5,4)
parallelepipede1 = Parallelepipede(6,5,3)

rectangle1.perimetre()