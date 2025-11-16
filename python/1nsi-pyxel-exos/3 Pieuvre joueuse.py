"""
Dès que l'on clique avec la souris pour déplacer le diamant,
la pieuvre se met à courir après le diamant.
"""
import pyxel

pyxel.init(128, 128, title="Pieuvre joueuse")
# Le fichier "sample.pyxres" est un fichier de ressource pyxel.
# Il contient une grande image de laquelle on va extraire les 2 sprites
# que l'on va utiliser ici : la pieuvre et le diamant.
# Ces sprites seront animés :
# - Il y a 3 dessins de pieuvres que l'on affichera successivement
#   pour donner l'impression qu'elle nage
# - Et 3 dessins de diamant pour donner l'impression qu'il scintille. 
pyxel.load("sample.pyxres")
pieuvre = {"x":60, "y":60, "choix_img":0}
diamant = {"x":20, "y":20, "choix_img":0}
pyxel.mouse(True)

def update():
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        diamant["x"], diamant["y"] = pyxel.mouse_x - 4, pyxel.mouse_y - 4
    pieuvre["choix_img"] = (pyxel.frame_count//5)%3 * 8
    diamant["choix_img"] = ((pyxel.frame_count//5)%3+1) * 8
    pieuvre["x"] -= (pieuvre["x"] - diamant["x"])/10
    pieuvre["y"] -= (pieuvre["y"] - diamant["y"])/10
        
def draw():
    pyxel.cls(pyxel.COLOR_BLACK)
    pyxel.blt(diamant["x"], diamant["y"], 0, diamant["choix_img"], 72, 8, 8, 0)
    pyxel.blt(pieuvre["x"], pieuvre["y"], 0, pieuvre["choix_img"], 48, 8, 8, 0)
    print(f"{pyxel.mouse_x},{pyxel.mouse_y}")
    
pyxel.run(update, draw)

"""
Votre travail :
1) Etudier sérieusement le fonctionnement du programme dans les détails.
2) Observer dans la console les coordonnées des 4 coins de la fenêtre du programme ?
   La fenêtre du programme fait-elle réellement 128 pixels de large x 128 pixels de haut 
   sur l'écran de votre ordinateur ?
3) Que se passe-t-il si on supprime le "pyxel.mouse(True)"
4) Dans le terminal de votre ordinateur, taper : "pyxel edit sample.pyxres"
   et repérer à quelles coordonnées sont les sprites de pieuvre.
5) Quelles sont les valeurs successives que prend la variable pieuvre["choix_img"] ?
   Faire le lien avec la question précédente.
6) Dans les appels à "pyxel.blt" qui sont dans la fonction draw, le dernier paramètre
   est à 0. Quelle est la signification de ce paramètre ?
7) Modifier le code pour que la pieuvre recouvre le diamant et non le contraire.
8) Modifier le code pour que la vitesse de déplacement de la pieuvre augmente
   toutes les 10 secondes.
9) Modifier le code de telle sorte que dès que la pieuvre arrive sur le diamant,
   on ne puisse plus déplacer le diamant et on affiche "Game over"
"""	