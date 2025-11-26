import pyxel
from time import sleep


pyxel.init(256, 256, title="CHEVALIER", fps=30)
pyxel.load("2.pyxres")
player = {"x": 60, "y":60, "vx": 0, "vy": 0 ,"choix_img": 0, "cd": 0}

attackHitbox = {"x":1000, "y":1000, "choix_img":0, "exist": True}

debugDummy = {"x": 60, "y":60, "exist":True}


HUD = [ [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]


            


taille_case = 16
colonne = len(HUD[0])
ligne = len(HUD)

listeMur = []
for y in range(ligne):
        for x in range(colonne):
            tuile = HUD[y][x]
            if tuile == 1:
                listeMur.append({"x": x * taille_case, "y": y * taille_case})


direction = 1
dirctionvertical = 1
SPEED = 1
sword = 1  #1 --> epee de base, 2--> epee amelioré, 3--> epee ultime
xp = 0
ult = 0
gravier = 0 # 1= droite, 2= gauche, 3=haut, 4=bas
upgrade = 0

def mort(objet):
    if objet["exist"] == False :
        objet["x"], objet["y"] = 1000, 1000

def deplacement():
    global direction
    player["choix_img"] = 0
    if pyxel.btn(pyxel.KEY_LEFT):
        direction = -1
        player["choix_img"] = (pyxel.frame_count//2)%4 * 16
        player["vx"] += SPEED * direction
        gravier = 2
        
    elif pyxel.btn(pyxel.KEY_RIGHT):
        direction = 1
        player["choix_img"] = (pyxel.frame_count//2)%4 * 16
        player["vx"] += SPEED * direction
        player["y"] += player["vy"]
        gravier = 1

    elif pyxel.btn(pyxel.KEY_UP):
        dirctionvertical = -1
        player["vy"] += SPEED * dirctionvertical
        player["choix_img"] = (pyxel.frame_count//2)%4 * 16
        gravier = 3
    
    elif pyxel.btn(pyxel.KEY_DOWN):
        dirctionvertical = 1
        player["vy"] += SPEED * dirctionvertical
        player["choix_img"] = (pyxel.frame_count//2)%4 * 16
        gravier = 4
    
    player["x"] += player["vx"]
    player["y"] += player["vy"]
    
    if pyxel.btnr(pyxel.KEY_LEFT) or pyxel.btnr(pyxel.KEY_RIGHT):
        player["vx"] = 0
    if pyxel.btnr(pyxel.KEY_UP) or pyxel.btnr(pyxel.KEY_DOWN):
        player["vy"] = 0

def accelerationLimit():
    if player["vx"]>4:
        player["vx"] = 4
    elif player["vy"]>4:
        player["vy"] = 4
    elif player["vx"] < -4:
        player["vx"] = -4
    elif player["vy"] < -4:
        player["vy"] = -4

def isColliding(object_a, object_b):
    ax1 = object_a["x"]
    ax2 = object_a["x"] + taille_case
    ay1 = object_a["y"] 
    ay2 = object_a["y"] + taille_case
    
    bx1 = object_b["x"]
    bx2 = object_b["x"] + taille_case
    by1 = object_b["y"]
    by2 = object_b["y"] + taille_case
    if ax1 > bx2 or ay1 > by2 or ax2 < bx1 or ay2 < by1:
        return False
    else:
        return True

def mort(objet):
    if objet["exist"] == False :
        objet["x"], objet["y"] = 1000, 1000

 
def attack():
    global xp, sword, ult
    if pyxel.btnp(pyxel.KEY_SPACE):
        if direction == 1:
            attackHitbox["x"], attackHitbox["y"] = player["x"] + taille_case , player["y"]
        elif direction == -1:
            attackHitbox["x"], attackHitbox["y"] = player["x"] - taille_case , player["y"]
        player["cd"] = 10
        hitBox = True
        if player["cd"] == 0:
            mort(attackHitbox)
    if isColliding(attackHitbox, debugDummy):
        debugDummy["exist"] = False
        xp += 10
        ult += 5
        

def barreXp():
    global barreXpA, xpMax, xpDiz, xp, sword
    xpMax= 89
    barreXpA = xp/xpMax*100 // 1
    barre = 100
    xpDiz = 0
    if xp >xpMax:
        xp = 0
        sword +=1


def barreVie():
    global vie, barreVieA
    vie = 100
    vieMax = 100
    barreVieA = vie/vieMax*100 // 1
    if isColliding(debugDummy, player):
        vie -= 1

def barreUlti():
    global ult, barreUltA, ultMax
    ultMax = 100
    barreUltA = ult/ultMax*100 //1
    if ult > ultMax:
        ult = 0
        
    


def collision():
    if player["x"]<= 48:
        player["vx"] = 0
        player["x"] += 1
    elif player["y"] <= 32:
        player["vy"] = 0
        player["y"] += 1
    elif player["y"] > 176:
        player["vy"] = 0
        player["y"] -= 1
    elif player["x"] > 208:
        player["vx"] = 0
        player["x"] -=1
            


        
def update():
    
    deplacement()
    accelerationLimit()
    attack()
    mort(debugDummy)
    player["cd"] -= 1 if player["cd"] > 0 else 0
    collision()
    print(player["x"], player["y"])
    print(gravier)
    barreXp()
    if pyxel.btnp(pyxel.KEY_U):
        debugDummy["exist"] = True
        debugDummy["x"], debugDummy["y"] = 60, 60
    barreVie()
    barreUlti()

def draw():
    global HUD, ligne, colonne, taille_case, direction, barre
    pyxel.cls(pyxel.COLOR_GRAY)
    
    for y in range(ligne):
        for x in range(colonne):
            tuile = HUD[x][y]
            if tuile == 1:
                couleur = 0
            elif tuile == 0:
                couleur = 1
            pyxel.rect(taille_case*y, taille_case*x, taille_case, taille_case, couleur)
    
    if direction == 1:
        pyxel.blt(player["x"], player["y"], 0, player["choix_img"],16,16,16, 2)
    elif direction == -1:
        pyxel.blt(player["x"], player["y"], 0,player["choix_img"],16,-16,16, 2)
        
    if sword == 1:
        if direction == 1:
            pyxel.blt(player["x"]+ 8*direction, player["y"]+ 3, 0, attackHitbox["choix_img"], 64, 16, 16, 2)
        elif direction == -1:
             pyxel.blt(player["x"]+ 8*direction, player["y"]+ 3, 0, attackHitbox["choix_img"], 64, -16, 16, 2)
    elif sword == 2:
        pyxel.blt(player["x"]+ 8*direction, player["y"]+ 3, 0, attackHitbox["choix_img"],64, 16, 16, 2)
             
    pyxel.rect(attackHitbox["x"], attackHitbox["y"], taille_case, taille_case, pyxel.COLOR_RED)
    
    pyxel.blt(debugDummy["x"], debugDummy["y"], 0, player["choix_img"], 16,16,16,2)
    
    if isColliding(debugDummy, player):
        pyxel.rect(1*taille_case, 1*taille_case, taille_case, taille_case, pyxel.COLOR_GREEN)
    else:
        pyxel.rect(1*taille_case, 1*taille_case, taille_case, taille_case, pyxel.COLOR_RED)
    
    pyxel.text(10* taille_case, 20, str(xp), pyxel.COLOR_GREEN)
    
    
    pyxel.rect(150, 210, 100, 10, pyxel.COLOR_GRAY)   #dessine barre xp
    pyxel.rect(150, 210, barreXpA, 10, pyxel.COLOR_GREEN)
    
    pyxel.rect(10, 210, 100, 10, pyxel.COLOR_GRAY)   #dessine barre vie
    pyxel.rect(10, 210, barreVieA, 10, pyxel.COLOR_RED)
    
    pyxel.rect(80, 230, 100, 10, pyxel.COLOR_GRAY)   #dessine barre ult
    pyxel.rect(80, 230, barreUltA, 10, pyxel.COLOR_YELLOW)
    pyxel.blt(120, 220, 0, 16, 48, 16, 16, 2)
    
    pyxel.text(taille_case, taille_case, str(gravier), pyxel.COLOR_CYAN)
    pyxel.text(8, 16, "CHEVALIER", 7)
    #emplacement d'inventaire du joueur, affiche les items dans des cadres
    pyxel.blt(16, 32, 0, 0, 96, 16, 16, 2)
    pyxel.blt(16, 32, 0, 0, 64, 16, 16, 2)
    pyxel.blt(16, 57, 0, 0, 96, 16, 16, 2)
    pyxel.blt(16, 82, 0, 0, 96, 16, 16, 2)
            
pyxel.run(update, draw)