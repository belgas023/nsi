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

assert exp(5, 0) == 1
assert exp(5, 1) == 5
assert exp(5, 2) == 25
assert exp(1, 4) == 1
assert exp(10, 3) == 1000
assert exp(-3, 2) == 9

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

assert exp_rapide(5, 0) == 1
assert exp_rapide(5, 1) == 5
assert exp_rapide(5, 2) == 25
assert exp_rapide(1, 4) == 1
assert exp_rapide(10, 3) == 1000
assert exp_rapide(-3, 2) == 9

