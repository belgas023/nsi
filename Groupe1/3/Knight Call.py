import pyxel
import random

#initialisation music
music = 1


# initialisation de la fenêtre
pyxel.init(256, 256, "Knight Call", fps=30)
pyxel.load("2.pyxres")

# initialisation de la musique du jeu
music = 1

# position et état du héros
hero_x = 126
hero_y = 200
ismoving_hero = False

# position et état du boss
boss_x = 0
boss_y = 0
boss_vie = 10  # points de vie du boss

# liste des squelettes
squelettes = []

# liste des tirs du joueur [x, y, dx, dy]
tirs = []
dernier_tir_joueur_frame = 0

# liste des projectiles du boss [x, y, dx, dy]
boss_tirs = []
dernier_tir_boss_frame = 0

# statistiques
temps = 0
vies = 3
kills = 0

# phase : "menu", "jeu", "boss", "gameover", "victoire"
phase = "menu"

# disposition clavier : "azerty" ou "qwerty"
clavier = "azerty"

def deplacement_hero():
    global hero_x, hero_y, ismoving_hero
    ismoving_hero = False

    # touches selon la disposition clavier
    if clavier == "azerty":
        haut, bas, gauche, droite = pyxel.KEY_Z, pyxel.KEY_S, pyxel.KEY_Q, pyxel.KEY_D
    else:
        haut, bas, gauche, droite = pyxel.KEY_W, pyxel.KEY_S, pyxel.KEY_A, pyxel.KEY_D

    # si phase boss : uniquement haut/bas
    if phase == "boss":
        if pyxel.btn(haut) and hero_y > 0:
            hero_y -= 2
            ismoving_hero = True
        if pyxel.btn(bas) and hero_y < pyxel.height - 16:
            hero_y += 2
            ismoving_hero = True
    else:
        if pyxel.btn(haut) and hero_y > 0:
            hero_y -= 2
            ismoving_hero = True
        if pyxel.btn(bas) and hero_y < pyxel.height - 16:
            hero_y += 2
            ismoving_hero = True
        if pyxel.btn(gauche) and hero_x > 0:
            hero_x -= 2
            ismoving_hero = True
        if pyxel.btn(droite) and hero_x < pyxel.width - 16:
            hero_x += 2
            ismoving_hero = True

def creer_squelette():
    global temps
    if phase != "jeu":
        return
    if len(squelettes) >= 20:
        return
    intervalle = max(10, 60 - temps * 2)
    if pyxel.frame_count % intervalle == 0:
        bord = random.choice(["haut", "bas", "gauche", "droite"])
        if bord == "haut":
            x = random.randint(0, pyxel.width - 16)
            y = -16
        elif bord == "bas":
            x = random.randint(0, pyxel.width - 16)
            y = pyxel.height
        elif bord == "gauche":
            x = -16
            y = random.randint(0, pyxel.height - 16)
        else:
            x = pyxel.width
            y = random.randint(0, pyxel.height - 16)
        squelettes.append([x, y])

def deplacer_et_collision_squelettes():
    global vies, kills, phase, hero_x, hero_y, boss_x, boss_y
    if phase != "jeu":
        return
    nouveaux = []
    for squelette in squelettes:
        # déplacement vers le héros
        if hero_x > squelette[0]:
            squelette[0] += 0.75
        elif hero_x < squelette[0]:
            squelette[0] -= 0.75
        if hero_y > squelette[1]:
            squelette[1] += 0.75
        elif hero_y < squelette[1]:
            squelette[1] -= 0.75
        # collision
        if abs(hero_x - squelette[0]) < 16 and abs(hero_y - squelette[1]) < 16:
            vies -= 1
            kills += 1
        else:
            nouveaux.append(squelette)
    squelettes[:] = nouveaux

    # passe au boss si 60 kills
    if kills >= 60:
        phase = "boss"
        squelettes.clear()
        tirs.clear()
        boss_tirs.clear()
        boss_x = pyxel.width - 16
        boss_y = pyxel.height // 2
        hero_x = 20
        hero_y = pyxel.height // 2

def deplacer_boss():
    global boss_y
    # le boss suit verticalement le héros à vitesse 1
    if hero_y > boss_y:
        boss_y += 1
    elif hero_y < boss_y:
        boss_y -= 1

def gerer_tirs():
    global dernier_tir_joueur_frame, dernier_tir_boss_frame, vies, boss_vie, kills
    if phase not in ("jeu", "boss"):
        return
    # tirs du boss toutes les 30 frames (1 seconde)
    if phase == "boss" and pyxel.frame_count - dernier_tir_boss_frame >= 30:
        boss_tirs.append([boss_x, boss_y + 8, -1.8, 0])
        dernier_tir_boss_frame = pyxel.frame_count
    # tirs du joueur
    if phase == "boss":
        # en boss, seulement flèche droite
        if pyxel.btnp(pyxel.KEY_RIGHT) and pyxel.frame_count - dernier_tir_joueur_frame >= 10:
            tirs.append([hero_x + 8, hero_y + 8, 1, 0])
            dernier_tir_joueur_frame = pyxel.frame_count
    else:
        # en phase jeu, toutes directions
        if (pyxel.btnp(pyxel.KEY_LEFT) or pyxel.btnp(pyxel.KEY_RIGHT)
           or pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.KEY_DOWN)):
            if pyxel.frame_count - dernier_tir_joueur_frame >= 10:
                if pyxel.btnp(pyxel.KEY_LEFT):
                    tirs.append([hero_x + 8, hero_y + 8, -1, 0])
                if pyxel.btnp(pyxel.KEY_RIGHT):
                    tirs.append([hero_x + 8, hero_y + 8, 1, 0])
                if pyxel.btnp(pyxel.KEY_UP):
                    tirs.append([hero_x + 8, hero_y + 8, 0, -1])
                if pyxel.btnp(pyxel.KEY_DOWN):
                    tirs.append([hero_x + 8, hero_y + 8, 0, 1])
                dernier_tir_joueur_frame = pyxel.frame_count

    # mise à jour et collision des tirs du boss
    nouveaux_boss_tirs = []
    for proj in boss_tirs:
        proj[0] += proj[2]
        proj[1] += proj[3]
        if abs(hero_x - proj[0]) < 16 and abs(hero_y - proj[1]) < 16:
            vies -= 1
        else:
            if 0 <= proj[0] <= pyxel.width and 0 <= proj[1] <= pyxel.height:
                nouveaux_boss_tirs.append(proj)
    boss_tirs[:] = nouveaux_boss_tirs

    # mise à jour et collision des tirs du joueur
    nouveaux_tirs = []
    for tir in tirs:
        tir[0] += tir[2] * 4
        tir[1] += tir[3] * 4
        touche = False
        # collision avec les squelettes
        for squelette in squelettes[:]:
            if abs(tir[0] - squelette[0]) < 16 and abs(tir[1] - squelette[1]) < 16:
                kills += 1
                squelettes.remove(squelette)
                touche = True
        # collision avec le boss
        if phase == "boss" and abs(tir[0] - boss_x) < 16 and abs(tir[1] - boss_y) < 16:
            boss_vie -= 1
            touche = True
        if not touche and 0 <= tir[0] <= pyxel.width and 0 <= tir[1] <= pyxel.height:
            nouveaux_tirs.append(tir)
    tirs[:] = nouveaux_tirs

def reset_jeu():
    global hero_x, hero_y, boss_x, boss_y, boss_vie
    global squelettes, tirs, boss_tirs, temps, vies, kills, phase
    hero_x, hero_y = 126, 200
    boss_x, boss_y = 0, 0
    boss_vie = 10
    squelettes.clear()
    tirs.clear()
    boss_tirs.clear()
    temps = 0
    vies = 3
    kills = 0
    phase = "jeu"

def update():
    global temps, phase, clavier, music
    
    
    if phase == "menu":
        if music == 1:
            pyxel.playm(1,0,True)
            music = 0

        if pyxel.btnp(pyxel.KEY_SPACE):
            reset_jeu()
        if pyxel.btnp(pyxel.KEY_LALT) or pyxel.btnp(pyxel.KEY_RALT):
            clavier = "qwerty" if clavier == "azerty" else "azerty"
        return
    
    
    if phase == "jeu":
        if music == 0:
            pyxel.playm(0,0,True)
            music = 2

        deplacement_hero()
        creer_squelette()
        deplacer_et_collision_squelettes()
        gerer_tirs()
        if vies <= 0:
            phase = "gameover"
        if pyxel.frame_count % 30 == 0:
            temps += 1
        return
    
    
    if phase == "boss":
        if music == 2:
            pyxel.playm(2,0,True)
            music = 3

        deplacement_hero()
        deplacer_boss()
        gerer_tirs()
        if vies <= 0:
            phase = "gameover"
        if boss_vie <= 0:
            phase = "victoire"
        if pyxel.frame_count % 30 == 0:
            temps += 1
        return
    
    
    if phase == "gameover":
        if music == 0 or music == 2 or music == 3:
            pyxel.playm(4,0,True)
            music = 5
        if pyxel.btnp(pyxel.KEY_R):
            reset_jeu()
            music = 0

        if pyxel.btnp(pyxel.KEY_M):
            phase = "menu"
        return
    
    
    if phase == "victoire":
        if pyxel.btnp(pyxel.KEY_R):
            reset_jeu()
        if pyxel.btnp(pyxel.KEY_M):
            phase = "menu"
        return

def draw():
    pyxel.cls(0)
    if phase == "menu":
        pyxel.bltm(0,0,1,0,0,256,256,0)
        pyxel.text(75,110,"Appuie sur ESPACE pour jouer",0)
        pyxel.text(115,60,"Knight Call",0)
        pyxel.text(55,165,"Appuie sur ALT pour changer les touches",0)
        if clavier == "azerty":
            pyxel.text(80,130,"Touches : ZQSD (AZERTY)",0)
        else:
            pyxel.text(80,130,"Touches : WASD (QWERTY)",0)
        return
    
    if phase == "gameover":
        pyxel.text(100,100,"GAME OVER",8)
        pyxel.text(80,120,"Temps final : " + str(temps) + "s",8)
        pyxel.text(80,135,"Kills total : " + str(kills),8)
        pyxel.text(60,165,"Appuie R pour recommencer",8)
        pyxel.text(60,180,"Appuie M pour menu",8)
        return
    
    if phase == "victoire":
        pyxel.text(100,100,"VICTOIRE !",10)
        pyxel.text(80,120,"Temps : " + str(temps) + "s",10)
        pyxel.text(80,135,"Kills : " + str(kills),10)
        pyxel.text(60,165,"Appuie R pour rejouer",10)
        pyxel.text(60,180,"Appuie M pour menu",10)
        return
    
    if phase == "jeu":
        pyxel.bltm(0,0,0,0,0,256,256,0)
        pyxel.text(80,10,"Kills : " + str(kills) + "/60 pour boss",0)
    else:
        # phase boss
        pyxel.text(50,5,"SEULS HAUT/BAS : monter/descendre",0)
        pyxel.text(50,15,"FLÈCHE DROITE : tirer vers la droite",0)
        pyxel.bltm(0,0,2,0,0,256,256,0)
        pyxel.blt(boss_x,boss_y,0,128,16,16,16,2)
        frame_proj = (pyxel.frame_count // 5) % 3
        sprite_proj = 96 + frame_proj * 16
        
        for px,py,_,_ in boss_tirs:
            pyxel.blt(int(px),int(py),0,sprite_proj,80,16,16,2)
    frame_hero = (pyxel.frame_count // 10) % 4 if ismoving_hero else 0
    pyxel.blt(hero_x,hero_y,0,frame_hero*16,16,16,16,2)
    
    
    if phase == "jeu":
        frame_sq = (pyxel.frame_count // 10) % 4
        sprite_sq = frame_sq * 16 + 64
        for sx,sy in squelettes:
            pyxel.blt(sx,sy,0,sprite_sq,16,16,16,2)
    for tx,ty,_,_ in tirs:
        couleur = 3 if phase == "boss" else 8
        pyxel.rect(tx-2,ty-2,4,4,couleur)
    pyxel.text(5,5,"Vies : " + str(vies),0)
    if phase == "boss":
        pyxel.text(190,5,"Boss : " + str(boss_vie),0)
    pyxel.text(204,246,"Temps : " + str(temps) + "s",0)
    pyxel.text(5,246,"Kills : " + str(kills),0)

pyxel.run(update, draw)


