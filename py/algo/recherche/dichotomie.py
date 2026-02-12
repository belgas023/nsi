def dichotomie(valeur, liste):
    a = 0
    b = len(liste)-1
    while a <= b:
        i = (a+b)//2
        if valeur == liste[i]:
            return True
        elif valeur > liste[i]:
            a = i+1
        else:
            b = i-1
    return False
