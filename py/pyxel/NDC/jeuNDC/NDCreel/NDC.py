import pyxel
from time import sleep




pyxel.init(256, 256, title="NDC", fps=30)

pyxel.load("2.pyxres")

player = {"x":40, "y":40, "vx":0, "vy":0, "choix_img":0, "cd":0} #personnage avec toutes ses stats

debugDummy = {"x":80, "y":40, "exist":True}

attackHitbox = {"x":0, "y":0, "exist": True}



taille_case = 16
colonne = 16
ligne = 16


SPEED = 1

sword = 1  #1 --> epee de base, 2--> epee amelioré, 3--> epee ultime
xp = 0

def mort(objet):
    if objet["exist"] == False :
        objet["x"], objet["y"] = 1000, 1000


def deplacementHorizontale():
    global directionx, directiony
    directionx , directiony = 0, 0
    if pyxel.btn(pyxel.KEY_RIGHT):
        directionx = 1
    elif pyxel.btn(pyxel.KEY_LEFT):
        directionx = -1
    elif pyxel.btn(pyxel.KEY_UP):
        directiony = -1
    elif pyxel.btn(pyxel.KEY_DOWN):
        directiony = 1
    
    player["vx"] += SPEED * directionx
    player["vy"] += SPEED * directiony
    player["x"] += player["vx"] 
    player["y"] += player["vy"] 
    if pyxel.btnr(pyxel.KEY_LEFT) or pyxel.btnr(pyxel.KEY_RIGHT) or pyxel.btnr(pyxel.KEY_UP) or pyxel.btnr(pyxel.KEY_DOWN):
        player["vx"] = 0
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

test = True
def attack():
    global xp
    if pyxel.btnp(pyxel.KEY_SPACE):
        attackHitbox["x"], attackHitbox["y"] = player["x"] + taille_case , player["y"]
        player["cd"] = 10
        if player["cd"] == 0:
            attackHitbox["exist"] = False
    if isColliding(attackHitbox, debugDummy):
        test = False
        print("aaa")
        xp += 10
        debugDummy["exist"] = False 
    else :
        test = True
        
        


def update():
    deplacementHorizontale()
    accelerationLimit()
    attack()
    player["cd"] -= 1 if player["cd"] > 0 else 0
    print(player["cd"])
    mort(debugDummy)
    mort(attackHitbox)


def draw():
    pyxel.cls(pyxel.COLOR_GRAY)
    pyxel.blt(player["x"], player["y"], player["choix_img"],0,16,16,16, 2)
    pyxel.blt(debugDummy["x"], debugDummy["y"], player["choix_img"],0,16,16,16, 2)
    if sword == 1:
        pyxel.blt(player["x"]+ 8, player["y"]+ 3, 0, player["choix_img"], 64, 16, 16, 2)
        
    if isColliding(player, debugDummy):
        pyxel.rect(1*taille_case, 1*taille_case, taille_case, taille_case, pyxel.COLOR_GREEN)
    else :
        pyxel.rect(1*taille_case, 1*taille_case, taille_case, taille_case, pyxel.COLOR_RED)
    pyxel.rect(attackHitbox["x"], attackHitbox["y"], taille_case, taille_case, pyxel.COLOR_RED)
    if test ==  False :
        pyxel.rect(2* taille_case, 1* taille_case, taille_case, taille_case, pyxel.COLOR_BLACK)
    else:
        pyxel.rect(2* taille_case, 1* taille_case, taille_case, taille_case, pyxel.COLOR_DARK_BLUE)
        
    pyxel.text(3*taille_case, 1, str(xp), 0)
pyxel.run(update, draw)
