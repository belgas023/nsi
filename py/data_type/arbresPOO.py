# Implementation arbres binaires avec POO

class Noeud():

    def __init__(self, cle, gauche=None, droit=None):
        self.cle = cle
        self.gauche = gauche
        self.droit = droit

    def __repr__(self):
        return f"({self.cle} -> {self.gauche}, {self.droit})".replace("None"," ")

# arbre:
E=Noeud("E")
F=Noeud("F")
D=Noeud("D",E,F)
C=Noeud("C")
B=Noeud("B",C,D)
J=Noeud("J",Noeud("K"),None)
H=Noeud("H",Noeud("I"),J)
G=Noeud("G",None,H)
A=Noeud("A",B,G)


def hauteur(noeud):
    if noeud is None:
        return -1
    else:
        return 1 + max( hauteur(noeud.gauche), hauteur(noeud.droit) )


def taille(noeud):
    if noeud is None:
        return 0
    else:
        return 1 + taille(noeud.gauche) + taille(noeud.droit)


def isFeuille(noeud):
    return noeud.gauche is None and noeud.droit is None


def nbrFeuilles(noeud):
    if isFeuille(noeud):
        return 1
    else:
        return nbrFeuilles(noeud.gauche)+nbrFeuilles(noeud.droit)


# DFS
def parcourPrefixe(noeud):
    if noeud is None:
        return None
    else:
        return noeud.cle, parcourPrefixe(noeud.gauche), parcourPrefixe(noeud.droit)


def parcourInfixe(noeud):
    if noeud is None:
        return None
    else:
        return parcourInfixe(noeud.gauche), noeud.cle, parcourInfixe(noeud.droit)


def parcourPostfixe(noeud):
    if noeud is None:
        return None
    else:
        return parcourPostfixe(noeud.gauche), parcourPostfixe(noeud.droit), noeud.cle

