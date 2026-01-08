#1) Compléter la fonction ci-dessous qui cherche si une valeur est dans une liste ou non :
def recherche_balayage(liste, valeur):
    """
    Parcourt la liste jusqu'à trouver la valeur indiquée

    Paramètres :
        liste : liste Python de nombres entiers triée ou non
        valeur : nombre entier cherché
    Valeur renvoyée :
        True si la valeur a été trouvée et False sinon
    """
    for i in liste:
        if i == valeur:
            return True
    return False 

assert not recherche_balayage([27, 52, 26, 72, 59, 75, 36], 56)
assert recherche_balayage([27, 52, 26, 72, 59, 75, 36], 75)
assert not recherche_balayage([29, 44, 67, 81, 92, 37, 14, 96, 34, 28, 29, 9, 72], 78)
assert recherche_balayage([29, 44, 67, 81, 92, 37, 14, 96, 34, 28, 29, 9, 72], 72)
assert recherche_balayage([11, 100, 99, 32, 45, 17, 69, 72, 98, 73, 19, 78, 39, 3, 73, 99, 0, 16, 94, 76], 0)
assert recherche_balayage([11, 100, 99, 32, 45, 17, 69, 72, 98, 73, 19, 78, 39, 3, 73, 99, 0, 16, 94, 76], 11)


#2) Compléter la fonction ci-dessous qui fait la même chose que la fonction précédente,
#   mais en utilisant l'algorithme de dichotomie.
def recherche_dichotomie(liste, valeur):
    """
    Recherche la valeur indiquée dans la liste par dichotomie

    Paramètres :
        liste : liste Python de nombres entiers obligatoirement triée
        valeur : nombre entier cherché
    Valeur renvoyée :
        True si la valeur a été trouvée et False sinon
    """
    fin = len(liste)-1
    debut = 0
    while debut <= fin:
        milieu = (debut+fin)//2
        if valeur == liste[milieu]:
            return True
        elif valeur > liste[milieu]:
            debut = milieu +1
        else:
            fin = milieu -1
    return False
            

assert not recherche_dichotomie([26, 27, 36, 52, 59, 72, 75], 56)
assert recherche_dichotomie([26, 27, 36, 52, 59, 72, 75], 75)
assert not recherche_dichotomie([9, 14, 28, 29, 29, 34, 37, 44, 67, 72, 81, 92, 96], 78)
assert recherche_dichotomie([9, 14, 28, 29, 29, 34, 37, 44, 67, 72, 81, 92, 96], 72)
assert recherche_dichotomie([0, 3, 11, 16, 17, 19, 32, 39, 45, 69, 72, 73, 73, 76, 78, 94, 98, 99, 99, 100], 0)
assert recherche_dichotomie([0, 3, 11, 16, 17, 19, 32, 39, 45, 69, 72, 73, 73, 76, 78, 94, 98, 99, 99, 100], 11)


#3) Même chose mais dans une version récursive !
#   Pour que les performances restent bonnes, on ne génère pas les sous-listes
#   en les recopiant (slices ou autre) mais en passant en paramètre les indices
#   de début et de fin de la sous-liste considérée.

def recherche_dichotomie_recursive(liste, valeur, a=0, b=-10):
    """
    Recherche la valeur indiquée dans la liste par dichotomie (version récursive)

    Paramètres :
        liste : liste Python de nombres entiers obligatoirement triée
        valeur : nombre entier cherché
        a: indice de début de recherche
        b: indice de fin de recherche
    Valeur renvoyée :
        True si la valeur a été trouvée et False sinon
    """
    if b == -10:
        b = len(liste)-1
    if a <= b:
        i=(a+b)//2
        if liste[i] == valeur:
            return True
        elif 
assert not recherche_dichotomie_recursive([26, 27, 36, 52, 59, 72, 75], 56)
assert recherche_dichotomie_recursive([26, 27, 36, 52, 59, 72, 75], 75)
assert not recherche_dichotomie_recursive([9, 14, 28, 29, 29, 34, 37, 44, 67, 72, 81, 92, 96], 78)
assert recherche_dichotomie_recursive([9, 14, 28, 29, 29, 34, 37, 44, 67, 72, 81, 92, 96], 72)
assert recherche_dichotomie_recursive([0, 3, 11, 16, 17, 19, 32, 39, 45, 69, 72, 73, 73, 76, 78, 94, 98, 99, 99, 100], 0)
assert recherche_dichotomie_recursive([0, 3, 11, 16, 17, 19, 32, 39, 45, 69, 72, 73, 73, 76, 78, 94, 98, 99, 99, 100], 11)


#4) Comparer la complexité des 2 méthodes (balayage et dichotomie),
#   c'est à dire évaluer "en gros" le nombre de comparaisons que l'on fait
#   à chaque fois "dans le pire des cas" pour une liste de taille n.
