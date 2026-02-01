"""
Jeu de la vie à programmer entièrement vous-même
"""
pass

"""
Votre travail :
1) Comprendre le principe du jeu en regardant les deux premières minutes de https://www.youtube.com/watch?v=S-W0NX97DB0
2) Programmer la première phase du jeu (dessin de la grille) :
   - L'écran est une grille de 64x64 cases de côté 6 pixels.
   - Le contenu de chaque case est mémorisé dans une liste de liste
     contenant des 0 (la case est vide) ou des 1 (la case contient une cellule vivante).
   - Au début du jeu, toutes les cases sont à 0,
     la souris est visible, le fond d'écran est marron.
   - Si le joueur fait un clic gauche sur une case, on affiche le carré bleu du fichier "res.pyxres"
     et s'il fait un clic droit, la case redevient marron.
   - Quand le joueur a terminé de tracer des motifs,
     il appuie sur la touche entrée pour lancer la seconde phase
3) Programmer la seconde phase du jeu (jeu de la vie) :
   - On masque la souris
   - Puis 5 fois par seconde, on recalcule et on réaffiche la grille
     en fonction des lois du jeu de la vie et on affiche en bas à gauche
     le numéro de la grille
"""