import pyxel

taille_case = 8
direction = 1

pyxel.init(23 * taille_case, 14 * taille_case, title="NEUILLEjeuNDC", fps=40)
pyxel.load("4.pyxres")
penguin = {"x":40, "y":40, "choix_img":0, "gCD":0, "vy":0, "vx":0}
debug_dummy = {"x": 85, "y": 48, "choix_img":0}
gravite_inversé = False
collision_activé = False
gravier = 1


#liste de liste contenant les différents niveaux du jeu
map1= [ [0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,2,2,2,2,2,0,0,0,0,0,0,0,0,0,2,2,2,2,2,0,0],
        [0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0],
        [0,0,3,3,3,3,3,0,0,0,0,0,0,0,0,0,3,3,3,3,3,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0],
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

#variable lié au joueur
GRAVITE = 0.5
JUMP = 6
SPEED = 0.4

#liste_terrain.append({"x":x * taille_case,"y":y * taille_case})
liste_terrain = []
listeDessous = []
listeDessus = []
for y in range(NB_LIGNES):  
    for x in range(NB_COLONNES):  #creer liste de dico pr chaque tuiles de terrain
        tuile = map[y][x]
        if tuile == 1:
            liste_terrain.append({"x":x * taille_case,"y":y * taille_case})
        elif tuile == 2:
            listeDessus.append({"x":x * taille_case, "y":y * taille_case})
        elif tuile == 3:
            listeDessous.append({"x":x * taille_case, "y":y *taille_case})
            
        
def deplacement_horizontal():
    #deplacement horizontale du joueur
    penguin["choix_img"] = 0
    global direction
    if pyxel.btn(pyxel.KEY_LEFT):
        direction = -1
        penguin["vx"] += SPEED 
        penguin["x"] += penguin["vx"] * direction
        penguin["choix_img"] = (pyxel.frame_count//10)%3 * 8    
    elif pyxel.btn(pyxel.KEY_RIGHT):
        direction = 1
        penguin["vx"] += SPEED 
        penguin["x"] += penguin["vx"] * direction
        penguin["choix_img"] = (pyxel.frame_count//10)%3 * 8
    elif pyxel.btnr(pyxel.KEY_LEFT) or pyxel.btnr(pyxel.KEY_RIGHT):
        penguin["vx"] = 0
        
def limitAcceleration():
    #limite de l'acceleration des deplacements
    if penguin["vx"] >= 4:
        penguin["vx"] = 4
        
def deplacement_vertical():
    #saut du joueur
     if pyxel.btnp(pyxel.KEY_SPACE) and isOnFloor(penguin):
         penguin["vy"] -= JUMP * gravier

        
def collision(liste):
    #collision entre penguin et le terrain
    for i in liste:
        if is_colliding(penguin, i) and gravite_inversé == False and dessusDessous(penguin) == True :
            penguin["y"] = i["y"] - taille_case
            penguin["vy"] = 0
        elif is_colliding(penguin, i) and gravite_inversé == True and dessusDessous(penguin) == False  :
            penguin["y"] = i["y"] + taille_case
            penguin["vy"] = 0
        
                         
def dessusDessous(penguin):
    #return True si penguin est au dessus des platform
    #return False si penguin est en dessous des platform
    for i in listeDessous:
        if is_colliding(penguin, i):
            return False
    for i in listeDessus:
        if is_colliding(penguin, i):
            return True 

def isOnFloor(penguin):
    #return True si penguin sur le sol
    for i in liste_terrain:
        if is_colliding(penguin, i):
            return True
            print("floor")
    return False

def gravite():
    #applique la gravite au penguin
    global gravier
    penguin["vy"]+= GRAVITE * gravier
    penguin["y"] += penguin["vy"]
    print(penguin["x"],penguin["y"])
    
def changement_couleur_décor():
    #change fond celon la gravité
    global gravite_inversé, collision_activé, gravier
    if is_colliding(penguin, debug_dummy):
        gravite_inversé = not gravite_inversé if penguin["gCD"] == 0 else gravite_inversé
        penguin["gCD"] = 30 if penguin["gCD"] == 0 else penguin["gCD"]
        if gravite_inversé == True:
            gravier = -1
        else:
            gravier = 1
            

def is_colliding(object_a, object_b):
    #permet de savoir si 2 objet se touchent
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


def offLimit(penguin):
    if penguin["x"] > 23*taille_case or penguin["x"]<0 or penguin["y"] > 14 *taille_case or penguin["y"] < 0:
        print("offLimit")
        return True
def gameOver():
    if offLimit(penguin) == True :
        penguin["x"], penguin["y"] = 40, 40
        gravite_inversé = False 
        


def update(): 
    #déplacement du personnage 
    deplacement_horizontal()
    deplacement_vertical()
    limitAcceleration()
    #gravité exercé sur le joueur
    gravite()
    #détecter les collisions
    collision(liste_terrain)
    #fonction inversant la gravité du jeu 
    changement_couleur_décor()
    #cooldown de l'inversion de gravité
    penguin["gCD"] -= (1 if penguin["gCD"] > 0 else 0)
    offLimit(penguin)
    
    
    
  
def draw():
    global direction, gravite_inversé, gravier
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
    elif direction == 1 and gravier == -1:
        pyxel.blt(penguin["x"], penguin["y"], 0, penguin["choix_img"], 56, 8, -8, pyxel.COLOR_DARK_BLUE)
    elif direction == -1 and gravier == -1:
        pyxel.blt(penguin["x"], penguin["y"], 0, penguin["choix_img"], 64, 8, -8, pyxel.COLOR_DARK_BLUE)
    pyxel.blt(debug_dummy["x"], debug_dummy["y"], 0, debug_dummy["choix_img"], 192, 8, 8, pyxel.COLOR_DARK_BLUE)
    pyxel.text(2* taille_case, 1*  taille_case,"isOnFloor()", pyxel.COLOR_BLACK)
    if isOnFloor(penguin) == True :
        pyxel.rect(1 * taille_case, 1 * taille_case, taille_case, taille_case, pyxel.COLOR_GREEN)
    else :
        pyxel.rect(1 * taille_case, 1 * taille_case, taille_case, taille_case, pyxel.COLOR_RED)
pyxel.run(update, draw)
