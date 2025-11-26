# Objectif : Implémenter une file en utilisant deux piles de la classe "Pile" ci-dessous.

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
        return self.sommet == None
    
    def empiler(self, valeur):
        self.sommet = Maillon(valeur, self.sommet)

    def lire_sans_dépiler(self):
        assert not self.est_vide(), "La pile est vide !"
        return self.sommet.valeur
        
    def dépiler(self):
        assert not self.est_vide(), "La pile est vide !"
        valeur_sommet = self.sommet.valeur
        self.sommet = self.sommet.suivant
        return valeur_sommet

    def __repr__(self):
        if self.sommet == None:
            return "None"
        else:
            return f"{self.sommet}"

class File:
    def __init__(self):
        self.p1 = Pile()
        self.p2 = Pile()
    
    def est_vide(self):
        pass

    def enfiler(self, valeur):
        pass
        
    def défiler(self):
        pass

    def __repr__(self):
        return f"{self.p1} / {self.p2}"


# Création de la file
a=File()
assert a.est_vide()
a.enfiler(10)
a.enfiler(11)
a.enfiler(12)
a.enfiler(13)
assert a.défiler() == 10
assert a.défiler() == 11
assert a.défiler() == 12
a.enfiler(14)
assert a.défiler() == 13
assert a.défiler() == 14
assert a.est_vide()