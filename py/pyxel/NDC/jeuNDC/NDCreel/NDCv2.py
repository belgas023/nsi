import pyxel
from time import sleep
import random


pyxel.init(256, 256, title="CHEVALIER", fps=30)
pyxel.load("2.pyxres")
player = {"x": 60, "y":60, "vx": 0, "vy": 0 ,"choix_img": 0, "cd": 0, "exist": True}
ennemi = {"x": 100, "y": 80, "choix_img": 64, "exist": True}
attackHitbox = {"x":0, "y":0, "choix_img": 0,"exist": True}


HUD = [ [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], #cree un hud 
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

direction = 1
dirctionvertical = 1
SPEED = 1
sword = 1  #1 --> epee de base, 2--> epee amelioré, 3--> epee ultime
xp = 0
ult = 0
vague = 1
atack = False
level = 1

def mort(objet):
    if objet["exist"] == False :    # evoie tres loin le truc qui meurt
        objet["x"], objet["y"] = 1000, 1000

def monstre_deplacement():
    ennemi["choix_img"] = 64
    if ennemi["x"] != player["x"] and ennemi["y"] != player["y"]: #deplacement des montres
        ennemi["x"] -= (ennemi["x"] - player["x"])/20
        ennemi["y"] -= (ennemi["y"] - player["y"])/20
        ennemi["choix_img"] = ((pyxel.frame_count//2)%4 +4)* 16
    
def barreXp():
    global barreXpA, xpMax, xpDiz, xp # barre d'exp qui augmente quand on tue un monstre
    xpMax= 89
    barreXpA = xp/xpMax*100 // 1
    barre = 100
    xpDiz = 0
    if xp >xpMax:   # se remet au debut quand on atteint 100
        xp = 0
        level += 1

def deplacement():
    global direction
    player["choix_img"] = 0
    if pyxel.btn(pyxel.KEY_LEFT):
        direction = -1
        player["choix_img"] = (pyxel.frame_count//2)%4 * 16 #ajoute a vitesse x une vitess et une direction
        player["vx"] += SPEED * direction
        
        
    elif pyxel.btn(pyxel.KEY_RIGHT):
        direction = 1
        player["choix_img"] = (pyxel.frame_count//2)%4 * 16
        player["vx"] += SPEED * direction
        player["y"] += player["vy"]
        

    elif pyxel.btn(pyxel.KEY_UP):
        dirctionvertical = -1
        player["vy"] += SPEED * dirctionvertical
        player["choix_img"] = (pyxel.frame_count//2)%4 * 16
        
    
    elif pyxel.btn(pyxel.KEY_DOWN):
        dirctionvertical = 1
        player["vy"] += SPEED * dirctionvertical
        player["choix_img"] = (pyxel.frame_count//2)%4 * 16
        
    
    player["x"] += player["vx"]  #ajoute aux coordonnée du joueur la vitesse
    player["y"] += player["vy"]
    
    if pyxel.btnr(pyxel.KEY_LEFT) or pyxel.btnr(pyxel.KEY_RIGHT):
        player["vx"] = 0
    if pyxel.btnr(pyxel.KEY_UP) or pyxel.btnr(pyxel.KEY_DOWN):
        player["vy"] = 0



def accelerationLimit():
    if player["vx"]>4:
        player["vx"] = 4
    elif player["vy"]>4:  #donne un limite a l'acceleration du joueur
        player["vy"] = 4
    elif player["vx"] < -4:
        player["vx"] = -4
    elif player["vy"] < -4:
        player["vy"] = -4

def isColliding(object_a, object_b):
    ax1 = object_a["x"]
    ax2 = object_a["x"] + taille_case  # test si 2 truc se touche
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

def attack():
    global xp, sword, atack, vague, ult
    if not atack:
        attackHitbox["x"], attackHitbox["y"] = -10000, 50000
    if direction == 1 and player["cd"] == 0 and not atack:
        if pyxel.btnp(pyxel.KEY_SPACE):
            attackHitbox["x"], attackHitbox["y"] = player["x"] + taille_case , player["y"]
            atack = True
            player["cd"] = 10
    elif direction == -1 and player["cd"] == 0 and not atack:
        if pyxel.btnp(pyxel.KEY_SPACE):
            attackHitbox["x"], attackHitbox["y"] = player["x"] - taille_case , player["y"]
            atack = True
            player["cd"] = 10
    atack = False
    print(player["cd"])
    
    if isColliding(attackHitbox, ennemi):
        ennemi["exist"] = False
        mort(ennemi)
        vague += 1
        ennemi["exist"] = True
        xp += 10
        mort(ennemi)
        ult += 5
        
def collision():
    if player["x"]<= 48:
        player["vx"] = 0
        player["x"] += 1
    elif player["y"] <= 32:
        player["vy"] = 0    #collision de bordure
        player["y"] += 1
    elif player["y"] > 176:
        player["vy"] = 0
        player["y"] -= 1
    elif player["x"] > 208:
        player["vx"] = 0
        player["x"] -=1
        
def barreUlti():
    global ult, barreUltA, ultMax
    ultMax = 100
    barreUltA = ult/ultMax*100 //1  # barre de pouvoir (sert a rien on a pas fini)
    if ult > ultMax:
        ult = 0
        
def barreVie():
    global vie, barreVieA
    vie = 100
    vieMax = 100
    barreVieA = vie/vieMax*100 // 1 # abrre de vie (sert a rien on a pas fini
    if isColliding(ennemi, player):
        vie -= 1
              
        
def update():
    
    global vague
    deplacement()
    accelerationLimit()
    attack()
    barreXp()
    barreVie()
    barreUlti()
    collision()
    player["cd"] -= 1 if player["cd"] > 0 else 0 # chronometre
    mort(attackHitbox)
    if pyxel.btnp(pyxel.KEY_E):
        vague += 1
    monstre_deplacement()
    if mort(player):
        pyxel.music[0].on

def draw():
    global HUD, ligne, colonne, taille_case, direction, level, barreUltA
    pyxel.cls(pyxel.COLOR_GRAY)
    
    for y in range(ligne):
        for x in range(colonne):  #dessine le hud en fonction de la matrice du debut
            tuile = HUD[x][y]
            if tuile == 1:
                couleur = 0
            elif tuile == 0:
                couleur = 1
            pyxel.rect(taille_case*y, taille_case*x, taille_case, taille_case, couleur)
            
    pyxel.rect(150, 210, 100, 10, pyxel.COLOR_GRAY)
    pyxel.rect(150, 210, barreXpA, 10, pyxel.COLOR_LIGHT_BLUE) #dessine barre d'xp
    pyxel.blt(240, 207, 0, 128,48,16,16,2)
    
    pyxel.rect(30, 210, 100, 10, pyxel.COLOR_GRAY)   #dessine barre vie
    pyxel.rect(30, 210, barreVieA, 10, pyxel.COLOR_RED)
    pyxel.blt(20,207,0, 112, 48, 16, 16, 2)
    
    pyxel.rect(80, 230, 100, 10, pyxel.COLOR_GRAY)   #dessine barre ult
    pyxel.rect(80, 230, barreUltA, 10, pyxel.COLOR_YELLOW)
    pyxel.blt(120, 220, 0, 16, 48, 16, 16, 2)
         
    if direction == 1 and ennemi["x"] < player["x"]:
        pyxel.blt(ennemi["x"], ennemi["y"], 0, ennemi["choix_img"], 16, 16, 16, 2)
    elif direction == 1 and ennemi["x"] > player["x"]:
        pyxel.blt(ennemi["x"], ennemi["y"], 0, ennemi["choix_img"], 16, -16, 16, 2) #dessine ennemi
    elif direction == -1 and ennemi["x"] > player["x"]:
        pyxel.blt(ennemi["x"], ennemi["y"], 0, ennemi["choix_img"], 16, -16, 16, 2)
    elif direction == -1 and ennemi["x"] < player["x"]:
        pyxel.blt(ennemi["x"], ennemi["y"], 0, ennemi["choix_img"], 16, 16, 16, 2)
    
    if direction == 1:
        print(player["x"], player["y"], player["choix_img"])
        pyxel.blt(player["x"], player["y"], 0, player["choix_img"],16,16,16, 2) # dessine player
    elif direction == -1:
        pyxel.blt(player["x"], player["y"], 0,player["choix_img"],16,-16,16, 2)
    if sword == 1:
        if direction == 1:
            pyxel.blt(player["x"]+ 8*direction, player["y"]+ 3, 0, attackHitbox["choix_img"], 64, 16, 16, 2) # dessine l'epee (sert a rien on a pas fini
        elif direction == -1:
             pyxel.blt(player["x"]+ 8*direction, player["y"]+ 3, 0, attackHitbox["choix_img"], 64, -16, 16, 2)
    

    
    pyxel.text(8, 16, "CHEVALIER", 10)  #dessine titre en haut a gauche
    pyxel.text(210, 16, f"vague {vague}", 7)  #dessins les vaues d'annemie
    pyxel.text(210, 24, f"level {level}", 15)
    #emplacement d'inventaire du joueur, affiche les items dans des cadres
    pyxel.blt(16, 32, 0, 0, 96, 16, 16, 2)
    pyxel.blt(16, 32, 0, 0, 64, 16, 16, 2)  #affiche les cases ou il devait il y avoir d'autres armes
    pyxel.blt(16, 57, 0, 32, 96, 16, 16, 2)
    pyxel.blt(16, 82, 0, 32, 96, 16, 16, 2)
            
pyxel.run(update, draw)