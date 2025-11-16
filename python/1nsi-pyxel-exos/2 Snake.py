"""
Jeu de snake
"""
import pyxel, random

# Le jeu se déroule sur une grille carrée de 32 colonnes et 32 lignes
# Chaque cellule de la grille mesure 8x8 pixels
taille_grille = 32
pyxel.init(8*taille_grille, 8*taille_grille, title="Snake", fps=10)

# Le corps du serpent est formé de carrés consécutifs.
# snake["corps"] est la liste des tuples précisant les coordonnées de chacun de ces carrés.
# La tête du serpent est le dernier tuple de cette liste .
# snake["direction"] est un tuple qui précise le déplacement de la tête entre deux frames.
snake = {"corps": [(1,2), (2,2), (3,2)], "direction": (1,0)}

# Il y a en permanence une et une seule pomme dans la grille.
# Dès que le serpent mange la pomme, elle réapparaît ailleurs dans la grille 
pomme = {"position": (12,7)}

def update():
    if jeu ["phase"]==1:
        if pyxel.btnp(pyxel.KEY_LEFT):
            snake["direction"] = (-1,0)
        elif pyxel.btnp(pyxel.KEY_RIGHT):
            snake["direction"] = (1,0)
        elif pyxel.btnp(pyxel.KEY_UP):
            snake["direction"] = (0,-1)
        elif pyxel.btnp(pyxel.KEY_DOWN):
            snake["direction"] = (0,1)
        
    # Détermine la nouvelle position de la tête
    ancienne_tête = snake["corps"][-1]
    nouvelle_tête = (ancienne_tête[0] + snake["direction"][0], ancienne_tête[1] + snake["direction"][1])
    
    snake["corps"].append(nouvelle_tête)
    
    
    if nouvelle_tête != pomme["position"]:
        snake["corps"].pop(0)
    else:
        while pomme["position"] in snake["corps"]:
            pomme["position"] = (random.randint(0, taille_grille - 1), random.randint(0, taille_grille - 1))

def draw():
    # Efface l'écran
    pyxel.cls(pyxel.COLOR_BLACK)
    # Dessine le corps du serpent
    for carré in snake["corps"][0:-1]:
        pyxel.rect(carré[0]*8, carré[1]*8, 8, 8, 15)
    # Dessine la tête du serpent
    pyxel.rect(snake["corps"][-1][0]*8, snake["corps"][-1][1]*8, 8, 8, 14)
    # Dessine la pomme
    pyxel.rect(pomme["position"][0]*8, pomme["position"][1]*8, 8, 8, pyxel.COLOR_RED)
    
pyxel.run(update, draw)

"""
Votre travail :
1) Etudier sérieusement le fonctionnement du programme dans les détails.
2) Modifier le code pour interdire au serpent de revenir sur ses pas.
   Il n'a le droit que d'avancer, de tourner à gauche ou à droite.
3) Modifier le code pour qu'au moment de créer une nouvelle pomme,
   on vérifie qu'elle n'est pas sur le serpent.
4) Modifier le code pour que la partie s'arrête quand le serpent sort de la grille.
   Dans ce cas, le serpent arrête d'avancer et on affiche au milieu de l'écran "Game over".
5) Modifier le code pour que la partie s'arrête aussi quand le serpent se mord la queue.
"""