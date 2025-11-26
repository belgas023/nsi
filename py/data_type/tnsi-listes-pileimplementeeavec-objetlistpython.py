# Objectif : Implémenter une pile en s'appuyant sur l'objet list Python
# On pourra utiliser ci-dessous les méthodes append et pop

class Pile:
    def __init__(self):
        self.pile=[]

    def est_vide(self):
        return self.pile == []
    
    def empiler(self,valeur):
        self.pile.append(valeur)
        
    def lire_sans_dépiler(self):
        return self.pile[-1]
    
    def dépiler(self):
        #asser verifier si pile vide
        return self.pile.pop(-1)
    
    def __repr__(self):
        return str(self.pile)


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
