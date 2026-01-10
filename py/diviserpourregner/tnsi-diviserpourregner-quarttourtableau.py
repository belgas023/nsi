# On cherche ici à comprendre le principe de l'algorithme en l'appliquant à un tableau de nombres :
# -> Compléter les fonctions ci-dessous en testant bien chaque fonction
#    avant de passer à la suivante ;-)

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
        liste.append([a+j+i for j in range(n)])
        a+=2
    return liste


print(cree_tableau(4))

def affiche_tableau(tableau):
    for ligne in tableau:
        print(*ligne, sep="\t")
    print()
affiche_tableau(cree_tableau(4))



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
    tableau_modele = cree_tableau(n*2)
    q1 = quadrant_1
    q2 = quadrant_2
 
    #remplace 1er qudrant par 2eme quadrant
    tableau[q1[0]][q1[1]:q1[1]+n] = tableau[q2[0]][q2[1]:q2[1]+n]
    tableau[q1[0]+n-1][q1[1]:q1[1]+n] = tableau[q2[0]+n-1][q2[1]:q2[1]+n]
 
    #remplace 2eme qudrant par 1er qudrant a partire du qudrant modéle
    tableau[q2[0]][q2[1]:q2[1]+n] = tableau_modele[q1[0]][q1[1]:q1[1]+n]
    tableau[q2[0]+n-1][q2[1]:q2[1]+n] = tableau_modele[q1[0]+n-1][q1[1]:q1[1]+n]

    return tableau 
    


def tourne_recursif(tableau, carré, n):
    """
    Découpe un carré de taille n x n en 4 quadrants, puis fait faire à ces quadrants un quart de tour dans le sens horaire :
         ┌───┬───┐                        ┌───┬───┐     
         │ A │ B │                        │ D │ A │    
    Ex : ├───┼───┤ devient après rotation ├───┼───┤
         │ D │ C │                        │ C │ B │  
         └───┴───┘                        └───┴───┘      
    Puis la fonction s'appelle récursivement pour chacun des quadrants qui sont à leur tour découpés en 4...
    Le carré de départ est défini par les coordonnées du coin en haut à gauche et par sa largeur.
    Paramètres :
        tableau : Liste de listes (tableau carré)
        carré : Tuple donnant la ligne puis la colonne du coin en haut à gauche du cadrant
        n : Entier positif donnant la largeur du carré de départ. (n doit être une puissance de 2)
    Valeur renvoyée :
        Ne renvoie rien mais modifie le tableau donné en entrée
    """
    pass


# Lancement de l'algorithme sur un tableau de nombres
n = 4
tab = cree_tableau(n)
affiche_tableau(tab)
permute_quadrants(tab, (0,0), (2,2), n//2)
affiche_tableau(tab)
# tourne_recursif(tab, (0, 0), n)
# affiche_tableau(tab)
