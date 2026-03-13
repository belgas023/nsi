# rendue monnaie dynamique descendante recursif + mémoïsation
from math import inf

def rendu_monnaie_mémoïsation(monnaie, somme_à_rendre, mem = None):
    """
    Paramètres :
        monnaie (list ou tuple) : Liste des valeurs des pièces disponibles
        somme_à_rendre (int) : Somme initiale à rendre
        mem (dict) : dictionnaire associant à chaque somme à rendre le nombre minimal de pièces nécessaires
    Valeur renvoyée :
        (int) : Nombre minimum de pièces à rendre
    Attention, si l'algorithme ne réussit pas à trouver une solution, il doit renvoyer inf !
    """
    reste = somme_à_rendre 

    # init 1ere iteration
    if mem is None:
        mem = {}

    if reste == 0: # cas de base
        return 0

    best = inf # init la valeur de return

    for piece in monnaie:
        if reste - piece >= 0:
            res = rendu_monnaie_mémoïsation(monnaie, reste - piece)

            if res in mem:  # mémoïsation
                return mem[res]

            elif res != inf and res <  best:
                best = res + 1

    return best

print(rendu_monnaie_mémoïsation((100, 10, 5, 3, 2), 8))
assert rendu_monnaie_mémoïsation((100, 10, 5, 3, 2), 8) == 2
assert rendu_monnaie_mémoïsation((100, 10, 5, 3, 2), 9) == 3
assert rendu_monnaie_mémoïsation((100, 10, 5, 3, 2), 10) == 1
assert rendu_monnaie_mémoïsation((100, 10, 5, 3, 2), 11) == 3
assert rendu_monnaie_mémoïsation((100, 10, 5, 3, 2), 12) == 2
assert rendu_monnaie_mémoïsation((100, 10, 5, 3, 2), 1) == inf
assert rendu_monnaie_mémoïsation((5, 3, 2), 11) == 3
assert rendu_monnaie_mémoïsation((5, 3, 2), 7) == 2
assert rendu_monnaie_mémoïsation((5, 3, 2), 9) == 3
assert rendu_monnaie_mémoïsation((5, 3, 2), 4) == 2
assert rendu_monnaie_mémoïsation((5, 3, 2), 14) == 4
