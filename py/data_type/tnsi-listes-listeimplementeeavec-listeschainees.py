# Objectif : Implémenter une liste sans s'appuyer sur l'objet list Python
# Nous n'utiliserons ni "self.liste = []", ni les fonctions et méthodes "len", "append", "pop",...
# En revanche, nous nous appuyerons sur la classe Maillon ci-dessous.

class Maillon:
    def __init__(self, valeur, maillon_suivant = None):
        self.valeur = valeur
        self.suivant = maillon_suivant
    
    def __repr__(self):
        return f"{self.valeur}->{self.suivant}"

class Liste:
    
    
    def __init__(self):
        self.début = None
    
    def est_vide(self):
        return self.début is None
    
    def longueur(self):
        if self.est_vide():
            return 0
        else:
            résultat = 1
            maillon = self.début
            while maillon.suivant != None:
                maillon = maillon.suivant
                résultat += 1
            return résultat
    
    def ajouter(self, valeur, indice=0):  # correction prof
        assert 0 <= indice < self.longueur(), "l'indice est incorrect"
        if indice == 0:
            self.début = Maillon(valeur, self.début)
        else:
            maillon_suivant = self.début
            for _ in range(indice):
                maillon_précédent = maillon_suivant
                maillon_suivant = maillon_suivant.suivant
            maillon_précédent.suivant = Maillon(valeur, maillon_suivant)

    def supprimer(self, indice=0):
        assert 0< indice < self.longueur(), 'indice inccorecte'
        if indice == 0:
            self.début = 

    def lire(self, indice):
        pass
        
    def __repr__(self):
        if self.début == None:
            return "None"
        else:
            return f"{self.début}"


a=Liste()
#assert a.est_vide()
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

# Remarque, nous avons implémenté notre liste chainée ci-dessus à l'aide de deux classes : Maillon et Liste.
# Nous aurions pu faire un autre choix et nous contenter de la classe Maillon mais c'est moins pratique ensuite (cf code ci-dessous ;-)
tête_liste = Maillon(5, Maillon(2, Maillon(3)))
print(tête_liste)
tête_liste.suivant = Maillon(10, tête_liste.suivant)
print(tête_liste)

    