[200~from math import inf

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
                                                          if mem == None:
                                                                  mem = {0:0}
                                                                      if somme_à_rendre in mem:
                                                                              return mem[somme_à_rendre]
                                                                                  elif somme_à_rendre < min(monnaie):
                                                                                          return inf
                                                                                              else:
                                                                                                      nb_pièces_possible = []
                                                                                                              for pièce in monnaie:
                                                                                                                          if pièce <= somme_à_rendre:
                                                                                                                                          nb_pièces_possible.append(1 + rendu_monnaie_mémoïsation(monnaie, somme_à_rendre - pièce, mem))
                                                                                                                                                  mem[somme_à_rendre] = min(nb_pièces_possible)
                                                                                                                                                          return mem[somme_à_rendre]
