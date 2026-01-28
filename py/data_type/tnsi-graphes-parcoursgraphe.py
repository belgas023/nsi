# Question 1 :
"""
Représenter le graphe ci-dessous sur une feuille de papier :
"""
mongraphe = {"A":("B","F"),
             "B":("A","C","D","G"),
             "C":("B","E"),
             "D":("B","I"),
             "E":("C","I"),
             "F":("A","G","H"),
             "G":("B","F","I"),
             "H":("F","I"),
             "I":("D","E","G","H")}

# Question 2 :
"""
On veut parcourir tous les sommets du graphe.

Commençons par l'algorithme de parcours en largeur (BFS - Breadth First Search) :
Principe : On choisit d'explorer en priorité les plus anciens sommets : Utilisation d'une file
---------------------------------------------------------------------
Créer une file des sommets à traiter et une liste des sommets visités 
Enfiler le sommet de départ
Tant que la file n'est pas vide :
    Défiler le plus ancien sommet
    S'il n'est pas dans la liste des sommets visités :
        L'ajouter à la liste des visités
        Parcourir ses voisins, et les enfiler s'ils ne sont pas encore dans la liste des sommets visités
A la fin, renvoyer la liste des sommets visités
---------------------------------------------------------------------

Tester cet algorithme sur feuille (sans ordinateur)
et vérifier que si l'on part du sommet A et que l'on parcours toujours les voisins d'un sommet par ordre alphabétique,
on obtient comme parcours : 'A', 'B', 'F', 'C', 'D', 'G', 'H', 'E', 'I'
"""

# Question 3 :
"""
Ecrire et tester la fonction ci-dessous
"""
def parcours_largeur_itératif(sommet_départ, graphe):
    file = [sommet_départ]
    sommets_visite = []
    while len(file) > 0:
        sommet = file.pop(0)
        if sommet not in sommets_visite:
            sommets_visite.append(sommet)
            for i in graphe[sommet]:
                file.append(i)
    return sommets_visite
    
        
#print(parcours_largeur_itératif("A", mongraphe))
assert parcours_largeur_itératif("A", mongraphe) == ['A', 'B', 'F', 'C', 'D', 'G', 'H', 'E', 'I']
assert parcours_largeur_itératif("C", mongraphe) == ['C', 'B', 'E', 'A', 'D', 'G', 'I', 'F', 'H']
assert parcours_largeur_itératif("H", mongraphe) == ['H', 'F', 'I', 'A', 'G', 'D', 'E', 'B', 'C']

# Question 4
"""
Etudions maintenant l'algorithme de parcours en profondeur (DFS - Depth First Search)
Principe : On choisit d'explorer en priorité les plus récents sommets : Utilisation d'une pile
---------------------------------------------------------------------
Créer une pile des sommets à traiter et une liste des sommets visités 
Empiler le sommet de départ
Tant que la pile n'est pas vide :
    Dépiler le plus récent sommet
    S'il n'est pas dans la liste des sommets visités :
        L'ajouter à la liste des visités
        Parcourir ses voisins, et les empiler s'ils ne sont pas encore dans la liste des sommets visités
A la fin, renvoyer la liste des sommets visités
---------------------------------------------------------------------

Tester cet algorithme sur feuille (sans ordinateur)
et vérifier que si l'on part du sommet A et que l'on parcours toujours les voisins d'un sommet par ordre alphabétique,
on obtient comme parcours : 'A', 'F', 'H', 'I', 'G', 'B', 'D', 'C', 'E'
"""

# Question 5 :
"""
Ecrire et tester la fonction ci-dessous
"""
def parcours_profondeur_itératif(sommet_départ, graphe):
    pile = [sommet_départ]
    sommets_visite = []
    while len(pile)>0:
        sommet = pile.pop(-1)
        if sommet not in sommets_visite:
            sommets_visite.append(sommet)
            for i in graphe[sommet]:
                pile.append(i)
    return sommets_visite

assert parcours_profondeur_itératif("A", mongraphe) == ['A', 'F', 'H', 'I', 'G', 'B', 'D', 'C', 'E']
assert parcours_profondeur_itératif("C", mongraphe) == ['C', 'E', 'I', 'H', 'F', 'G', 'B', 'D', 'A']
assert parcours_profondeur_itératif("H", mongraphe) == ['H', 'I', 'G', 'F', 'A', 'B', 'D', 'C', 'E']

# Question 6
"""
Il existe aussi une version récursive assez simple du parcours en profondeur :
---------------------------------------------------------------------
Ajouter le sommet de départ à la liste des sommets visités
Parcourir ses voisins, et s'ils ne sont pas encore dans la liste des sommets visités, appeler récursivement la fonction sur ces voisins
---------------------------------------------------------------------

Tester cet algorithme sur feuille (sans ordinateur) en dessinant l'arbre des appels récursifs
et vérifier que si l'on part du sommet A et que l'on parcours toujours les voisins d'un sommet par ordre alphabétique,
on obtient comme parcours : 'A', 'B', 'C', 'E', 'I', 'D', 'G', 'F', 'H'
"""

def parcours_profondeur_récursif(sommet_départ, graphe, sommets_visités:list):
    sommets_visités.append(sommet_départ)
    for i in graphe[sommet_départ]:
        if i not in sommets_visités:
            parcours_profondeur_récursif(i,graphe, sommets_visités)
    
    
sommets_visités = []
parcours_profondeur_récursif("A", mongraphe, sommets_visités)
assert sommets_visités == ['A', 'B', 'C', 'E', 'I', 'D', 'G', 'F', 'H']

sommets_visités = []
parcours_profondeur_récursif("C", mongraphe, sommets_visités)
assert sommets_visités == ['C', 'B', 'A', 'F', 'G', 'I', 'D', 'E', 'H']

sommets_visités = []
parcours_profondeur_récursif("H", mongraphe, sommets_visités)
assert sommets_visités == ['H', 'F', 'A', 'B', 'C', 'E', 'I', 'D', 'G']



