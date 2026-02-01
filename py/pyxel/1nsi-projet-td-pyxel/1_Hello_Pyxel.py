"""
Affiche un texte clignotant que l'on peut déplacer avec les flèches du clavier
"""
import pyxel

pyxel.init(128, 128, title="Hello", fps=10)

# Coordonnées du début du texte affiché
x = 40
y = 30

def update():
    global x, y
    if pyxel.btn(pyxel.KEY_RIGHT):
        x += 1
    elif pyxel.btn(pyxel.KEY_LEFT):
        x -= 1

def draw():
    pyxel.cls(0)
    pyxel.text(x, y, "Hello, Pyxel !", pyxel.frame_count % 16)

pyxel.run(update, draw)


"""
Votre travail :
1) Bien observer et mémoriser la structure du programme.
2) Consulter la documentation de pyxel pour bien comprendre
   le fonctionnement du programme dans les détails.
3) A quoi sert la ligne "global x, y" dans la fonction update ?
4) Observer la différence si on prend un fps de 1 ou 2.
5) Quelle touche du clavier permet de fermer le programme ?
6) Ajouter la possibilité de déplacer le "Hello, Pyxel !" avec les flèches haut et bas.
7) Remplacer toutes les occurences de "pyxel.btn" par "pyxel.btnp".
   Quelle différence observez-vous ? Quand préférer "btn" et quand préférer "btnp" ?
8) Interdire les déplacements qui feraient sortir le "Hello, Pyxel !" de la fenêtre du programme.
"""