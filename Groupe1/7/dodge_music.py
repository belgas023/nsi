import pyxel, random, time
pyxel.init(256, 256, "jeu")
ennemi = [[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0]]
ennemi_2 = [[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0]]
personnage = [0, 0, 0, 0, 0]
vitesse= 10
personnage[random.randint(0,4)] = 1
pyxel.load("4.pyxres")
steve_wii = 0
song = 0
timer = 0
mort = 3
music = True
win = False
jouer = False
bs = 0
def update():
    global personnage, ennemi, timer, ennemi_2, mort, music, win, jouer, steve_wii, song, bs
    if pyxel.btnp(pyxel.KEY_RETURN) and jouer==False:
        jouer=True
    if pyxel.btnp(pyxel.KEY_1) and jouer==False:
        song = 1
    elif pyxel.btnp(pyxel.KEY_2) and jouer==False:
        song = 0
    if jouer == True:
        if song == 0:
            steve_wii = 3
        elif song == 1:
            steve_wii = 4
        if personnage[personnage.index(1)]==ennemi[personnage.index(1)][5]:
            ennemi[personnage.index(1)][5]=0
            mort -= 1
            print(mort)
        if mort == 0 and bs == 0:
            pyxel.playm(2,0,True)
            bs = 1
        if pyxel.frame_count%5 == 0:
            timer+=1
        #print(ennemi)
        if timer==steve_wii:
            if music == True:
                music = False
                pyxel.playm(song, 0)
            elif music == False:
                
                if pyxel.play_pos(0) == None:
                    win = True
            pos_ennemi = random.randint(0, 4)
            #print(pos_ennemi)
            while ennemi[pos_ennemi][0] == 1 or ennemi[pos_ennemi][1]==1:
                pos_ennemi = random.randint(0,4)
            ennemi[pos_ennemi][0]=1
            timer = 0
            for i in range(len(ennemi)):
                for j in range(len(ennemi[i])):
                    if ennemi[i][5]==1:
                        ennemi[i][5]=0                    
                    if ennemi[i][-j] == 1:
                        ennemi_2[i][-j+1] = ennemi[i][-j]
            ennemi=ennemi_2
            ennemi_2 = [[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0]]
        if pyxel.btnp(pyxel.KEY_UP) and personnage[0]!=1:
            i = personnage.index(1)
            personnage[i-1] = 1
            personnage[i] = 0
        if pyxel.btnp(pyxel.KEY_DOWN) and personnage[4]!=1:
            i = personnage.index(1)
            personnage[i+1] = 1
            personnage[i] = 0
        if pyxel.btnp(pyxel.KEY_RETURN) and jouer==False:
            jouer=True
def draw():
    if jouer == False:
        pyxel.bltm(0, 0, 0,256*4, 0, 256, 256)
    if win == True:
        pyxel.bltm(0, 0, 0, 512+256, 256, 256, 256)
        pyxel.stop()
    elif win == False and jouer == True:
        if mort > 0:
            if timer %4==0:
                pyxel.bltm(0, 0, 0, 0, 0, 256, 256)
            else:
                pyxel.bltm(0, 0, 0, 0, 256, 256, 256)
            if mort == 2:
                if timer == 0 or timer == 2 or timer == 4:
                    pyxel.bltm(0, 0, 0, 256, 0, 256, 256)
                elif timer == 1 or timer == 3 or timer == 5:
                    pyxel.bltm(0, 0, 0, 256, 256, 256, 256)
            if mort == 1:
                if timer == 0 or timer == 2 or timer == 4:
                    pyxel.bltm(0, 0, 0, 512, 0, 256, 256)
                elif timer == 1 or timer == 3 or timer == 5:
                    pyxel.bltm(0, 0, 0, 512, 256, 256, 256)
            if timer==0 or timer==3:
                pyxel.blt(20, 39+48*personnage.index(1) ,0, 0, 17, 16, 16, scale=1.5)
            elif timer ==1 or timer==4:
                pyxel.blt(20, 39+48*personnage.index(1) ,0, 16, 17, 16, 16, scale=1.5)
            elif timer ==2 or timer==5:
                pyxel.blt(20, 39+48*personnage.index(1) ,0, 32, 17, 16, 16, scale=1.5)
            for i in range(len(ennemi)):
                for j in range(len(ennemi[i])):
                    if ennemi[i][j]==1:
                        if timer%2==0:
                            pyxel.blt(240-43*j, 39+48*i ,0, 64, 33, 16, 16, scale=1.5, colkey=2)
                        else:
                            pyxel.blt(240-43*j, 39+48*i ,0, 80, 33, 16, 16, scale=1.5, colkey=2)
        elif mort == 0:
            pyxel.bltm(0, 0, 0, 512+256, 0, 256, 256)
pyxel.run(update, draw)