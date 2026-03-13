#rendu monnaie recursif
from math import inf

def rendu_monnaie_recursif(monnaie, somme_à_rendre):
    """
    Paramètres :
        monnaie (list ou tuple) : Liste des valeurs des pièces disponibles
        somme_à_rendre (int) : Somme initiale à rendre
    Valeur renvoyée :
        (int) : Nombre minimum de pièces à rendre
    Attention, si l'algorithme ne réussit pas à trouver une solution, il doit renvoyer inf !
    """
    reste = somme_à_rendre

    # cas de base
    if reste == 0: # = exclusif car elimine les cas ou negatif
        return 0
    
    best = inf # init best avec inf

    for piece in monnaie:
        if reste - piece >= 0: # tant que soustraiable
            res = rendu_monnaie_recursif(monnaie, reste - piece)
            if res != inf and res < best:
                best = res + 1
    return best


assert rendu_monnaie_recursif((100, 10, 5, 3, 2), 8) == 2
assert rendu_monnaie_recursif((100, 10, 5, 3, 2), 9) == 3
assert rendu_monnaie_recursif((100, 10, 5, 3, 2), 10) == 1
assert rendu_monnaie_recursif((100, 10, 5, 3, 2), 11) == 3
assert rendu_monnaie_recursif((100, 10, 5, 3, 2), 12) == 2
assert rendu_monnaie_recursif((100, 10, 5, 3, 2), 1) == inf
assert rendu_monnaie_recursif((5, 3, 2), 11) == 3
assert rendu_monnaie_recursif((5, 3, 2), 7) == 2
assert rendu_monnaie_recursif((5, 3, 2), 9) == 3
assert rendu_monnaie_recursif((5, 3, 2), 4) == 2
assert rendu_monnaie_recursif((5, 3, 2), 14) == 4
