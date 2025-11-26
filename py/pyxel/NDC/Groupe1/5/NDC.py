import pyxel, random

pyxel.init(128, 128, title="Nuit du Code")

pyxel.load("2.pyxres")

joueur = {"x" : 30, "y" : 97, "direction" : 1, "sens" : 1, "arc": 1, "saut": 0, "choix_img" : 0}
fleches = []
ennemis = [[110, 90, 0, -1, 0], [10, 90, 0, 1, 0], [20, 30, 0, 1, 0]]
tonneau_gauche = {"x" : 2, "y" : 92, "w" : 12, "h" : 20}
tonneau_droit = {"x" : 113, "y" : 99, "w" : 14, "h" : 13}
bloc_milieu_gauche = {"x" : 0, "y" : 72, "w" : 40, "h" : 16}
bloc_milieu_droit = {"x" : 88, "y" : 72, "w" : 40, "h" : 16}
bloc_haut = {"x" : 40, "y" : 32, "w" : 48, "h" : 16}
epee = {"x" : joueur["x"], "y" : joueur["y"], "direction" : joueur["direction"], "sens" : joueur["sens"]}
timer = 0
buff = 0
dist = 12
vitesse_ennemis = 1
vies = 3
son = 0
score = 0
apparition_ennemis = {"x" : 40, "y" : 10, "direction" : 1}
def update():
    global timer, apparition_ennemis, epee, vies, buff, dist, vitesse_ennemis, son, score
    

    if pyxel.btn(pyxel.KEY_RIGHT) and joueur["x"] <= 120:
        joueur["x"] += 1
        joueur["direction"] = 1
        joueur["choix_img"] = ((pyxel.frame_count//3)*16)%64 + 1
    if pyxel.btn(pyxel.KEY_LEFT) and joueur["x"] >= 3:
        joueur["x"] -= 1
        joueur["direction"] = -1
        joueur["choix_img"] = ((pyxel.frame_count//3)*16)%64 + 1
    if pyxel.btnp(pyxel.KEY_DOWN):
        for c in range(len(ennemis)):
            if (joueur["x"] <= ennemis[c][0] + dist and joueur["x"] >= ennemis[c][0] - dist and (ennemis[c][1] <= joueur["y"] + 25 and ennemis[c][1] >= joueur["y"] - 25)):
                ennemis[c][2] = 1
    if pyxel.btnp(pyxel.KEY_UP) and joueur["saut"] == 0:
         joueur["saut"] = 1
         timer = 0
    if joueur["saut"] == 1 and timer < 20:
        joueur["y"] -= 4
        timer += 1
    if joueur["y"] <= 8:
        timer = 20
    if timer == 20:
        joueur["saut"] = 0
        
    
    if pyxel.pget(joueur["x"], joueur["y"] + 15) != pyxel.COLOR_BLACK:
        joueur["y"] += 2
        
    if apparition_ennemis["direction"] == 1:
        apparition_ennemis["x"] += 1
    if apparition_ennemis["x"] < 8 and apparition_ennemis["direction"] == 2:
        apparition_ennemis["direction"] = 1
        
    if apparition_ennemis["x"] > 120:
        apparition_ennemis['direction'] = 2
    if apparition_ennemis["direction"] == 2:
        apparition_ennemis["x"] -= 1

    
            
    for c in range(len(ennemis)):
        if (joueur["x"] <= ennemis[c][0] + 7 and joueur["x"] >= ennemis[c][0] - 7 and ennemis[c][1] <= joueur["y"] + 7 and ennemis[c][1] >= joueur["y"] - 7) and ennemis[c][2] == 0:
            vies -= 1
            ennemis[c][2] = 1

        if pyxel.pget(ennemis[c][0], ennemis[c][1] + 16) != pyxel.COLOR_BLACK:
            ennemis[c][1] += 1
        if ennemis[c][2] == 1:
            ennemis[c][0] = apparition_ennemis["x"]
            ennemis[c][1] = apparition_ennemis["y"]
            ennemis[c][2] = 0
            buff += 1
            score += 100

        if pyxel.frame_count % 150 == 0:
            ennemis[c][4] = random.randint(0, 2)
            
        if ennemis[c][4] == 1:
            ennemis[c][0] += vitesse_ennemis
            ennemis[c][3] = 1
        if ennemis[c][4] == 2:
            ennemis[c][3] = -1
            ennemis[c][0] -= vitesse_ennemis
        if ennemis[c][0] < 3 or ennemis[c][0] > 115 or (pyxel.frame_count % 90 == 0):
            ennemis[c][4] = 0

        
    if buff == 10:
        dist = 25
        vitesse_ennemis = 2

    
    epee = {"x" : joueur["x"], "y" : joueur["y"], "direction" : joueur["direction"], "sens" : joueur["sens"]}
    
    if vies == 0:
        if son == 1:
            
            pyxel.cls(1)
            pyxel.text(42, 50, "Game Over", 7)
            pyxel.playm(0)
            son += 1
    
    if vies >= 1:
        if son == 0:
                pyxel.playm(1)
                son += 1

            
    
def draw():
    if vies >= 1:
        pyxel.cls(2)
        pyxel.bltm(0, 0, 0, 0, 0, 128, 128)
        if joueur["direction"] == 1:
            
            pyxel.blt(joueur["x"], joueur["y"], 0, joueur["choix_img"], 16, 14, 16, 2)
            if dist == 12:
                pyxel.blt(epee["x"]+14, epee["y"]+2, 0, 3, 66, 11, 11, 2)
            if dist == 25:
                pyxel.blt(epee["x"]+14, epee["y"], 0, 16, 65, 15, 14, 2)
                
        elif joueur["direction"] == -1:
            pyxel.blt(joueur["x"], joueur["y"], 0, joueur["choix_img"], 16, -14, 16, 2)
            if dist == 12:    
                pyxel.blt(epee["x"]-10, epee["y"]+2, 0, 3, 66, -11, 11, 2)
            if dist == 25:
                pyxel.blt(epee["x"]-12, epee["y"], 0, 16, 65, -15, 14, 2) 
                
      
        for k in range(len(ennemis)):
            if ennemis[k][3] == 1:
                pyxel.blt(ennemis[k][0], ennemis[k][1], 0, 66, 17, 11, 15, 2)
            if ennemis[k][3] == -1:
                pyxel.blt(ennemis[k][0], ennemis[k][1], 0, 66, 17, -11, 15, 2)
                

    if vies >= 1:
        pyxel.blt(5, 116, 0, 114, 51, 12, 11) #cœur 1
    if vies >= 2:
        pyxel.blt(16, 116, 0, 114, 51, 12, 11) #cœur 2
    if vies == 3:
        pyxel.blt(27, 116, 0, 114, 51, 12, 11) #cœur 3

        

pyxel.run(update, draw)


"""
THE KNIGHT OF PROPHECY
--> Vous êtes un puissant chevalier, protecteur du royaume. Vous êtes cependant attaqué par une attaque ennemie de zombies.
Saurez-vous vous montrer vaillant et survivre face à cette invasion ?

Règles et Déroulement du jeu :
- Les ennemis se déplacent de gauche à droite toutesles 4 secondes.
- Vous commencez avec 3 vies. 
- Si vous vous faites toucher par un ennemi, celui-ci meurt (et donc disparait et réaparaitra quelques secondes plus tard) 
et vous perdez 1 vie sur les 3.
- Au bout de 0 vie, vous avez perdu, un "Game Over" s'affiche. Votre nombre de vies est représenté par le nombre de cœurs 
affichés en bas à droite de l'écran
- Pour éliminer un ennemi vous pouvez le taper à l'épée ou bien lui tirer dessus à l'aide de l'arc (commandes ci-dessous)

Commandes :
Se déplacer : Utilisez les flèches directionnelles (gauche, droite et du haut) pour vous déplacer de gauche à droite et pour sauter
Attaque à l'épée : Utilsez la flèche directionnelle du bas pour attaquer avec votre épée

"""