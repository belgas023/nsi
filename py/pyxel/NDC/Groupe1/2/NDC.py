import pyxel
pyxel.init(128,128, fps = 30)
pyxel.load("NDC_Morgan.pyxres")

personnage = {"coordonnée" : [0,30],
              "costume" : 0,
              "direction" : 1}

Blocs = {
    "level_1": {
        "bloc": {
            "bloc_1": {"coordonnée": [0, 104], "pyxres": [0, 104], "taille": [56, 24]},
            "bloc_2": {"coordonnée": [64, 104], "pyxres": [64, 104], "taille": [32, 24]},
            "bloc_3": {"coordonnée": [112, 104], "pyxres": [112, 104], "taille": [16, 24]}
        },
        "portail": {"coordonnée": [120, 93], "pyxres": [120, 93], "taille": [8, 11]}
    },

    "level_2": {
        "bloc": {
            "bloc_1": {"coordonnée": [0, 104], "pyxres": [128, 104], "taille": [16, 24]},
            "bloc_2": {"coordonnée": [32, 104], "pyxres": [152, 104], "taille": [8, 24]},
            "bloc_3": {"coordonnée": [48, 104], "pyxres": [168, 104], "taille": [88, 24]}
        },
        "portail": {"coordonnée": [120, 93], "pyxres": [248, 93], "taille": [8, 11]}
    },

    "level_3": {
        "bloc": {
            "bloc_1": {"coordonnée": [0, 104], "pyxres": [256, 104], "taille": [16, 24]},
            "bloc_2": {"coordonnée": [24, 104], "pyxres": [280, 104], "taille": [8, 24]},
            "bloc_3": {"coordonnée": [48, 104], "pyxres": [296, 104], "taille": [24, 24]},
            "bloc_4": {"coordonnée": [80, 104], "pyxres": [328, 104], "taille": [56, 24]}
        },
        "portail": {"coordonnée": [120, 93], "pyxres": [376, 93], "taille": [8, 11]},
        "pics": {
            "pics_1" : {"coordonnée": [96, 96], "pyxres": [344, 96], "taille": [5, 3]}
            }
    },

    "level_4": {
        "bloc": {
            "bloc_1": {"coordonnée": [0, 104], "pyxres": [384, 104], "taille": [16, 24]},
            "bloc_2": {"coordonnée": [24, 96], "pyxres": [400, 96], "taille": [16, 32]},
            "bloc_3": {"coordonnée": [40, 104], "pyxres": [416, 104], "taille": [16, 24]},
            "bloc_4": {"coordonnée": [56, 96], "pyxres": [432, 96], "taille": [8, 32]},
            "bloc_5": {"coordonnée": [64, 104], "pyxres": [440, 104], "taille": [8, 24]},
            "bloc_6": {"coordonnée": [80, 104], "pyxres": [456, 104], "taille": [56, 24]}
        },
        "portail": {"coordonnée": [120, 93], "pyxres": [504, 93], "taille": [8, 11]},
        "pics": {
            "pics_1": {"coordonnée": [40, 96], "pyxres": [416, 96], "taille": [5, 3]},
            "pics_2": {"coordonnée": [48, 96], "pyxres": [424, 96], "taille": [5, 3]}
        }
    },

    "level_5": {
        "bloc": {
            "bloc_1": {"coordonnée": [0, 104], "pyxres": [512, 104], "taille": [16, 24]},
            "bloc_2": {"coordonnée": [24, 112], "pyxres": [528, 96], "taille": [16, 16]},
            "bloc_3": {"coordonnée": [40, 104], "pyxres": [544, 104], "taille": [16, 24]},
            "bloc_4": {"coordonnée": [64, 104], "pyxres": [568, 96], "taille": [8, 32]},
            "bloc_5": {"coordonnée": [80, 104], "pyxres": [584, 104], "taille": [56, 24]}
        },
        "portail": {"coordonnée": [0, 93], "pyxres": [512, 93], "taille": [8, 11]},
        "clé": {"coordonnée": [120, 93], "pyxres": [632, 96], "taille": [8, 8]},
        "pics": {
            "pics_1": {"coordonnée": [24, 88], "pyxres": [528, 88], "taille": [5, 3]},
            "pics_2": {"coordonnée": [32, 88], "pyxres": [536, 88], "taille": [5, 3]}
        }
    },

    "level_6": {
        "bloc": {
            "bloc_1": {"coordonnée": [0, 104], "pyxres": [640, 104], "taille": [16, 24]},
            "bloc_2": {"coordonnée": [24, 112], "pyxres": [656, 96], "taille": [24, 16]},
            "bloc_3": {"coordonnée": [48, 120], "pyxres": [680, 120], "taille": [24, 8]},
            "bloc_4": {"coordonnée": [88, 120], "pyxres": [720, 120], "taille": [8, 8]},
            "bloc_5": {"coordonnée": [96, 112], "pyxres": [728, 104], "taille": [8, 16]},
            "bloc_6": {"coordonnée": [104, 104], "pyxres": [736, 104], "taille": [32, 24]}
        },
        "portail": {"coordonnée": [120, 93], "pyxres": [760, 93], "taille": [8, 11]},
        "pics": {
            "pics_1": {"coordonnée": [24, 88], "pyxres": [656, 88], "taille": [5, 3]},
            "pics_2": {"coordonnée": [112, 86], "pyxres": [536, 88], "taille": [5, 3]}
        }
    },

    "level_7": {
        "bloc": {
            "bloc_1": {"coordonnée": [0, 104], "pyxres": [768, 104], "taille": [24, 24]},
            "bloc_2": {"coordonnée": [40, 104], "pyxres": [800, 104], "taille": [64, 24]},
            "bloc_3": {"coordonnée": [112, 104], "pyxres": [872, 104], "taille": [8, 24]},
            "bloc_4": {"coordonnée": [128, 104], "pyxres": [888, 104], "taille": [8, 24]}
        },
        "portail": {"coordonnée": [120, 93], "pyxres": [880, 93], "taille": [8, 11]}
    },

    "level_8": {
        "bloc": {
            "bloc_1": {"coordonnée": [0, 104], "pyxres": [896, 104], "taille": [16, 24]},
            "bloc_6": {"coordonnée": [56, 104], "pyxres": [944, 104], "taille": [32, 24]},
            "bloc_7": {"coordonnée": [88, 104], "pyxres": [976, 104], "taille": [8, 8]},
            "bloc_8": {"coordonnée": [96, 104], "pyxres": [984, 104], "taille": [8, 8]},
            "bloc_9": {"coordonnée": [104, 104], "pyxres": [992, 104], "taille": [8, 8]},
            "bloc_10": {"coordonnée": [112, 104], "pyxres": [1000, 104], "taille": [8, 8]},
            "bloc_11": {"coordonnée": [120, 104], "pyxres": [1008, 104], "taille": [16, 24]}
        },
        "blocs_phantom": {
            "blocs_phantom_1": {"coordonnée": [24, 104], "pyxres": [912, 104], "taille": [8, 8]},
            "blocs_phantom_2": {"coordonnée": [32, 104], "pyxres": [920, 104], "taille": [8, 8]},
            "blocs_phantom_3": {"coordonnée": [40, 104], "pyxres": [928, 104], "taille": [8, 8]},
            "blocs_phantom_4": {"coordonnée": [48, 104], "pyxres": [936, 104], "taille": [8, 8]}
        },
        "portail": {"coordonnée": [0, 93], "pyxres": [888, 93], "taille": [8, 11]},
        "clé": {"coordonnée": [120, 93], "pyxres": [1016, 96], "taille": [8, 8]}
    }
}





couleur = 6
level = 1
niveau = (f"level_{level}")
gauche = True
droite = True 
bas = True
haut = True
saut = 0
debut_level = False
temps = 0
mort = False
porte = False

def update():
    
    global personnage, haut, droite, bas, gauche, Blocs, niveau, level, saut, temps, mort, debut_level, fin_jeu, porte
    
    fin_jeu = False
    if level == 9:
        fin_jeu = True
        
    #collision bas
    for bloc in Blocs[niveau]["bloc"]:
        if personnage["coordonnée"][0] + 8 > Blocs[niveau]["bloc"][bloc]["coordonnée"][0] and personnage["coordonnée"][0] < Blocs[niveau]["bloc"][bloc]["coordonnée"][0] + Blocs[niveau]["bloc"][bloc]["taille"][0]:
            if personnage["coordonnée"][1] + 8 >= Blocs[niveau]["bloc"][bloc]["coordonnée"][1] and personnage["coordonnée"][1] + 8 <= Blocs[niveau]["bloc"][bloc]["coordonnée"][1] + Blocs[niveau]["bloc"][bloc]["taille"][1]:
                personnage["coordonnée"][1] = Blocs[niveau]["bloc"][bloc]["coordonnée"][1] - 8
                bas = False
                saut = 0
                break
            else :
                bas = True
        else :
            bas = True
    
    #collision haut
    for bloc in Blocs[niveau]["bloc"] :
        if (Blocs[niveau]["bloc"][bloc]["coordonnée"][0] < (personnage["coordonnée"][0] + 8)) and ((Blocs[niveau]["bloc"][bloc]["coordonnée"][0] + Blocs[niveau]["bloc"][bloc]["taille"][0]) > personnage["coordonnée"][0]) :
            if personnage["coordonnée"][1] +1 - Blocs[niveau]["bloc"][bloc]["taille"][1] == Blocs[niveau]["bloc"][bloc]["coordonnée"][1] :
                haut = False
                break
            else :
                haut = True
        else :
            haut = True
    
    #collision gauche
    for bloc in Blocs[niveau]["bloc"] :
        if (Blocs[niveau]["bloc"][bloc]["coordonnée"][1] < (personnage["coordonnée"][1] + 8)) and ((Blocs[niveau]["bloc"][bloc]["coordonnée"][1] + Blocs[niveau]["bloc"][bloc]["taille"][1]) > personnage["coordonnée"][1]) :
            if personnage["coordonnée"][0] == Blocs[niveau]["bloc"][bloc]["coordonnée"][0] + Blocs[niveau]["bloc"][bloc]["taille"][0] :
                gauche = False
                break
            else :
                gauche = True
        else :
            gauche = True
            
    #collision droite
    for bloc in Blocs[niveau]["bloc"] :
        if (Blocs[niveau]["bloc"][bloc]["coordonnée"][1] < (personnage["coordonnée"][1] + 8)) and ((Blocs[niveau]["bloc"][bloc]["coordonnée"][1] + Blocs[niveau]["bloc"][bloc]["taille"][1]) > personnage["coordonnée"][1]) :
            if personnage["coordonnée"][0] + 8 == Blocs[niveau]["bloc"][bloc]["coordonnée"][0] :
                droite = False
                break
            else :
                droite = True
        else :
            droite = True
    
    
    #déplacement personnage
    if pyxel.btn(pyxel.KEY_RIGHT) and personnage["coordonnée"][0] < 120 and droite == True:
        personnage["coordonnée"][0] += 1
        personnage["direction"] = 1
    elif pyxel.btn(pyxel.KEY_LEFT) and personnage["coordonnée"][0] > 0 and gauche == True:
        personnage["coordonnée"][0] -= 1
        personnage["direction"] = -1
        
    #gravité + saut
    if bas == True and saut == 0:
        personnage["coordonnée"][1] += 3
    
    if bas == False :
        saut = 0
    
    if pyxel.btn(pyxel.KEY_UP) and saut == 0 :
        saut = 1
        temps = pyxel.frame_count
    
    if saut == 1 :
        if pyxel.frame_count - temps < 6 :
            personnage["coordonnée"][1] -= 3
        elif pyxel.frame_count - temps < 9 :
            personnage["coordonnée"][1] -= 2
        elif pyxel.frame_count - temps <= 11 :
            personnage["coordonnée"][1] -= 1
        else :
            saut = 2
    elif saut == 2 and bas == True :
        if pyxel.frame_count - temps < 13 :
            personnage["coordonnée"][1] += 1
        elif pyxel.frame_count - temps < 16 :
            personnage["coordonnée"][1] += 2
        elif pyxel.frame_count - temps <= 22 :
            personnage["coordonnée"][1] += 3
        else :
            saut = 3
    if saut == 3 :
        if bas == True :
            personnage["coordonnée"][1] += 3
        else :
            saut = 0

    #changement de costume
    if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_LEFT) :
        personnage["costume"] = pyxel.frame_count//3%4
    elif saut == 1 or saut == 2 :
        personnage["costume"] = 4
    else :
        personnage["costume"] = 0
    
    

        
    
    #codage de la mort du perso
    if personnage["coordonnée"][1] > 130:
        mort = True
    

    if "pics" in Blocs[niveau] :
        for pic in Blocs[niveau]["pics"]:
            if (Blocs[niveau]["pics"][pic]["coordonnée"][0] < personnage["coordonnée"][0] + 8) and (Blocs[niveau]["pics"][pic]["coordonnée"][0] + Blocs[niveau]["pics"][pic]["taille"][0] > personnage["coordonnée"][0]) and \
               (Blocs[niveau]["pics"][pic]["coordonnée"][1] < personnage["coordonnée"][1] + 8) and (Blocs[niveau]["pics"][pic]["coordonnée"][1] + Blocs[niveau]["pics"][pic]["taille"][1] > personnage["coordonnée"][1]):
                mort = True
                debut_level = True 



    
    if mort :
        debut_level = True
    
    
    if debut_level:
        if niveau == 1:
            porte = True
            personnage["coordonée"][0] = 0
            personnage["coordonée"][1] = 30
            debut_level = False
            mort = False
            
        elif niveau == 2:
            porte = True 
            personnage["coordonée"][0] = 0
            personnage["coordonée"][1] = 30
            debut_level = False
            mort = False
            
        elif niveau == 3:
            porte = True 
            personnage["coordonée"][0] = 0
            personnage["coordonée"][1] = 30
            debut_level = False
            mort = False
            
        elif niveau == 4:
            porte = True 
            personnage["coordonée"][0] = 0
            personnage["coordonée"][1] = 30
            debut_level = False
            mort = False
            
        elif niveau == 5:
            porte = False
            personnage["coordonée"][0] = 0
            personnage["coordonée"][1] = 30
            debut_level = False
            mort = False
            
        elif niveau == 6:
            porte = True 
            personnage["coordonée"][0] = 0
            personnage["coordonée"][1] = 30
            debut_level = False
            mort = False
            
        elif niveau == 7:
            porte = True 
            personnage["coordonée"][0] = 0
            personnage["coordonée"][1] = 30
            debut_level = False
            mort = False
            
        elif niveau == 8:
            porte = False 
            personnage["coordonée"][0] = 0
            personnage["coordonée"][1] = 30
            debut_level = False
            mort = False
            
        elif niveau == 9:
            porte = True 
            personnage["coordonée"][0] = 0
            personnage["coordonée"][1] = 30
            debut_level = False
            mort = False

    
    #collision avec clé
    if "clé" in Blocs[niveau] :
        if (Blocs[niveau]["clés"]["clé_1"]["coordonnée"][0] < personnage["coordonnée"][0] + 8) and \
            (Blocs[niveau]["clés"]["clé_1"]["coordonnée"][0] + Blocs[niveau]["clés"]["clé_1"]["taille"][0] > personnage["coordonnée"][0]) and \
            (Blocs[niveau]["clés"]["clé_1"]["coordonnée"][1] < personnage["coordonnée"][1] + 8) and \
            (Blocs[niveau]["clés"]["clé_1"]["coordonnée"][1] + Blocs[niveau]["clés"]["clé_1"]["taille"][1] > personnage["coordonnée"][1]):
                porte = True
    
    #collision avec la porte

    if Blocs[niveau]["portail"]["coordonnée"][0] <= personnage["coordonnée"][0] + 8 and personnage["coordonnée"][0] <= Blocs[niveau]["portail"]["coordonnée"][0] + Blocs[niveau]["portail"]["taille"][0] :
        if Blocs[niveau]["portail"]["coordonnée"][1] <= personnage["coordonnée"][1] + 8 and personnage["coordonnée"][1] <= Blocs[niveau]["portail"]["coordonnée"][1] + Blocs[niveau]["portail"]["taille"][1] :
            level += 1
            print(niveau)
            debut_level = True
            print("ok")
            porte = False


    niveau = (f"level_{level}")

        
        
            
    
            
    
def draw():
    pyxel.cls(couleur)
    for bloc in Blocs[niveau]["bloc"] :
        pyxel.bltm(Blocs[niveau]["bloc"][bloc]["coordonnée"][0], Blocs[niveau]["bloc"][bloc]["coordonnée"][1], 0, Blocs[niveau]["bloc"][bloc]["pyxres"][0], Blocs[niveau]["bloc"][bloc]["pyxres"][1], Blocs[niveau]["bloc"][bloc]["taille"][0], Blocs[niveau]["bloc"][bloc]["taille"][1])
    if "pics" in Blocs[niveau] :
        for pic in Blocs[niveau]["pics"] : 
            pyxel.blt(Blocs[niveau]["pics"][pic]["coordonnée"][0], Blocs[niveau]["pics"][pic]["coordonnée"][1], 0, Blocs[niveau]["pics"][pic]["pyxres"][0], Blocs[niveau]["pics"][pic]["pyxres"][1], Blocs[niveau]["pics"][pic]["taille"][0], Blocs[niveau]["pics"][pic]["taille"][1], 5)    
    
    if "clé" in Blocs[niveau] :
        pyxel.bltm(Blocs[niveau]["clé"]["clé_1"]["coordonnée"][0], Blocs[niveau]["clé"]["clé_1"]["coordonnée"][1], 0, Blocs[niveau]["clé"]["clé_1"]["pyxres"][0], Blocs[niveau]["clé"]["clé_1"]["pyxres"][1], Blocs[niveau]["clé"]["clé_1"]["taille"][0], Blocs[niveau]["clé"]["clé_1"]["taille"][1], 5)
    pyxel.bltm(Blocs[niveau]["portail"]["coordonnée"][0], Blocs[niveau]["portail"]["coordonnée"][1], 0, Blocs[niveau]["portail"]["pyxres"][0], Blocs[niveau]["portail"]["pyxres"][1], Blocs[niveau]["portail"]["taille"][0], Blocs[niveau]["portail"]["taille"][1], 5)
    pyxel.blt(personnage["coordonnée"][0], personnage["coordonnée"][1], 0, personnage["costume"]*8, 56, personnage["direction"]*8, 8, 5)
    
    if fin_jeu:
        pyxel.cls(0)
        pyxel.text(30, 60, "Maybe next time ;)", 6)




pyxel.run(update, draw)
