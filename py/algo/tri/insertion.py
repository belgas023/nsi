def insertion(liste):
    for i in range(len(liste)):
        terme_a_inserer = liste[i]
        j = i-1
        while j >= 0 and liste[j] > terme_a_inserer:
            liste[j+1] = liste[j]
            j -= 1
        liste[j+1] = terme_a_inserer
