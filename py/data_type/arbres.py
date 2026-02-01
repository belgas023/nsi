# Implementation arbres binaire avec listes

# Arbre:
#    A
#   / \
#  B   C 
# / \
#D   E

nD = ['d', [], []]
nE = ['e', [], []]

nB = ['b', nD, nE]
nC = ['c', [], []]

nA = ['a', nB, nC] 


def hauteur(noeud):
    if noeud == []: 
        return -1
    else:
        return 1 + max( hauteur(noeud[1]),hauteur(noeud[2]) )


def taille(noeud):
    if noeud == []:
        return 0
    else:
        return 1 + taille(noeud[1]) + taille(noeud[2])


def isFeuille(noeud):
    return noeud[1] == [] and noeud[2] == []


def nbrFeuille(noeud):
    if isFeuille(noeud):
        return 1
    else:
        return nbrFeuille(noeud[1]) + nbrFeuille(noeud[2])


#DFS
def parcourPrefixe(noeud):
    if noeud == []:
        return None
    else:
        return noeud[0], parcourPrefixe(noeud[1]), parcourPrefixe(noeud[2])
 

def parcourInfixe(noeud):
    if noeud == []:
        return None
    else:
        return parcourInfixe(noeud[1]), noeud[0], parcourInfixe(noeud[2])


 def parcourPostfixe(noeud):
    if noeud == []:
        return None
    else:
        return parcoourPostfixe(noeud[1]), parcourPostfixe(noeud[2]), noeud[0]


def BFS(noeud):
    res = []
    file = [noeud]
    while len(file)>0:
        print(file.pop(0))
        res.append(noeud)
        if noeud[1] != []:
            file.append(noeud[1])
        elif noeud[2] != []:
            file.append(noeud[2])
    return res

