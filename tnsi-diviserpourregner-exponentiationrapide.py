#1) Compléter la fonction ci-dessous qui calcule x^n de façon récursive :
def exp(x, n):
    """
    On peut calculer x^n de façon récursive :
    x^0 = 1
    x^n = x * x^(n-1)

    Paramètres :
        x : flottant ou entier
        n : entier positif
    Valeur retournée :
        x^n : flottant
    """
    if n == 0:
        return 1
    else:
        return x * exp(x, n-1)

#Jeu de test à utiliser :
assert exp(5, 0) == 1
assert exp(5, 1) == 5
assert exp(5, 2) == 25
assert exp(1, 4) == 1
assert exp(10, 3) == 1000
assert exp(-3, 2) == 9


#2) Combien de multiplications faut-il faire pour calculer x^100 ?
#   Quelle est la complexité de la fonction ci-dessus ?

#il faut faire 100 multiplication
#complexité linéaire

#3) Compléter la fonction ci-dessous qui calcule x^n en utilisant l'exponentiation rapide :
def exp_rapide(x, n):
    """
    On peut calculer x^n plus rapidement :
    x^0 = 1
    si n est pair :   x^n = x^(n/2) * x^(n/2)
    si n est impair : x^n = x * x^(n-1)

    Paramètres :
        x : flottant ou entier
        n : entier positif
    Valeur retournée :
        x^n : flottant
    """
    if n == 0:
        return 1
    else:
        if n%2==0: #pair
            return exp_rapide(x, n/2)**2 #calculer au carré, ne pas faire une autre appel recursif
        else:
            return x * exp_rapide(x, n-1)

#Jeu de test à utiliser :
assert exp_rapide(5, 0) == 1
assert exp_rapide(5, 1) == 5
assert exp_rapide(5, 2) == 25
assert exp_rapide(1, 4) == 1
assert exp_rapide(10, 3) == 1000
assert exp_rapide(-3, 2) == 9


#4) Faire l'arbre des appels récursifs permettant de calculer x^100 avec cette nouvelle méthode.
#   Combien de multiplications va-t-on faire en tout ?
#   Quelle est la complexité de la fonction ci-dessus ?
#   Comparer la complexité des 2 méthodes

#On va faire 9 multiplication
#
