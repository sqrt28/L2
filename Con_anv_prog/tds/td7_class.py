import math
# Exercice 1
print("\nExercice1:\n")


class Point(object):
    def __init__(self, abscisse, ordonne):
        self._abscisse = abscisse
        self._ordonne = ordonne

    def get_abscisse(self):
        return self._abscisse

    def get_ordonne(self):
        return self._ordonne

    def set_abscisse(self, value):
        self._abscisse = value

    def set_ordonne(self, value):
        self._ordonne = value

    def cloner(pt):
        point = Point(pt.get_abscisse(), pt.get_ordonne())
        return point

    def afficher(self):
        print("Point: {0},{1}".format(self._abscisse, self._ordonne))


p1 = Point(50, 100)
p2 = Point(55, 20)
p1.afficher()
Point.cloner(p1).afficher()


# Exercice 2
print("\nExercice2:\n")


class Segment(Point):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def estVerticale(self):
        return self.p1.get_abscisse() == self.p2.get_abscisse()

    def estHorizontale(self):
        return self.p1.get_ordonne() == self.p2.get_ordonne()

    def estSurDiagonale(self):
        return Segment.estVerticale(self) == Segment.estHorizontale(self)

    def longueur(self):
        return ((self.p1.get_abscisse()-self.p2.get_abscisse())**2 + (self.p1._ordonne()-self.p2.get_ordonne())**2)**0.5


s1 = Segment(p1, p2)
print(s1.estVerticale())
print(s1.estHorizontale())
print(s1.estSurDiagonale())


# Exercice 3
print("\nExercice3:\n")


class CString(object):
    nombreStr = 0

    def __init__(self, char):
        self.char = char
        CString.nombreStr += 1

    def get_chaine(self):
        return self.char

    def plus(self, lettre):
        return (CString(self.char + lettre))

    def plusGrandQue(self, chaine):
        return self.get_chaine() > chaine.get_chaine()

    def infOuEgale(self, chaine):
        return self.get_chaine() <= chaine.get_chaine()

    def plusGrand(self, chaine):
        if self.get_chaine() > chaine.get_chaine():
            return self
        else:
            return chaine
            
    def nbrChaines():
        return CString.nombreStr


s1 = CString("sa")
s2 = CString("ethan")
s1.plus("m")

print(s1.get_chaine())
print(s1.plusGrandQue(s2))
print(s1.infOuEgale(s2))
print("le nombre de chaines creées est: {}".format(CString.nbrChaines()))

if s1.plusGrandQue(s2):
    print("la chaine '{}' est plus grand que la chaine '{}'".format(
        s1.get_chaine(), s2.get_chaine()))
if s1.infOuEgale(s2):
    print("la chaine '{}' est plus petite que la chaine'{}'".format(
        s1.get_chaine(), s2.get_chaine()))

s3 = s1.plusGrand(s2)
print(s3.get_chaine())


# Exercice 4

class Definition(object):
    def __init__(self, char, definition):
        self.char = CString(char)
        self.definition = CString(definition)
        
    def get_Clef(self):
        return self.char.get_chaine()

    def get_definition(self):
        return self.definition.get_chaine()


homer = Definition("Homer", "buveur de bière")
print("La définition du mot {} est {}".format(
    homer.get_Clef(), homer.get_definition()))
