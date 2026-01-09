def cree_tableau(n):
    liste = []
    a = 1
    for i in range(n):
        liste.append([a+j+i for j in range(n)])
        a+=2
    return liste

def permute_quadrants(tableau, quadrant_1, quadrant_2, n):
    """
    Échange les contenus de deux quadrants carrés de taille n x n.
    Ces quadrants sont définis par les coordonnées du coin en haut à gauche et par leur largeur.
    Paramètres :
        tableau : Liste de listes (tableau carré)
        quadrant_1 : Tuple donnant la ligne puis la colonne du coin en haut et à gauche du quadrant 1
        quadrant_2 : Tuple donnant la ligne puis la colonne du coin en haut et à gauche du quadrant 2
        n : Entier positif donnant la largeur des deux cadrants
    Valeur renvoyée :
        Ne renvoie rien mais modifie le tableau donné en entrée
    """
    indice_q1_debut = 
    listeQ1 = tableau[quadrant_1[0]][quadrant_1[1]]
    listeQ2 = tableau[quadrant_2[0]][quadrant_2[1]]
    
tableau = cree_tableau(4)
quadrant_1 = (0,0)
quadrant_2 = (2,2)
n = 2

print(tableau)
print(tableau[quadrant_1[0]][quadrant_1[1]])
print(tableau[quadrant_2[0]][quadrant_2[1]])

                