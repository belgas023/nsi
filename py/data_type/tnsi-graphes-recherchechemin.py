# Question 1 :
"""
Comme d'habitude, dessiner sur feuille le graphe ci-dessous.
"""

mongraphe = {'A':('B','D','E'),
             'B':('A','C','F'),
             'C':('B','E'),
             'D':('A','I'),
             'E':('A','C','G','H','I'),
             'F':('B','H'),
             'G':('E'),
             'H':('E','F','I'),
             'I':('D','E','H')}


# Question 2 :
"""
Pour trouver un chemin entre deux sommets,
- dans un 1er temps, on fait un parcours en largeur
      en mémorisant la provenance des sommets avec un dictionnaire.
- dans un 2ème temps, on reconstitue le chemin grâce à ce dictionnaire.
"""

def trouve_chemin(sommet_départ, sommet_arrivée, graphe):
    # 1er temps : Parcours en largeur avec mémorisation des provenances des sommets
    provenance = {}
    file = [sommet_départ]
    sommet_visite = []
    while len(file)>0:
        sommet = file.pop(0)
        if sommet not in sommet_visite:
            sommet_visite.append(sommet)
            for i in graphe[sommet]:
                file.append(i)
                provenance.update({i:sommet})
                

    # 2ème temps : Reconstitution du chemin parcouru en partant de la fin 
    print(provenance)
    a = sommet_départ
    resultat = []
    while a != sommet_arrivée:
        print(a)
        resultat.append(a)
        a = provenance[a]
    resultat.append(a)
    return resultat
        
        
print(trouve_chemin('A', 'H', mongraphe))
assert trouve_chemin("A", "H", mongraphe) == ['A', 'E', 'H']
print(trouve_chemin("B", "H", mongraphe))
assert trouve_chemin("B", "H", mongraphe) == ['B', 'F', 'H']

assert trouve_chemin("D", "C", mongraphe) == ['D', 'A', 'B', 'C']
assert trouve_chemin("H", "C", mongraphe) == ['H', 'E', 'C']
assert trouve_chemin("D", "H", mongraphe) == ['D', 'I', 'H']
