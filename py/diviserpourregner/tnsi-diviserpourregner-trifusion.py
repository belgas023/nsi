# 1) Implémenter en Python la fonction fusion ci-dessous :

def fusion(liste1, liste2):
    """
    Cette fonction fusionne 2 listes triées en une seule liste triée

    Entrées : liste1 et liste2 sont deux listes triées de nombres
    Valeur renvoyée : une seule liste triée
    """

    m1, m2 = 0, 0 #marqueurs
    nouv_liste = []
    while m1!=len(liste1) and m2!=len(liste2):
        if liste1[m1]>liste2[m2]:
            nouv_liste.append(liste2[m2])
            m2+=1
        else:
            nouv_liste.append(liste1[m1])
            m1+=1
    if m1!=len(liste1):
        for i in liste1[m1:]:
            nouv_liste.append(i)
    if m2!= len(liste2):
        for i in liste2[m2:]:
            nouv_liste.append(i)
    return nouv_liste 
        
print(fusion([3, 6, 7],[1, 8]))
assert(fusion([3, 6, 7],[1, 8])) == [1, 3, 6, 7, 8]
assert(fusion([-3, 8],[0, 1, 8])) == [-3, 0, 1, 8, 8]
assert(fusion([3, 3, 4],[7, 8, 8, 9])) == [3, 3, 4, 7, 8, 8, 9]
assert(fusion([3, 6, 7],[])) == [3, 6, 7]
assert(fusion([],[1, 8, 10])) == [1, 8, 10]
assert(fusion([3, 6, 7],[-1, 0])) == [-1, 0, 3, 6, 7]


# 2) Implémenter en Python la fonction trifusion ci-dessous :

def trifusion(liste):
    """
    Cette fonction sépare la liste en deux moitiés
    puis s'appelle récursivement sur les deux sous-listes
    puis fait la fusion des deux sous-listes retournées

    Entrée : liste est une liste non triée de nombres
    Valeur renvoyée : liste triée
    """
    if len(liste)==1:
        return liste
    else:
        milieu = len(liste)//2
        return fusion(trifusion(liste[:milieu]), trifusion(liste[milieu:]))

print(trifusion([66, 78, 1, 37, 92]))
assert(trifusion([66, 78, 1, 37, 92])) == [1, 37, 66, 78, 92]
assert(trifusion([83, 47, 31, -5, 11, 49, 3, 25])) == [-5, 3, 11, 25, 31, 47, 49, 83]
assert(trifusion([25, -6, 84, 41, 72, 99, -3, 14, -8, 87, 58])) == [-8, -6, -3, 14, 25, 41, 58, 72, 84, 87, 99]
assert(trifusion([67, 5, -4, 21, -9, 17, 68, 15, 86, -10, 41, 42])) == [-10, -9, -4, 5, 15, 17, 21, 41, 42, 67, 68, 86]
assert(trifusion([52, 91, -3, 58, 73, 39, 74, 89, 74, 4, 90, 77, 90, 94, 99])) == [-3, 4, 39, 52, 58, 73, 74, 74, 77, 89, 90, 90, 91, 94, 99]
