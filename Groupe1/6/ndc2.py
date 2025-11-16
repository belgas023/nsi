import pyxel, random
taille_grille=128

pyxel.init(taille_grille*6, taille_grille*6, title="The run for immortality")
pyxel.load("2.pyxres")

personnage={'x':10*6,'y':114*6,'vie':5,'choix_arme':1,'choix_personnage':[0,16]}
vague=1
vitesse_cases=6
score = 0
nb_cases1=6
nb_cases2=18
nb_cases3=18

spawn=[]

def update():
    global spawn, score 

    if personnage['vie']>0:
        nombres_cases_1=[(random.randint(1,3),random.randint(1,3)) for _ in range(nb_cases1)]
        cases=[{'ligne':l,'choix_boite':{1:0,2:16,3:32}[s],'x':taille_grille*6} for (l,s) in nombres_cases_1]
        if pyxel.frame_count%30==0 and cases:
            spawn.append(cases.pop(0))

        if pyxel.frame_count%4==0:
            if personnage['choix_personnage'][0]<48:
                personnage['choix_personnage'][0]+=16
            else:
                personnage['choix_personnage'][0]=0

        if pyxel.btnp(pyxel.KEY_X):
            personnage['choix_arme']=3
        elif pyxel.btnp(pyxel.KEY_C):
            personnage['choix_arme']=16
        elif pyxel.btnp(pyxel.KEY_V):
            personnage['choix_arme']=32

        if pyxel.btnp(pyxel.KEY_UP) and personnage['y']>=36*6:
            personnage['y']-=40*6
        if pyxel.btnp(pyxel.KEY_DOWN) and personnage['y']<114*6:
            personnage['y']+=40*6

        if pyxel.frame_count%30==0:
            for case in spawn:
                case['x']-=90

        for case in spawn[:]:
            y_case={1:114*6,2:74*6,3:34*6}[case['ligne']]
            sword_x=personnage['x']+70
            if sword_x>=case['x']-42 and sword_x<=case['x']-42+64 and personnage['y']==y_case:
                if (personnage['choix_arme']==3 and case['choix_boite']==0) or personnage['choix_arme']==case['choix_boite']:
                    spawn.remove(case)
                    score += 1
                else:
                    personnage['vie']-=1
                    spawn.remove(case)

        for case in spawn[:]:
            if case['x']-42<0:
                personnage['vie']-=1
                spawn.remove(case)
    else:
        pyxel.show()
        pyxel.text(64*6, 64*6,0,  'GAME OVER !! YOU LOOSE')
    
def draw():
    if score >=15:
        pyxel.bltm(0,0,0, 0, 200,512+256,512+256)
        pyxel.blt(28*6,64*6,0,0,16,16,16,pyxel.COLOR_PURPLE,scale=7)
        pyxel.blt(100*6, 64*6, 0, 128, 15, 15, 15, pyxel.COLOR_PURPLE, scale=7)
        pyxel.blt(64*6, 64*6, 0, 20, 50, 8, 11, pyxel.COLOR_PURPLE, scale=7)
        
        
    else:
        pyxel.cls(pyxel.COLOR_PURPLE)
        pyxel.blt(personnage['x'],personnage['y'],0,personnage['choix_personnage'][0],16,16,16,pyxel.COLOR_PURPLE,scale=7)
        if personnage['choix_arme']==3:
            pyxel.blt(personnage['x']+60,personnage['y'],0,2,65,12,12,pyxel.COLOR_PURPLE,scale=6)
        if personnage['choix_arme']==16:
            pyxel.blt(personnage['x']+65,personnage['y']-5,0,15,64,16,16,pyxel.COLOR_PURPLE,scale=6)
        if personnage['choix_arme']==32:
            pyxel.blt(personnage['x']+70,personnage['y']-10,0,31,63,17,17,pyxel.COLOR_PURPLE,scale=6)
        for i in range(personnage['vie']):
            pyxel.blt((5.5*i+2)*6,15,0,115,52,12,12,pyxel.COLOR_PURPLE,scale=3)
        for case in spawn:
            if case['ligne']==1:
                pyxel.blt(case['x']-42,114*6,0,case['choix_boite'],96,16,16,pyxel.COLOR_PURPLE,scale=4)
            elif case['ligne']==2:
                pyxel.blt(case['x']-42,74*6,0,case['choix_boite'],96,16,16,pyxel.COLOR_PURPLE,scale=4)
            elif case['ligne']==3:
                pyxel.blt(case['x']-42,34*6,0,case['choix_boite'],96,16,16,pyxel.COLOR_PURPLE,scale=4)
        if personnage['vie'] <= 0:
            pyxel.cls(pyxel.COLOR_PURPLE)
            pyxel.bltm(32*6,32*6,0,0,0, 384, 175)
        
    

pyxel.run(update,draw)
