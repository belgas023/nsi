"""
Jeu de la vie à programmer entièrement vous-même
"""

import pyxel
taille_ecran = 64
pyxel.init(taille_ecran*6, taille_ecran*6, title="Le jeu de la vie", fps=64)
taille_grille = 20 + 64 + 20
#ajouter zone tampon car grille infini donc evite erreure quand comptage cellule

matrice = []
for i in range(taille_grille):
    matrice.append([0]*taille_grille)
print(matrice)

pyxel.mouse(True)

def update():
    global xclique, yclique
    if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
        xclique, yclique = pyxel.mouse_x, pyxel.mouse_y
        print(xclique, yclique)
    #if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
     #   matrice[pyxel.mouse_y // 6+20][pyxel.mouse_x // 6 +20] = 1
    #elif pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT
                
def draw():
    pyxel.cls(pyxel.COLOR_BROWN)
    if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT): 
        pyxel.pset(xclique, yclique, pyxel.COLOR_BLACK)
    
    
pyxel.run(update, draw)
"""
Votre travail :
1) Comprendre le principe du jeu en regardant les deux premières minutes de https://www.youtube.com/watch?v=S-W0NX97DB0
2) Programmer la première phase du jeu (dessin de la grille) :
   - L'écran est une grille de 64x64 cases de côté 6 pixels.
   - Le contenu de chaque case est mémorisé dans une liste de liste
     contenant des 0 (la case est vide) ou des 1 (la case contient une cellule vivante).
   - Au début du jeu, toutes les cases sont à 0,
     la souris est visible, le fond d'écran est marron.
   - Si le joueur clique sur une case marron, on affiche le carré bleu du fichier "res.pyxres"
     et s'il clique sur une bleue, elle devient marron.
   - Quand le joueur a terminé de tracer des motifs,
     il appuie sur la touche entrée pour lancer la seconde phase
3) Programmer la seconde phase du jeu (jeu de la vie) :
   - On masque la souris
   - Puis 5 fois par seconde, on recalcule et on réaffiche la grille
     en fonction des lois du jeu de la vie et on affiche en bas à gauche
     le numéro de la grille
"""