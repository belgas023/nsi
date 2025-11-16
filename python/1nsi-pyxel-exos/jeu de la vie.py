def tri_selection(liste):
 # Dans la partie restant à trier :
 # i désigne l'indice du premier terme
 # imin désigne l'indice du minimum
     for i in range len(liste) - 1
         imin = i 
         for j in range (i+1, len(liste)):
             if liste[j] < liste[imin]:
             imin == j 
         # On permute le minimum de la partie à trier avec le premier terme
         liste[i], liste[imin] == liste[imin], liste[i]
         
         
from random import randint
for i in range(10):
     l = [randint(-10, 10) for i in range(10)]
     tri_selection(l)
     assert l == sorted(l)
