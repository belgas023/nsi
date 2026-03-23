# 
from math import inf

def rendu_monnaie_itératif_avec_liste_pièces(monnaie, somme_à_rendre):
    """
    Paramètres :
        monnaie (list ou tuple) : Liste des valeurs des pièces disponibles
        somme_à_rendre (int) : Somme initiale à rendre
    Valeur renvoyée :
        (list) : Liste des pièces à rendre
                                          Attention, si l'algorithme ne réussit pas à trouver une solution, il doit renvoyer une liste vide
      """
      nb_pièces = [inf for i in range(somme_à_rendre + 1)]
      nb_pièces[0] = 0
      mem = {0:[]}
      for somme in range(somme_à_rendre + 1):
          for pièce in monnaie:
              if somme + pièce <= somme_à_rendre and 1 + nb_pièces[somme] < nb_pièces[somme + pièce]:
                  nb_pièces[somme + pièce] = 1 + nb_pièces[somme]
                  mem[somme + pièce] = mem[somme] + [pièce]
              if nb_pièces[somme_à_rendre] != inf:
                  return mem[somme_à_rendre]
      return []
