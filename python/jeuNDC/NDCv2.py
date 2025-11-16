import pyxel

taille_case = 8
direction = 1

pyxel.init(23 * taille_case, 14 * taille_case, title="NEUILLEjeuNDC", fps=40)
pyxel.load("4.pyxres")
penguin = {"x":40, "y":40, "choix_img":0, "gCD": 0, "vy":0}
debug_dummy = {"x": 55, "y": 88, "choix_img":0}
gravite_inversé = False
collision_activé = False
gravier = 1


#liste de liste contenant les différents niveaux du jeu
map1= [ [0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
        [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
]
map2= [ [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
        [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
        [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
        [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
        [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
]



levels = [map1, map2]
map = levels[0]

NB_LIGNES = len(map)
NB_COLONNES = len(map[0])

#constantes
GRAVITE = 0.5
ACCELERATION = 15
SPEED = 3
JUMP = 5

liste_terrain = []

for y in range(NB_LIGNES):  
    for x in range(NB_COLONNES):  #creer liste de dico pr chaque tuiles de terrain
        tuile = map[y][x]
        if tuile == 1:
            liste_terrain.append({"x":x * taille_case,"y":y * taille_case})


def dash():
    if pyxel.btnp(pyxel.KEY_SHIFT):
        penguin["x"] += ACCELERATION * direction
        

def deplacement_horizontal():
    #sprite par defaut du joueur lorsqu'il ne se déplace pas
    penguin["choix_img"] = 0
    global direction
    if pyxel.btn(pyxel.KEY_LEFT):
        direction = -1
        penguin["x"] += SPEED* direction
        penguin["choix_img"] = (pyxel.frame_count//10)%3 * 8    
    elif pyxel.btn(pyxel.KEY_RIGHT):
        direction = 1
        penguin["x"] += SPEED * direction
        penguin["choix_img"] = (pyxel.frame_count//10)%3 * 8

def deplacementVerticale():
    if pyxel.btnp(pyxel.KEY_SPACE) and isOnFloor(penguin):
         penguin["vy"] -= JUMP * gravier
 

    
    
def collision(liste):
    for i in liste:
        if is_colliding(penguin, i) and gravite_inversé == False :
            penguin["y"] = i["y"] - taille_case
            penguin["vy"] = 0
        elif is_colliding(penguin, i) and gravite_inversé == True :
            penguin["y"] = i["y"] + taille_case
            penguin["vy"] = 0


            

def isOnFloor(object):
    for i in liste_terrain:
        if is_colliding(object, i):
            return True 
            print("floor")
    return False 
    

def gravite():
    global gravier
    penguin["vy"] += GRAVITE * gravier
    penguin["y"] += penguin["vy"]
    print(penguin["x"],penguin["y"])
    
def changement_couleur_décor():
    global gravite_inversé, collision_activé, gravier
    if is_colliding(penguin, debug_dummy):
        gravite_inversé = not gravite_inversé if penguin["gCD"] == 0 else gravite_inversé
        penguin["gCD"] = 30 if penguin["gCD"] == 0 else penguin["gCD"]
        if gravite_inversé == True:
            gravier = -1
        else:
            gravier = 1
            

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
    dash()
    #gravité exercé sur le joueur
    gravite()
    #détecter les collisions
    collision(liste_terrain)
    #fonction inversant la gravité du jeu 
    changement_couleur_décor()
    #cooldown de l'inversion de gravité
    penguin["gCD"] -= (1 if penguin["gCD"] > 0 else 0)
    #saut et autres
    deplacementVerticale()
    
  
def draw():
    global direction, gravite_inversé
    #dessin du niveau avec un fond cyan et des platformes rouges
    for y in range(NB_LIGNES):
        for x in range(NB_COLONNES):
            tuile = map[y][x] 
            if tuile == 0 and gravite_inversé:
                couleur = pyxel.COLOR_PEACH
            elif tuile == 0:
                couleur = 6
            elif tuile == 1 and gravite_inversé:
                couleur = 8
            elif tuile == 1:
                couleur = pyxel.COLOR_NAVY
            pyxel.rect(x * taille_case, y * taille_case, taille_case, taille_case, couleur)
    #mise à jour de la directioin du sprite lorsque le joueur va à gauche ou a droite 
    if direction == 1 and gravier == 1:
        pyxel.blt(penguin["x"], penguin["y"], 0, penguin["choix_img"], 56, 8, 8, pyxel.COLOR_DARK_BLUE)
    elif direction == -1 and gravier == 1:
        pyxel.blt(penguin["x"], penguin["y"], 0, penguin["choix_img"], 64, 8, 8, pyxel.COLOR_DARK_BLUE)
    #mise a jour du sprite celon la gravité (à l'endroit
    elif direction == 1 and gravier == -1:
        pyxel.blt(penguin["x"], penguin["y"], 0, penguin["choix_img"], 56, 8, -8, pyxel.COLOR_DARK_BLUE)
    elif direction == -1 and gravier == -1:
        pyxel.blt(penguin["x"], penguin["y"], 0, penguin["choix_img"], 64, 8, -8, pyxel.COLOR_DARK_BLUE)
    pyxel.blt(debug_dummy["x"], debug_dummy["y"], 0, debug_dummy["choix_img"], 48, 8, 8, pyxel.COLOR_DARK_BLUE)
        
    if isOnFloor(penguin) == True :
        pyxel.rect(1 * taille_case, 1 * taille_case, taille_case, taille_case, pyxel.COLOR_GREEN)
    else :
        pyxel.rect(1 * taille_case, 1 * taille_case, taille_case, taille_case, pyxel.COLOR_RED)
    pyxel.text(2* taille_case, 1*  taille_case,"isOnFloor()", pyxel.COLOR_BLACK)

pyxel.run(update, draw)




