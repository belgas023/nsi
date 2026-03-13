# rendu monnaie dynamique montante
from math import inf

def rendu_monnaie_itératif(monnaie, somme_à_rendre):
    """
    Paramètres :
        monnaie (list ou tuple) : Liste des valeurs des pièces disponibles
        somme_à_rendre (int) : Somme initiale à rendre
    Valeur renvoyée :
        (int) : Nombre minimum de pièces à rendre
    Attention, si l'algorithme ne réussit pas à trouver une solution, il doit renvoyer inf !
    """
    nb_pièces = [inf for i in range(somme_à_rendre + 1)]
    nb_pièces[0] = 0
    for somme in range(somme_à_rendre + 1):
        for pièce in monnaie:
            if somme + pièce <= somme_à_rendre and 1 + nb_pièces[somme] < nb_pièces[somme + pièce]:
                nb_pièces[somme + pièce] = 1 + nb_pièces[somme]
            if nb_pièces[somme_à_rendre] != inf:
                return nb_pièces[somme_à_rendre]
    return inf

print(rendu_monnaie_itératif((100, 10, 5, 3, 2), 8))
assert rendu_monnaie_itératif((100, 10, 5, 3, 2), 8) == 2
assert rendu_monnaie_itératif((100, 10, 5, 3, 2), 9) == 3
assert rendu_monnaie_itératif((100, 10, 5, 3, 2), 10) == 1
assert rendu_monnaie_itératif((100, 10, 5, 3, 2), 11) == 3
assert rendu_monnaie_itératif((100, 10, 5, 3, 2), 12) == 2
assert rendu_monnaie_itératif((100, 10, 5, 3, 2), 1) == inf
assert rendu_monnaie_itératif((5, 3, 2), 11) == 3
assert rendu_monnaie_itératif((5, 3, 2), 7) == 2
assert rendu_monnaie_itératif((5, 3, 2), 9) == 3
assert rendu_monnaie_itératif((5, 3, 2), 4) == 2
assert rendu_monnaie_itératif((5, 3, 2), 14) == 4
