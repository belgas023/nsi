import pyxel

taille_case = 8
direction = 1

pyxel.init(23 * taille_case, 14 * taille_case, title="NEUILLEjeuNDC", fps=30)
pyxel.load("4.pyxres")

penguin = {"x":40, "y":40, "choix_img":0}     #dictionnaire pour le joueur (penguin)
debug_dummy = {"x": 60, "y": 40, "choix_img":0} #dictionnnaire pour un test pour debuger

#liste de liste contenant les différents niveaux du jeu
map1= [ [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
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

taille_case = 8
NB_LIGNES = len(map)
NB_COLONNES = len(map[0])

GRAVITE = 3
JUMP_SPEED = 10
SPEED = 3               #constantes principales
ACCELERATION = 2


liste_terrain = []

for y in range(NB_LIGNES):  
    for x in range(NB_COLONNES):  #creer liste de dico pour chaque tuiles de terrain
        tuile = map[y][x]
        if tuile == 1:
            liste_terrain.append({"x":x * taille_case,"y":y * taille_case})

def collision(liste):
    for i in liste:
        if is_colliding(penguin, i):              #collision verticale
            penguin["y"] = i["y"] - taille_case
            
        
            

def deplacement_horizontal():
     if pyxel.btn(pyxel.KEY_LEFT):
        penguin["x"] -= SPEED
        direction = -1
        penguin["choix_img"] = (pyxel.frame_count//10)%3 * 8
     elif pyxel.btn(pyxel.KEY_RIGHT):
        penguin["x"] += SPEED
        direction = 1
        penguin["choix_img"] = (pyxel.frame_count//10)%3 * 8


def deplacementsVerticale():
    if pyxel.btnp(pyxel.KEY_UP):
        if isOnFloor(penguin):
            jump()

def gravite():
    if isOnFloor(penguin) == False :
        penguin["y"]+= GRAVITE
    #print(penguin["x"],penguin["y"])
    

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

def isOnFloor(object):
    a = False 
    for i in liste_terrain:
        if is_colliding(object, i):
            a = True
            print("floor")
        else:
            a = False
    return a



def jump():
    penguin["y"] -= JUMP_SPEED
    
def acceleration():
    pass

def update():
    global coordonnee
    
      
    gravite()    
    collision(liste_terrain)
    deplacement_horizontal() #applique deplacements
    deplacementsVerticale()
    
    
    #print(penguin["x"], penguin["y"]) #debug - affiche coordonnées du pinguin
                    
    #if is_colliding(penguin, debug_dummy):
     #   print("collision!")
    #else :
     #   print(".")


 
def draw():
    pyxel.cls(pyxel.COLOR_CYAN) #affiche fond
    
    for y in range(NB_LIGNES):  #affiche terrain
        for x in range(NB_COLONNES):
            tuile = map[y][x]

            if tuile == 0:
                couleur = pyxel.COLOR_CYAN
            elif tuile == 1:
                couleur = 8  
            pyxel.rect(x * taille_case, y * taille_case, taille_case, taille_case, couleur)
            
    pyxel.blt(penguin["x"], penguin["y"], 0, penguin["choix_img"], 56, 8, 8, pyxel.COLOR_DARK_BLUE)    #affiche sprites
    pyxel.blt(debug_dummy["x"], debug_dummy["y"], 0, debug_dummy["choix_img"], 56, 8, 8, pyxel.COLOR_DARK_BLUE)            
    if isOnFloor(penguin) == True :
        pyxel.rect(1* taille_case, 1*taille_case,taille_case, taille_case, pyxel.COLOR_GREEN)
    else:
        pyxel.rect(1* taille_case, 1*taille_case,taille_case, taille_case, pyxel.COLOR_RED)
    


pyxel.run(update, draw)



