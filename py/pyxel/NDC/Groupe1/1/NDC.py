import pyxel
import random

pyxel.init(256,256,title='NDC',fps=30)

pyxel.load("2.pyxres")

perso={"x":80,"y":220,"vitesse":4,"niveau":1,"vie":10,"aimant":10,"img":0,"timer":40}

atk={"x":100,"y":100,"visible":False,"dirx":0,"diry":0,"vitesse":2,"portée":30,"repousse":5}

objet={"x":0,"y":0,"visible":True,"niveau":1, "nom" : "rien"}

portail={"x":251,"y":15}

bonus=[]

bonusmax=["supervitesse","longshoot","speedball","maxirepousse","trou noir","aimanté"]

pyxel.mouse(True)
music=0

if perso["niveau"] == 4:
    pyxel.playm(0, loop=True)

pièce = [{"x":45, "y" :205, "visible" : True, "niveau":1,"img":1},
         {"x":42, "y" :21, "visible" : True, "niveau":1,"img":2},
         {"x":245, "y" :206, "visible" : True, "niveau":1,"img":1},
         {"x":213, "y" :110, "visible" : True, "niveau":1,"img":3},
         {"x":155, "y" :147, "visible" : True, "niveau":1,"img":1},
         {"x":175, "y" :220, "visible" : True, "niveau":2,"img":2},
         {"x":236, "y" :194, "visible" : True, "niveau":2,"img":2},
         {"x":39, "y" :219, "visible" : True, "niveau":2,"img":1},
         {"x":87, "y" :59, "visible" : True, "niveau":2,"img":2},
         {"x":198, "y" :79, "visible" : True, "niveau":2,"img":1},
         {"x":31, "y" :240, "visible" : True, "niveau":3,"img":3},
         {"x":114, "y" :240, "visible" : True, "niveau":3,"img":1},
         {"x":200, "y" :240, "visible" : True, "niveau":3,"img":2},
         {"x":72, "y" :15, "visible" : True, "niveau":3,"img":3},
         {"x":152, "y" :15, "visible" : True, "niveau":3,"img":1},
         ]

ennemies = [{"x":45, "y" :120, "niveau":1,"vitesse":1,"img":1},
            {"x":42, "y" :21, "niveau":1,"vitesse":1.2,"img":1},
            {"x":245, "y" :187, "niveau":1,"vitesse":2.0,"img":1},
            {"x":101, "y" :15, "niveau":2,"vitesse":1.5,"img":1},
            {"x":174, "y" :161, "niveau":2,"vitesse":1.4,"img":1},
            {"x":111, "y" :239, "niveau":2,"vitesse":1.9,"img":1},
            {"x":10, "y" :170, "niveau":3,"vitesse":1.35,"img":1},
            {"x":176, "y" :170, "niveau":3,"vitesse":1.55,"img":1},
            {"x":128, "y" :128, "niveau":4,"vitesse":2.7,"img":2},
            ]

def ajout_item():
    bonus.append(objet.copy())
    objet["visible"]=False
    objet["niveau"]+=1

def gestion_bonus():
    global objet
    if pyxel.frame_count % 250 == 0 and objet["niveau"]==perso["niveau"]:
        objet={"x":8 *random.randint(0,32),"y":8 *random.randint(0,32),"visible":True,"nom":random.choice(bonusmax),"niveau":objet["niveau"]}
    if distance(perso,objet)<perso["aimant"] and objet["visible"]:
        if len(bonus)==0:
            ajout_item()
        else:
            for i in bonus:
                compteur=0
                if i["nom"]!=objet["nom"]:
                    compteur+=1
                if compteur==len(bonus):
                    ajout_item()

def appliquer_bonus():
    souris={"x":pyxel.mouse_x,"y":pyxel.mouse_y}
    perso["vitesse"]=3
    perso["aimant"]=8
    atk["portée"]=45
    atk["vitesse"]=3
    atk["repousse"]=4
    
    for i in bonus:
        if i["nom"] == "supervitesse":
            perso["vitesse"]=5
        if i["nom"] == "longshoot":
            atk["portée"]=85
        if i["nom"] == "speedball":
            atk["vitesse"]=4
        if i["nom"] == "maxirepousse":
            atk["repousse"]=15
        if i["nom"] == "trou noir" and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            for i in ennemies:
                if distance(i,souris) < 30:
                    i["x"]=souris["x"]
                    i["y"]=souris["y"]
        if i["nom"] == "aimanté":
            perso["aimant"]=24

def distance(a,b): # a et b sont des dictionnaires
    return ((a["x"]-b["x"])**2+(a["y"]-b["y"])**2)**(1/2)
    
def shoot():
    if distance(perso,atk)> atk["portée"]:
        atk["visible"]=False
    if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and not atk["visible"]:
        atk["x"]=perso["x"]
        atk["y"]=perso["y"]
        atk["visible"]=True
        atk["dirx"]=(pyxel.mouse_x-atk["x"])/max(abs(atk["x"]-pyxel.mouse_x),abs(atk["y"]-pyxel.mouse_y),1)
        atk["diry"]=(pyxel.mouse_y-atk["y"])/max(abs(atk["x"]-pyxel.mouse_x),abs(atk["y"]-pyxel.mouse_y),1)
    atk["x"]+=atk["dirx"]*atk["vitesse"]
    atk["y"]+=atk["diry"]*atk["vitesse"]
    
def mooving():
    liste=[pyxel.KEY_UP,pyxel.KEY_DOWN,pyxel.KEY_LEFT,pyxel.KEY_RIGHT]
    for i in liste:
        if pyxel.btn(i):
            return True
    return False

def action():
    if pyxel.btn(pyxel.KEY_UP) and pyxel.pget(perso["x"],perso["y"]-perso["vitesse"]-4) != 13:
        if perso["y"] > 8:
            perso["y"] -= perso["vitesse"]
    if pyxel.btn(pyxel.KEY_DOWN) and pyxel.pget(perso["x"],perso["y"]+perso["vitesse"]+6) != 13:
        if perso["y"] < 256-perso["vitesse"]-8:
            perso["y"] += perso["vitesse"]
    if pyxel.btn(pyxel.KEY_RIGHT) and pyxel.pget(perso["x"]+perso["vitesse"]+4,perso["y"]) != 13:
        if perso["x"] < 256-perso["vitesse"]-8:
            perso["x"] += perso["vitesse"]
    if pyxel.btn(pyxel.KEY_LEFT) and pyxel.pget(perso["x"]-perso["vitesse"]-4,perso["y"]) != 13:
        if perso["x"] > 5:
            perso["x"] -= perso["vitesse"]
    if mooving():
        if pyxel.frame_count % 7 == 0:
            perso["img"]= (perso["img"]+1 )% 4
    else:
        perso["img"]=0

def gestion_ennemies():
    for i in ennemies:
        if i["niveau"] == perso["niveau"]:
            if atk["visible"] and distance(i,atk)<8:
                i["x"]+=atk["dirx"]*atk["repousse"]
                i["y"]+=atk["diry"]*atk["repousse"]
            if distance(i, perso)<65:
                i["x"]+=(i["vitesse"]*(perso["x"]-i["x"]))/max(abs(perso["x"]-i["x"]),abs(perso["y"]-i["y"]),1)
                i["y"]+=(i["vitesse"]*(perso["y"]-i["y"]))/max(abs(perso["x"]-i["x"]),abs(perso["y"]-i["y"]),1)
            if distance(perso,i)<8 and pyxel.frame_count % 20 == 0:
                perso["vie"]-=1
            i["x"]=max(min(i["x"],256),0)
            i["y"]=max(min(i["y"],256),0)
            
            if i["img"]==2:
              if not mooving() and perso["timer"] < 30 and pyxel.frame_count % 30 == 0:
                  i["x"]=perso["x"]
                  i["y"]=perso["y"]
    if perso["niveau"]==4 and pyxel.frame_count % 30 == 0:
        perso["timer"]-=1
        if perso["timer"]==0:
            ennemies[-1]["vitesse"]=0
            perso["niveau"] += 1


def level_up():
    perso["niveau"]+=1
    perso["x"]=4
    perso["y"]=15
    for i in pièce:
        i["visible"]=True
    if perso["niveau"]==4:
        perso["timer"]==40

def gestion_piece():
    compteur=0
    for i in pièce:
        if distance(i,perso)<perso["aimant"]:
            i["visible"]=False
        if not i["visible"] or i["niveau"] != perso["niveau"]:
            compteur+=1
        if pyxel.frame_count % 4 == 0:
            i["img"] = (i["img"]+1) % 3
    if compteur==len(pièce):
        if distance(perso,portail)<20:
            level_up()

def update():
    global music
    if perso["niveau"] < 5:
        appliquer_bonus()
        gestion_bonus()
    gestion_piece()
    gestion_ennemies()
    action()
    shoot()
    if perso["niveau"] == 4 and music==0:
        music=1
        pyxel.playm(0, loop=True)
    

def draw():
    if perso["niveau"] != 4:
        pyxel.cls(0)
    else:
        pyxel.cls((pyxel.frame_count//5)%16)
        pyxel.text(120,214,f"Il vous reste {str(perso['timer'])} a tenir",7)

    
    if perso["niveau"] == 1:
        pyxel.bltm(0, 0, 0, 0, 0, 256, 256, 2)
    if perso["niveau"] == 2:
        pyxel.bltm(0, 0, 0, 0, 256, 256, 256, 2)
    if perso["niveau"] == 3:
        pyxel.bltm(0, 0, 0, 0, 512, 256, 256, 2)
    if perso["niveau"] == 4:
        pyxel.bltm(0, 0, 0, 0, 768, 256, 256, 2)
    if perso["niveau"] == 5:
        pyxel.bltm(0, 0, 0, 0, 1280, 256, 256, 2)
    
    pyxel.blt(perso['x']-8,perso['y']-8, 0, 16*perso["img"], 16, 16, 16, 2)
    if atk["visible"]:
        pyxel.blt(atk['x']-8,atk['y']-8, 0, 0, 80, 16, 16, 2)
    if objet["visible"]:
        pyxel.blt(objet['x']-8,objet['y']-8, 0, 32, 96, 16, 16, 2)
    
    if perso["niveau"]<4:
        pyxel.blt(portail["x"]-8,portail["y"]-8,0, 128, 48, 16, 16, 2)
    
    for i in pièce:
        if i["visible"] and i["niveau"] == perso["niveau"]:
            pyxel.blt(i["x"], i["y"], 0, 36+i["img"]*16, 52, 8, 8, 2)
    for j in ennemies:
        if j["niveau"]==perso["niveau"]:
            if j["img"]==1:
                pyxel.blt(j["x"]-8, j["y"]-8, 0, 64, 16, 16, 16, 2)
            else:
                pyxel.blt(j["x"]-8, j["y"]-8, 0, 128, 16, 16, 16, 2)
    for k in range(perso["vie"]):
        pyxel.blt(k*16,0,0,112,48,16,16,2)
    
    if perso["vie"] < 1:
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 1024, 512, 512, 2)
        pyxel.show()

pyxel.run(update,draw)

""" Bienvenu dans le jeu ArgentMax
Vous êtes un aventurier dans une maison hanté. Vous avez vu dans un journal que cette maison regorgait de trésors,
vous y êtes donc allé pour gagner beaucoup d'argent. En franchissant la porte d'entré, vous avez perdu connaissance,
vous vous réveillez dans une pièce dans la maison. Vous pouvez vous déplacer avec les flèches directionnelles, vous
devez rentrer chez vous, mais pour cela, vous êtes contraint de récupérer toute les pièces de la pièce avant
d'acceder à la pièce suivante, attention aux squellettes pouvant léviter, passer à travers les murs et qui vous
foncent dessus.
Il vous font des dếgats et si vos vies décendent à 0, vous mouriez.
Pour vous défendre, faites un clique droit sur la souris, les squellettes seront repoussés et ne peuvent être tués.
Vous pouvez aussi récupérer des pouvoirs dans des boites bonus afin de mieux vous défendre.
Vous pouvez aller plus vite, avoir un projectiles qui va plus vite, un projectile plus rapide, une capacité à
repousser les ennemis améliorée, vous pouvez attirer les ennemis à un endroit précis ou avoir un aimant.
Pour les utiliser, utiliser la touche gauche de votre souris.
Faites attention à l'antagoniste final Bonne chance."""


