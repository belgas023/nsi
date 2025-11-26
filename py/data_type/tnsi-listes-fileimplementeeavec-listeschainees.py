# Objectif : Implémenter une file en utilisant une liste chainée
# Nous n'utiliserons ni "self.liste = []", ni les fonctions et méthodes "len", "append", "pop",...
# En revanche, nous nous appuyerons sur la classe Maillon ci-dessous.

class Maillon:
    def __init__(self, valeur, maillon_suivant = None):
        self.valeur = valeur
        self.suivant = maillon_suivant
    
    def __repr__(self):
        return f"{self.valeur}>>{self.suivant}"

class File:
    def __init__(self):
        self.début = None
    
    def est_vide(self):
        pass
    
    def enfiler(self, valeur):
        pass

    def défiler(self):
        pass

    def __repr__(self):
        if self.début == None:
            return "None"
        else:
            return f"{self.début}"


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