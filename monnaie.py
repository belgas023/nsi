from math import inf
def rendu_monnaie_glouton(monnaie, somme_à_rendre):
    """
    Paramètres :
        monnaie (list ou tuple) : Liste des valeurs des pièces disponibles triées par ordre décroissant
        somme_à_rendre (int) : Somme initiale à rendre
    Valeur renvoyée :
        (int) : Nombre minimum de pièces à rendre
    Attention, si l'algorithme ne réussit pas à trouver une solution 
        (par ex: rendu_monnaie_glouton((5,3,2), 6)), il doit renvoyer inf !
    """

    res = 0 # ce qu'on renvoie
    reste = somme_à_rendre 

    for piece in monnaie: # pour chacune des pieces
        while reste >= piece: # tant que le reste souscrvable par la piece
            reste -= piece # soustrait le reste par la piece
            res += 1 # incremente nombre piece a rendre

    if reste >0:
        return inf

    return res
                    
assert rendu_monnaie_glouton((100, 50, 20, 10, 5, 2, 1), 8) == 3
assert rendu_monnaie_glouton((100, 50, 20, 10, 5, 2, 1), 9) == 3
assert rendu_monnaie_glouton((100, 50, 20, 10, 5, 2, 1), 10) == 1
assert rendu_monnaie_glouton((100, 50, 20, 10, 5, 2, 1), 11) == 2
assert rendu_monnaie_glouton((100, 50, 20, 10, 5, 2, 1), 12) == 2
assert rendu_monnaie_glouton((100, 50, 20, 10, 5, 2, 1), 13) == 3
assert rendu_monnaie_glouton((100, 50, 20, 10, 5, 2, 1), 14) == 3
assert rendu_monnaie_glouton((100, 50, 20, 10, 5, 2, 1), 15) == 2
assert rendu_monnaie_glouton((5, 3, 2), 11) == inf
assert rendu_monnaie_glouton((5, 3, 2), 7) == 2
assert rendu_monnaie_glouton((5, 3, 2), 9) == inf
assert rendu_monnaie_glouton((5, 3, 2), 4) == inf
assert rendu_monnaie_glouton((5, 3, 2), 14) == inf
print("rendue monnaie glouton done")


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

    # cas de base:
    if reste == 0: # renvoie uniquement si pas inf
        return 0

    best = inf # init best avec inf au cas ou impossible

    for piece in monnaie:
        if reste - piece >=0:
            resultat = rendu_monnaie_recursif(monnaie, reste - piece)
            if resultat != inf:
                best = min(best, resultat)
    return best

print(rendu_monnaie_recursif((100, 10, 5, 3, 2), 8) )
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
print("done")


