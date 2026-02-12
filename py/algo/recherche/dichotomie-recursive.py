def recherche_balayage(liste, valeur):
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

def recherche_dichotomie(liste, valeur):
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

def recherche_dichotomie_recursive(liste, valeur, a=0, b=-10):
    if b == -10:
        b = len(liste)-1
    if a <= b:
        i=(a+b)//2
        if liste[i] == valeur:
            return True
        elif liste[i] <= valeur:
            return recherche_dichotomie_recursive(liste, valeur, i +1, b)
        else:
            return recherche_dichotomie_recursive(liste, valeur, a, i-1)

assert not recherche_dichotomie_recursive([26, 27, 36, 52, 59, 72, 75], 56)
assert recherche_dichotomie_recursive([26, 27, 36, 52, 59, 72, 75], 75)
assert not recherche_dichotomie_recursive([9, 14, 28, 29, 29, 34, 37, 44, 67, 72, 81, 92, 96], 78)
assert recherche_dichotomie_recursive([9, 14, 28, 29, 29, 34, 37, 44, 67, 72, 81, 92, 96], 72)
assert recherche_dichotomie_recursive([0, 3, 11, 16, 17, 19, 32, 39, 45, 69, 72, 73, 73, 76, 78, 94, 98, 99, 99, 100], 0)
assert recherche_dichotomie_recursive([0, 3, 11, 16, 17, 19, 32, 39, 45, 69, 72, 73, 73, 76, 78, 94, 98, 99, 99, 100], 11)

