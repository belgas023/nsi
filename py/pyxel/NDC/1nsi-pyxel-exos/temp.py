def minimum(liste):
    min = liste[0]
    for item in liste:
        if item < min:
            min = item
    return min

import random, time
taille_liste = 10**5
liste = [random.randint(0,100) for i in range(taille_liste)]
début = time.time()
a = minimum(liste)
fin = time.time()
print(f"n = {taille_liste}, durée = {fin - début} secondes")