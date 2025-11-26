import pyxel

taille_case = 8
direction = 1

pyxel.init(23 * taille_case, 14 * taille_case, title="NEUILLEjeuNDC", fps=100)
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

TILE_SIZE = 8
NB_LIGNES = len(map)
NB_COLONNES = len(map[0])

GRAVITE = 1
JUMP_SPEED = 10
SPEED = 1
ACCELERATION = 2


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

def jump(object):
    penguin["y"] += JUMP_SPEED
    
def acceleration():
    pass






def update():
    global coordonnee
    
    deplacement_horizontal() #applique deplacements

    print(penguin["x"], penguin["y"]) #debug - affiche coordonnées du pinguin
                    
    if is_colliding(penguin, debug_dummy):
        print("collision!")
    else :
        print(".")


 
def draw():
    pyxel.cls(pyxel.COLOR_CYAN) #affiche fond
    
    for y in range(NB_LIGNES):  #affiche terrain
        for x in range(NB_COLONNES):
            tuile = map[y][x]

            if tuile == "0":
                couleur = pyxel.COLOR_CYAN
            elif tuile == "1":
                couleur = 8  
            pyxel.rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE, couleur)
            
    pyxel.blt(penguin["x"], penguin["y"], 0, penguin["choix_img"], 56, 8, 8, pyxel.COLOR_DARK_BLUE)    #affiche sprites
    pyxel.blt(debug_dummy["x"], debug_dummy["y"], 0, debug_dummy["choix_img"], 56, 8, 8, pyxel.COLOR_DARK_BLUE)            
    
    


pyxel.run(update, draw)


