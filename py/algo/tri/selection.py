def selection(liste):
    for i in range(len(liste)):
        imin = i
        for j in range(i, (len(liste))):
            if liste[j] < liste[imin]:
                imin = j
        liste[i], liste[imin]= liste[imin], liste[i]
