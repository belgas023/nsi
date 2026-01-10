def cree_tableau(n):
    liste = []
    a = 1
    for i in range(n):
        ligne=[]
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
    #indiceQ1 = tableau[ q1[0] ][ q1[1] ] #donne 1er valeur quadrant 1
    #indiceQ2 = tableau[ q2[0] ][ q2[1] ] #donne 1er valeur quadrant 2
    tableau_modele = tableau
    q1 = quadrant_1
    q2 = quadrant_2

    listeQ1 = [tableau[q1[0]][q1[1]:q1[1]+n],tableau[q1[0]+n-1][q1[1]:q1[1]+n]]
    listeQ2 = [tableau[q2[0]][q2[1]:q2[1]+n],tableau[q2[0]+n-1][q2[1]:q2[1]+n]]
    #renvoie liste des valeurs des quandrant 
    #sous forme [[1,2],
    #            [4,5]]
    
    #remplacage:
    tableau[q1[0]][q1[1]:q1[1]+n] = tableau[q2[0]][q2[1]:q2[1]+n]
    tableau[q1[0]+n-1][q1[1]:q1[1]+n] = tableau[q2[0]+n-1][q2[1]:q2[1]+n]

    tableau[q2[0]][q2[1]:q2[1]+n] = tableau_buffer[q1[0]][q1[1]:q1[1]+n]
    tableau[q2[0]+n-1][q2[1]:q2[1]+n] = tableau_buffer[q1[0]+n-1][q1[1]:q1[1]+n]
    return tableau




tableau = cree_tableau(4)
tableau_buffer = cree_tableau(4)
q1 = (0,0)
q2 = (2,2)
n = 2

print("==Initial==")                
print("tableau:")
affiche_tableau(tableau)

print(f"indice q1: {tableau[q1[0]][q1[1]]}")
print(f"indice q2: {tableau[q2[0]][q2[1]]}")

listeQ1 = [tableau[q1[0]][q1[1]:q1[1]+n],
           tableau[q1[0]+n-1][q1[1]:q1[1]+n]]

listeQ2 = [tableau[q2[0]][q2[1]:q2[1]+n],
           tableau[q2[0]+n-1][q2[1]:q2[1]+n]]

print(f"quadrant 1: {listeQ1}")
print(f"quadrant 2: {listeQ2}")

print("==Remplacage==")                
#remplace ligne1 et 2 de quadrant 1 par ligne 1 et 2 de qudrant 2
tableau[q1[0]][q1[1]:q1[1]+n] = tableau[q2[0]][q2[1]:q2[1]+n]
tableau[q1[0]+n-1][q1[1]:q1[1]+n] = tableau[q2[0]+n-1][q2[1]:q2[1]+n]

tableau[q2[0]][q2[1]:q2[1]+n] = tableau_buffer[q1[0]][q1[1]:q1[1]+n]
tableau[q2[0]+n-1][q2[1]:q2[1]+n] = tableau_buffer[q1[0]+n-1][q1[1]:q1[1]+n]

print("tableau:")
affiche_tableau(tableau)
