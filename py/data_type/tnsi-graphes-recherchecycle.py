# Question 1 :
"""
Dessiner sur feuille les deux graphes ci-dessous.
Contiennent-ils des cycles ?
"""

mongraphe1 = {"A":("B","C"),
             "B":("A","F"),
             "C":("A","D","E"),
             "D":("C"),
             "E":("C"),
             "F":("B")}

mongraphe2 = {"A":("B","C"),
             "B":("A","F"),
             "C":("A","D","E"),
             "D":("C","F"),
             "E":("C"),
             "F":("B","D")}

# Question 2 :
"""
Pour détecter si un graphe non orienté contient un cycle,
on adapte ci-dessous l'algorithme de parcours en profondeur.
"""

def trouve_cycle(sommet_départ, graphe):
    """ Renvoie True si un cycle est trouvé et False sinon"""
    pile = [sommet_départ]
    sommet_visite = []
    while len(pile)>0:
        sommet = pile.pop(-1)
        if sommet not in sommet_visite:
            sommet_visite.append(sommet)
            for i in graphe[sommet]:
                if i in pile:
                    return True
                else:
                    pile.append(i)
    return False


print(trouve_cycle("A", mongraphe1))
print(trouve_cycle("A", mongraphe2))
assert not trouve_cycle("A", mongraphe1)
assert trouve_cycle("A", mongraphe2)
print("test")
