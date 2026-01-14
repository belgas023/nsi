def cree_tableau(n):
    """
    Crée un tableau carré de taille n x n.
    Les cases du tableau sont numérotées ligne par ligne.
    Ex avec n = 3 :
    [[1, 2, 3]
     [4, 5, 6]
     [7, 8, 9]]
     
    Paramètre :
        n entier positif
    Valeur renvoyée :
        liste de listes
    """
    liste = []
    a = 1
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne.append(a)
            a+=1
        liste.append(ligne)
    return liste

def affiche_tableau(tableau):
    for ligne in tableau:
        print(*ligne, sep="\t")
    print()

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
    for i in range(len(tableau)//2):
        for j in range(len(tableau)//2):
            #tableau[ quadrant_1[0] ][ quadrant_1[1] ], tableau[ quadrant_2[0] ][ quadrant_2[1] ] = tableau[ quadrant_2[0] ][ quadrant_2[1] ], tableau[ quadrant_1[0] ][ quadrant_1[1] ] 
            tableau[quadrant_1[0]+i][quadrant_1[1]+j], tableau[quadrant_2[0]+i][quadrant_2[1]+j] = tableau[quadrant_2[0]+i][quadrant_2[1]+j], tableau[quadrant_1[0]+i][quadrant_1[1]+j]

    return tableau


n = 4
tab = cree_tableau(n)
affiche_tableau(tab)
permute_quadrants(tab, (0,0), (2,2), n//2)
affiche_tableau(tab)

