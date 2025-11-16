import pyxel

taille_case = 8
direction = 1

pyxel.init(23 * taille_case, 14 * taille_case, title="NEUILLEjeuNDC", fps=60)
pyxel.load("4.pyxres")
penguin = {"x":40, "y":40, "choix_img":0}
debug_dummy = {"x": 60, "y": 40, "choix_img":0}


#liste de liste contenant les différents niveaux du jeu
map1= [ "00000000000000000000000",
        "00000000000000000000000",
        "00000000000000000000000",
        "00000000000000000000000",
        "00000000000000000000000",
        "00000000000000000000000",
        "00111110000000001111100",
        "00000000000000000000000",
        "00000000000000000000000",
        "00000000000000000000000",
        "00000000000000000000000",
        "00000000000000000000000",
        "00111111111111111111100",
        "00111111111111111111100",
]

map2= [ "00000000000000000000000",
        "00000000000000000000000",
        "00000000000000000000000",
        "00000000000000000000000",
        "00111110000000001111100",
        "00000000000000000000000",
        "00000000000000000000000",
        "00000000000000000000000",
        "00000001111111110000000",
        "00000011111111111000000",
        "00001111111111111110000",
        "00001111111111111110000",
        "00011111111111111111000",
        "00111111111111111111100",
]



levels = [map1, map2]
map = levels[0]

NB_LIGNES = len(map)
NB_COLONNES = len(map[0])


GRAVITE = 4
liste_terrain = []
def matrice():
    global liste_terrain
    for y in range(NB_LIGNES):
        for x in range(NB_COLONNES):
            tuile = map[y][x]
            if tuile == 1:     
                a = (x, y)
                liste_terrain.append(a)
    return liste_terrain
print(liste_terrain)
    
     

    

def deplacement_horizontal():
     if pyxel.btn(pyxel.KEY_LEFT):
        penguin["x"] -= 3
        direction = -1
        penguin["choix_img"] = (pyxel.frame_count//10)%3 * 8
     elif pyxel.btn(pyxel.KEY_RIGHT):
        penguin["x"] += 3
        direction = 1
        penguin["choix_img"] = (pyxel.frame_count//10)%3 * 8

def gravite():
    penguin["y"]+= GRAVITE
    print(penguin["x"],penguin["y"])

def is_colliding(object_a, object_b):
    a_x1 = object_a["x"]
    a_x2 = object_a["x"] + taille_case  #coordonneés object 1
    a_y1 = object_a["y"]
    a_y2 = object_a["y"] + taille_case
    
    b_x1 = object_b["x"]
    b_x2 = object_b["x"] + taille_case  #coordonnées object 2
    b_y1 = object_b["y"]
    b_y2 = object_b["y"] + taille_case
    
    if a_x1 > b_x2 or a_y1 > b_y2 or a_x2 < b_x1 or a_y2 < b_y1:
        return False
    else:
        return True 

def update(): 
    #déplacement du personnage sur l'axe horizontal
    deplacement_horizontal() 
    #gravité exercé sur le joueur
    #gravite()
    #détecter les collisions
    #if is_colliding(penguin, debug_dummy):
     #   print("collision!")
    #else :
        #print(".")
    matrice()
  
def draw():
    #dessin du niveau avec un fond cyan et des platformes rouges
    pyxel.cls(pyxel.COLOR_LIGHT_BLUE)
    for y in range(NB_LIGNES):
        for x in range(NB_COLONNES):
            tuile = map[y][x]

            if tuile == "0":
                couleur = 6
            elif tuile == "1":
                couleur = 8  
            pyxel.rect(x * taille_case, y * taille_case, taille_case, taille_case, couleur)
    #mise à jour de l'emplacement du sprite du joueur
    pyxel.blt(penguin["x"], penguin["y"], 0, penguin["choix_img"], 56, 8, 8, pyxel.COLOR_DARK_BLUE)
    pyxel.blt(debug_dummy["x"], debug_dummy["y"], 0, debug_dummy["choix_img"], 48, 8, 8, pyxel.COLOR_DARK_BLUE)
    
          
pyxel.run(update, draw)
