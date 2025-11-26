# Objectif : Implémenter une liste en s'appuyant sur l'objet list Python

class Liste:
    def __init__(self):
        self.liste = []
    
    def est_vide(self): # test si vide
        return self.liste == []
    
    def longueur(self):
        return len(self.liste)
    
    def ajouter(self, valeur, indice=0):
        self.liste.insert(indice, valeur)
        
    def supprimer(self, indice=0):
        self.liste.pop(indice)
        
    def lire(self, indice):
        return self.liste[indice]
        
    def __repr__(self):
        return str(self.liste)
    
a=Liste()
assert a.est_vide()
assert a.longueur() == 0
a.ajouter(2,0)
assert not a.est_vide()
assert a.longueur() == 1
a.ajouter(5,0)
assert a.longueur() == 2
a.ajouter(3,2)
assert a.longueur() == 3
print(a)
a.supprimer(1)
assert a.longueur() == 2
print(a)
assert a.lire(0) == 5
assert a.lire(1) == 3