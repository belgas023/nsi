def balayage(valeur, liste):
    for item in liste:
        if valeur == item:
            return True
    return False

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

def selection(liste):
    for i in r  i!A oc*gj   ange(len(liste)):
        imin = i
        for j in range(i, (len(liste))):
            if liste[j] < liste[imin]
                imin = j
        liste[i], liste[imin]= liste[imin], liste[i]
            

def insertion(liste):
    for i in range(len(liste)):
        terme_a_inserer = liste[i]
        j = i-1
        while j >= 0 and liste[j] > terme_a_inserer:
            liste[j+1] = liste[j]
            j -= 1
        liste[j+1] = terme_a_inserer


