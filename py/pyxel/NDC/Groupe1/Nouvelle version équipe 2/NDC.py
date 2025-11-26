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
            "portail": {"coordonnée": [120, 93], "pyxres": [8,101], "taille": [8, 11]}
    },

    "level_2": {
        "bloc": {
            "bloc_1": {"coordonnée": [0, 104], "pyxres": [128, 104], "taille": [16, 24]},
            "bloc_2": {"coordonnée": [32, 104], "pyxres": [152, 104], "taille": [8, 24]},
            "bloc_3": {"coordonnée": [48, 104], "pyxres": [168, 104], "taille": [88, 24]}
        },
        "portail": {"coordonnée": [120, 93], "pyxres": [8,101], "taille": [8, 11]}
    },

    "level_3": {
        "bloc": {
            "bloc_1": {"coordonnée": [0, 104], "pyxres": [256, 104], "taille": [16, 24]},
            "bloc_2": {"coordonnée": [24, 104], "pyxres": [280, 104], "taille": [8, 24]},
            "bloc_3": {"coordonnée": [48, 104], "pyxres": [296, 104], "taille": [24, 24]},
            "bloc_4": {"coordonnée": [80, 104], "pyxres": [328, 104], "taille": [56, 24]}
        },
        "portail": {"coordonnée": [120, 93], "pyxres": [8,101], "taille": [8, 11]},
        "pics": {
            "pics_1" : {"coordonnée": [91, 101], "pyxres": [346, 101], "taille": [5, 3]}
            }
    },

    "level_4": {
        "bloc": {
            "bloc_1": {"coordonnée": [0, 104], "pyxres": [384, 104], "taille": [16, 24]},
            "bloc_2": {"coordonnée": [16, 96], "pyxres": [400, 96], "taille": [16, 32]},
            "bloc_3": {"coordonnée": [32, 104], "pyxres": [416, 104], "taille": [16, 24]},
            "bloc_4": {"coordonnée": [48, 96], "pyxres": [432, 96], "taille": [8, 32]},
            "bloc_5": {"coordonnée": [56, 104], "pyxres": [440, 104], "taille": [8, 24]},
            "bloc_6": {"coordonnée": [72, 104], "pyxres": [456, 104], "taille": [56, 24]}
        },
        "portail": {"coordonnée": [120, 93], "pyxres": [8,101], "taille": [8, 11]},
        "pics": {
            "pics_1": {"coordonnée": [34, 101], "pyxres": [416, 96], "taille": [5, 3]},
            "pics_2": {"coordonnée": [42, 101], "pyxres": [424, 96], "taille": [5, 3]}
        }
    },

    "level_5": {
        "bloc": {
            "bloc_1": {"coordonnée": [0, 104], "pyxres": [512, 104], "taille": [16, 24]},
            "bloc_2": {"coordonnée": [16, 112], "pyxres": [528, 112], "taille": [16, 16]},
            "bloc_3": {"coordonnée": [32, 104], "pyxres": [544, 104], "taille": [16, 24]},
            "bloc_4": {"coordonnée": [72, 104], "pyxres": [584, 104], "taille": [56, 24]}
        },
        "portail": {"coordonnée": [0, 93], "pyxres": [16,101], "taille": [8, 11]},
        "clé": {"coordonnée": [120, 93], "pyxres": [632, 96], "taille": [8, 8]},
        "pics": {
            "pics_1": {"coordonnée": [18, 109], "pyxres": [528, 88], "taille": [5, 3]},
            "pics_2": {"coordonnée": [26, 109], "pyxres": [536, 88], "taille": [5, 3]}
            },
        "clé" : {"coordonnée" : [120, 96], "pyxres" : [632,96], "taille" : [8, 8]}
    },

    "level_6": {
        "bloc": {
            "bloc_1": {"coordonnée": [0, 104], "pyxres": [640, 104], "taille": [16, 24]},
            "bloc_2": {"coordonnée": [16, 112], "pyxres": [656, 112], "taille": [24, 16]},
            "bloc_3": {"coordonnée": [40, 120], "pyxres": [680, 120], "taille": [24, 8]},
            "bloc_4": {"coordonnée": [80, 120], "pyxres": [720, 120], "taille": [8, 8]},
            "bloc_5": {"coordonnée": [88, 112], "pyxres": [728, 112], "taille": [8, 16]},
            "bloc_6": {"coordonnée": [96, 104], "pyxres": [736, 104], "taille": [32, 24]}
        },
        "portail": {"coordonnée": [120, 93], "pyxres": [8,101], "taille": [8, 11]},
        "pics": {
            "pics_1": {"coordonnée": [24, 109], "pyxres": [664, 88], "taille": [5, 3]},
            "pics_2": {"coordonnée": [50, 117], "pyxres": [636, 88], "taille": [5, 3]},
            "pics_3": {"coordonnée": [98, 101], "pyxres": [736, 88], "taille": [5, 3]},
            "pics_4": {"coordonnée": [105, 101], "pyxres": [736, 88], "taille": [5, 3]}
        }
    },

    "level_7": {
        "bloc": {
            "bloc_1": {"coordonnée": [0, 104], "pyxres": [768, 104], "taille": [24, 24]},
            "bloc_2": {"coordonnée": [32, 104], "pyxres": [800, 104], "taille": [32, 24]},
            "bloc_3": {"coordonnée": [64, 104], "pyxres": [832, 104], "taille": [32, 24]},
            "bloc_4": {"coordonnée": [104, 104], "pyxres": [872, 104], "taille": [8, 24]},
            "bloc_5": {"coordonnée": [120, 104], "pyxres": [888, 104], "taille": [8, 24]}
        },
        "portail": {"coordonnée": [120, 93], "pyxres": [8,101], "taille": [8, 11]}
    },

    "level_8": {
        "bloc": {
            "bloc_1": {"coordonnée": [0, 104], "pyxres": [896, 104], "taille": [16, 24]},
            "bloc_2": {"coordonnée": [48, 104], "pyxres": [944, 104], "taille": [32, 24]},
            "bloc_3": {"coordonnée": [112, 104], "pyxres": [1008, 104], "taille": [16, 24]},
            "blocs_phantom_1": {"coordonnée": [16, 104], "pyxres": [912, 104], "taille": [8, 8]},
            "blocs_phantom_2": {"coordonnée": [24, 104], "pyxres": [920, 104], "taille": [8, 8]},
            "blocs_phantom_3": {"coordonnée": [32, 104], "pyxres": [928, 104], "taille": [8, 8]},
            "blocs_phantom_4": {"coordonnée": [40, 104], "pyxres": [936, 104], "taille": [8, 8]},
            "blocs_phantom_5": {"coordonnée": [80, 104], "pyxres": [976, 104], "taille": [8, 8]},
            "blocs_phantom_6": {"coordonnée": [88, 104], "pyxres": [984, 104], "taille": [8, 8]},
            "blocs_phantom_7": {"coordonnée": [96, 104], "pyxres": [992, 104], "taille": [8, 8]},
            "blocs_phantom_8": {"coordonnée": [104, 104], "pyxres": [1000, 104], "taille": [8, 8]}
            },
        "portail": {"coordonnée": [0, 93], "pyxres": [16,101], "taille": [8, 11]},
        "clé": {"coordonnée": [120, 93], "pyxres": [1016, 96], "taille": [8, 8]}
            }
        
        }
        







couleur = 6
level = 5
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
clé = False
fin_jeu = False
temps_blc = 0
g = False


def update():
    
    global personnage, haut, droite, bas, gauche, Blocs, niveau, level, saut, temps, mort, debut_level, fin_jeu, porte, clé, temps_blc, g
    if fin_jeu == False :
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
        if "blocs_phantom" in bloc and bas == False:
            del Blocs[niveau]["bloc"][bloc]
        
        
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
        
        if pyxel.btnp(pyxel.KEY_UP) and saut == 0 :
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
        
        #initialisation debut niveau
        if debut_level:
            personnage["coordonnée"] = [0, 80]
            debut_level = False
            mort = False
            porte = (level not in [5, 8])
            clé = False
            if "clé" in Blocs[niveau] :
                Blocs[niveau]["portail"]["pyxres"][0] = 16
            
            if level == 1 :
                Blocs[niveau] = {
                    "bloc": {
                        "bloc_1": {"coordonnée": [0, 104], "pyxres": [0, 104], "taille": [56, 24]},
                        "bloc_2": {"coordonnée": [64, 104], "pyxres": [64, 104], "taille": [32, 24]},
                        "bloc_3": {"coordonnée": [112, 104], "pyxres": [112, 104], "taille": [16, 24]}
                    },
                    "portail": {"coordonnée": [120, 93], "pyxres": [8,101], "taille": [8, 11]}
                }
            elif level == 2 :
                Blocs[niveau] = {
                    "bloc": {
                        "bloc_1": {"coordonnée": [0, 104], "pyxres": [128, 104], "taille": [16, 24]},
                        "bloc_2": {"coordonnée": [32, 104], "pyxres": [152, 104], "taille": [8, 24]},
                        "bloc_3": {"coordonnée": [48, 104], "pyxres": [168, 104], "taille": [88, 24]}
                    },
                    "portail": {"coordonnée": [120, 93], "pyxres": [8,101], "taille": [8, 11]}
                }
                g = False
            elif level == 3 :
                Blocs["level_3"] =  {
                    "bloc": {
                        "bloc_1": {"coordonnée": [0, 104], "pyxres": [256, 104], "taille": [16, 24]},
                        "bloc_2": {"coordonnée": [24, 104], "pyxres": [280, 104], "taille": [8, 24]},
                        "bloc_3": {"coordonnée": [48, 104], "pyxres": [296, 104], "taille": [24, 24]},
                        "bloc_4": {"coordonnée": [80, 104], "pyxres": [328, 104], "taille": [56, 24]}
                    },
                    "portail": {"coordonnée": [120, 93], "pyxres": [8,101], "taille": [8, 11]},
                    "pics": {
                        "pics_1" : {"coordonnée": [91, 101], "pyxres": [346, 101], "taille": [5, 3]}
                        }
                }
                g = False
            
            elif level == 4 :
                Blocs[niveau] = {
                    "bloc": {
                        "bloc_1": {"coordonnée": [0, 104], "pyxres": [384, 104], "taille": [16, 24]},
                        "bloc_2": {"coordonnée": [16, 96], "pyxres": [400, 96], "taille": [16, 32]},
                        "bloc_3": {"coordonnée": [32, 104], "pyxres": [416, 104], "taille": [16, 24]},
                        "bloc_4": {"coordonnée": [48, 96], "pyxres": [432, 96], "taille": [8, 32]},
                        "bloc_5": {"coordonnée": [56, 104], "pyxres": [440, 104], "taille": [8, 24]},
                        "bloc_6": {"coordonnée": [72, 104], "pyxres": [456, 104], "taille": [56, 24]}
                    },
                    "portail": {"coordonnée": [120, 93], "pyxres": [8,101], "taille": [8, 11]},
                    "pics": {
                        "pics_1": {"coordonnée": [34, 101], "pyxres": [416, 96], "taille": [5, 3]},
                        "pics_2": {"coordonnée": [42, 101], "pyxres": [424, 96], "taille": [5, 3]}
                    }
                }
            elif level == 7 :
                Blocs[niveau] = {
                    "bloc": {
                        "bloc_1": {"coordonnée": [0, 104], "pyxres": [768, 104], "taille": [24, 24]},
                        "bloc_2": {"coordonnée": [32, 104], "pyxres": [800, 104], "taille": [32, 24]},
                        "bloc_3": {"coordonnée": [64, 104], "pyxres": [832, 104], "taille": [32, 24]},
                        "bloc_4": {"coordonnée": [104, 104], "pyxres": [872, 104], "taille": [8, 24]},
                        "bloc_5": {"coordonnée": [120, 104], "pyxres": [888, 104], "taille": [8, 24]}
                    },
                    "portail": {"coordonnée": [120, 93], "pyxres": [8,101], "taille": [8, 11]}
                }
                
                
            elif level == 8 :
                Blocs[niveau] = {
                    "bloc": {
                        "bloc_1": {"coordonnée": [0, 104], "pyxres": [896, 104], "taille": [16, 24]},
                        "bloc_2": {"coordonnée": [48, 104], "pyxres": [944, 104], "taille": [32, 24]},
                        "bloc_3": {"coordonnée": [112, 104], "pyxres": [1008, 104], "taille": [16, 24]},
                        "blocs_phantom_1": {"coordonnée": [16, 104], "pyxres": [912, 104], "taille": [8, 8]},
                        "blocs_phantom_2": {"coordonnée": [24, 104], "pyxres": [920, 104], "taille": [8, 8]},
                        "blocs_phantom_3": {"coordonnée": [32, 104], "pyxres": [928, 104], "taille": [8, 8]},
                        "blocs_phantom_4": {"coordonnée": [40, 104], "pyxres": [936, 104], "taille": [8, 8]},
                        "blocs_phantom_5": {"coordonnée": [80, 104], "pyxres": [976, 104], "taille": [8, 8]},
                        "blocs_phantom_6": {"coordonnée": [88, 104], "pyxres": [984, 104], "taille": [8, 8]},
                        "blocs_phantom_7": {"coordonnée": [96, 104], "pyxres": [992, 104], "taille": [8, 8]},
                        "blocs_phantom_8": {"coordonnée": [104, 104], "pyxres": [1000, 104], "taille": [8, 8]}
                        },
                    "portail": {"coordonnée": [0, 93], "pyxres": [16,101], "taille": [8, 11]},
                    "clé": {"coordonnée": [120, 93], "pyxres": [1016, 96], "taille": [8, 8]}
                    }
        
            elif level == 9 :
                fin_jeu = True
        
        #mouvement bloc niveau
        if level == 2:
            if personnage["coordonnée"][0] == 16 and not g:
                temps_blc = pyxel.frame_count
                g = True
                
            if g : 
                if pyxel.frame_count - temps_blc <= 16 :
                    Blocs[niveau]["bloc"]["bloc_2"]["coordonnée"][0] -= 1
        
        elif level == 3 :
            if personnage["coordonnée"][0] == 16 and not g:
                temps_blc = pyxel.frame_count
                g = True
            if g : 
                if pyxel.frame_count - temps_blc <= 7 :
                    Blocs[niveau]["bloc"]["bloc_2"]["coordonnée"][0] += 2
                elif pyxel.frame_count - temps_blc <= 18 :
                    Blocs[niveau]["bloc"]["bloc_2"]["coordonnée"][0] -= 2
            
        elif level == 4 :
            if personnage["coordonnée"][0] == 76 :
                Blocs[niveau] = {
                    "bloc": {
                        "bloc_1": {"coordonnée": [0, 104], "pyxres": [384, 104], "taille": [16, 24]},
                        "bloc_2": {"coordonnée": [16, 96], "pyxres": [400, 96], "taille": [16, 32]},
                        "bloc_3": {"coordonnée": [32, 104], "pyxres": [416, 104], "taille": [16, 24]},
                        "bloc_4": {"coordonnée": [48, 96], "pyxres": [432, 96], "taille": [8, 32]},
                        "bloc_5": {"coordonnée": [56, 104], "pyxres": [440, 104], "taille": [8, 24]},
                        "bloc_6": {"coordonnée": [72, 104], "pyxres": [456, 104], "taille": [56, 24]}
                    },
                    "portail": {"coordonnée": [120, 93], "pyxres": [8,101], "taille": [8, 11]},
                    "pics": {
                        "pics_1": {"coordonnée": [34, 101], "pyxres": [416, 96], "taille": [5, 3]},
                        "pics_2": {"coordonnée": [42, 101], "pyxres": [424, 96], "taille": [5, 3]},
                        "pics_3": {"coordonnée": [88, 101], "pyxres": [424, 96], "taille": [5, 3]}
                    }
                }
        
        elif level == 7 :
            if personnage["coordonnée"][0] == 50 :
                Blocs[niveau] = {
                    "bloc": {
                        "bloc_1": {"coordonnée": [0, 104], "pyxres": [768, 104], "taille": [24, 24]},
                        "bloc_2": {"coordonnée": [32, 104], "pyxres": [800, 104], "taille": [32, 24]},
                        "bloc_3": {"coordonnée": [64, 104], "pyxres": [832, 104], "taille": [32, 24]},
                        "bloc_4": {"coordonnée": [104, 104], "pyxres": [872, 104], "taille": [8, 24]},
                        "bloc_5": {"coordonnée": [120, 104], "pyxres": [888, 104], "taille": [8, 24]}
                    },
                    "portail": {"coordonnée": [120, 93], "pyxres": [8,101], "taille": [8, 11]},
                    "pics" : {
                        "pics_1" : {"coordonnée": [64, 101], "pyxres": [424, 96], "taille": [5, 3]}
                        }
                }
            if personnage["coordonnée"][0] == 100 :
                Blocs[niveau] = {
                    "bloc": {
                        "bloc_1": {"coordonnée": [0, 104], "pyxres": [768, 104], "taille": [24, 24]},
                        "bloc_2": {"coordonnée": [32, 104], "pyxres": [800, 104], "taille": [32, 24]},
                        "bloc_3": {"coordonnée": [64, 104], "pyxres": [832, 104], "taille": [32, 24]},
                        "bloc_5": {"coordonnée": [120, 104], "pyxres": [888, 104], "taille": [8, 24]}
                    },
                    "portail": {"coordonnée": [120, 93], "pyxres": [8,101], "taille": [8, 11]},
                    "pics" : {
                        "pics_1" : {"coordonnée": [64, 101], "pyxres": [424, 96], "taille": [5, 3]}
                        }
                }
            
        elif level == 8 :
            if personnage["coordonnée"][0] == 44 :
                Blocs[niveau]["pics"] = {"pics_1" : {"coordonnée": [64, 101], "pyxres": [424, 96], "taille": [5, 3]}}
                
        
        #collision avec clé
        if "clé" in Blocs[niveau] :
            if (Blocs[niveau]["clé"]["coordonnée"][0] < personnage["coordonnée"][0] + 8) and \
                (Blocs[niveau]["clé"]["coordonnée"][0] + Blocs[niveau]["clé"]["taille"][0] > personnage["coordonnée"][0]) and \
                (Blocs[niveau]["clé"]["coordonnée"][1] < personnage["coordonnée"][1] + 8) and \
                (Blocs[niveau]["clé"]["coordonnée"][1] + Blocs[niveau]["clé"]["taille"][1] > personnage["coordonnée"][1]):
                    porte = True
                    clé = True
                    Blocs[niveau]["portail"]["pyxres"][0] = 8
        
        if "clé" not in Blocs[niveau]:
            porte = True
        
            # collision avec la porte
        if porte:
            if (Blocs[niveau]["portail"]["coordonnée"][0] < personnage["coordonnée"][0] + 8 and
                Blocs[niveau]["portail"]["coordonnée"][0] + Blocs[niveau]["portail"]["taille"][0] > personnage["coordonnée"][0] and
                Blocs[niveau]["portail"]["coordonnée"][1] < personnage["coordonnée"][1] + 8 and
                Blocs[niveau]["portail"]["coordonnée"][1] + Blocs[niveau]["portail"]["taille"][1] > personnage["coordonnée"][1]):
                level += 1
                print("ok")
                if level <= 8:
                    niveau = f"level_{level}"
                    debut_level = True
                else:
                    # niveau terminé
                    fin_jeu = True


        niveau = (f"level_{level}")
    else :
        pass

        
        
            
    
            
    
def draw():
    if not fin_jeu :
        pyxel.cls(couleur)
        for bloc in Blocs[niveau]["bloc"] :
            pyxel.bltm(Blocs[niveau]["bloc"][bloc]["coordonnée"][0], Blocs[niveau]["bloc"][bloc]["coordonnée"][1], 0, Blocs[niveau]["bloc"][bloc]["pyxres"][0], Blocs[niveau]["bloc"][bloc]["pyxres"][1], Blocs[niveau]["bloc"][bloc]["taille"][0], Blocs[niveau]["bloc"][bloc]["taille"][1])
        if "pics" in Blocs[niveau] :
            for pic in Blocs[niveau]["pics"] : 
                pyxel.blt(Blocs[niveau]["pics"][pic]["coordonnée"][0], Blocs[niveau]["pics"][pic]["coordonnée"][1], 0, 34, 93, Blocs[niveau]["pics"][pic]["taille"][0], Blocs[niveau]["pics"][pic]["taille"][1], 5)    
        
        if "clé" in Blocs[niveau] and not clé:
            pyxel.bltm(Blocs[niveau]["clé"]["coordonnée"][0], Blocs[niveau]["clé"]["coordonnée"][1], 0, Blocs[niveau]["clé"]["pyxres"][0], Blocs[niveau]["clé"]["pyxres"][1], Blocs[niveau]["clé"]["taille"][0], Blocs[niveau]["clé"]["taille"][1], 5)
        #if "blocs_phantom" in Blocs[niveau][bloc] :
         #   for blcph in Blocs[niveau][bloc]["blocs_phantom"] :
          #      pyxel.bltm(Blocs[niveau][bloc]["blocs_phantom"][blcph]["coordonnée"][0], Blocs[niveau][bloc]["blocs_phantom"][blcph]["coordonnée"][1], 0, Blocs[niveau][bloc]["blocs_phantom"][blcph]["pyxres"][0], Blocs[niveau][bloc]["blocs_phantom"][blcph]["pyxres"][1], Blocs[niveau][bloc]["blocs_phantom"][blcph]["taille"][0], Blocs[niveau][bloc]["blocs_phantom"][blcph]["taille"][1], 5)
        
        pyxel.blt(Blocs[niveau]["portail"]["coordonnée"][0], Blocs[niveau]["portail"]["coordonnée"][1], 0, Blocs[niveau]["portail"]["pyxres"][0], Blocs[niveau]["portail"]["pyxres"][1], Blocs[niveau]["portail"]["taille"][0], Blocs[niveau]["portail"]["taille"][1], 5)
        pyxel.blt(personnage["coordonnée"][0], personnage["coordonnée"][1], 0, personnage["costume"]*8, 56, personnage["direction"]*8, 8, 5)
    
    if fin_jeu:
        pyxel.cls(0)
        pyxel.text(42, 60, "Bien joue ;)", 6)
        return




pyxel.run(update, draw)
