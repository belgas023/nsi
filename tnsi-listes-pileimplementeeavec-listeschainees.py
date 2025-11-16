# Objectif : Implémenter une pile en utilisant une liste chainée
# Nous n'utiliserons ni "self.liste = []", ni les fonctions et méthodes "len", "append", "pop",...
# En revanche, nous nous appuyerons sur la classe Maillon ci-dessous.

class Maillon:
    def __init__(self, valeur, maillon_suivant = None):
        self.valeur = valeur
        self.suivant = maillon_suivant
    
    def __repr__(self):
        return f"{self.valeur}>>{self.suivant}"

class Pile:
    def __init__(self):
        self.sommet = None
    
    def est_vide(self):
        return self.sommet is None
    
    def empiler(self, valeur):
        self.sommet = Maillon(valeur, self.sommet)

    def lire_sans_dépiler(self):
        return self.sommet.valeur
        
    def dépiler(self):
        voleur = self.sommet.valeur #derniere valeur
        self.sommet = self.sommet.suivant
        return voleur

    def __repr__(self):
        if self.sommet == None:
            return "None"
        else:
            return f"{self.sommet}"


# Création de la pile
a=Pile()
assert a.est_vide()
a.empiler(5)
assert not a.est_vide()
a.empiler(6)
assert a.lire_sans_dépiler() == 6
a.empiler(10)
a.empiler(11)
a.empiler(12)
assert a.dépiler() == 12
assert a.dépiler() == 11
assert a.dépiler() == 10
assert a.dépiler() == 6
assert a.dépiler() == 5
assert a.est_vide()
