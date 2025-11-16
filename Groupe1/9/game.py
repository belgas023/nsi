import pyxel
import random
import math

pyxel.init(256,256,title="choubidoubidou",fps = 60 , quit_key = pyxel.KEY_ESCAPE)
pyxel.load('2.pyxres')
data = {'gravity_force' : 0.1,"tilemap":[],"ground":[256,256-4*16],'cycle_count':0}
player = {'x':120,'y':120,'velocity':[0,0],'direction':0, 'last_direction':1,'h_speed' : 3,'img':[0,16],'jump_speed' : 3,'life':2,'vulnerable':False,'dash_speed' : 10}
ennemy = {"position" : [0 for i in range(16)],"velocity" : [random.randint(5,10)/10 for i in range(16)],'img':[random.randint(0,2) for i in range(16)]}
ennemy2 = {"side" : 0 , 'x' : 0}
game = {"phase":1}
life_timer = 60
ennemy1_spawn_timer = 5*60
ennemy2_spawn_timer = 5*60
"""
for x in range(128): #Obtenir la liste des coordonnées des blocs dessinés de la tilemap
    for y in range(32):
        if not ((pyxel.tilemaps[0].pget(x,y)[0] == 0) and  (pyxel.tilemaps[0].pget(x,y)[1] == 0)):
                data["tilemap"].append([x*8,y*8])
"""

def update():
    global life_timer, ennemy1_spawn_timer,ennemy2_spawn_timer
    
    if game["phase"] == 1:
        ennemy1_spawn_timer -= 1
        ennemy2_spawn_timer -= 1
        if ennemy2_spawn_timer <= 0:
            spawn_ennemy2()
            ennemy2_spawn_timer = 5*60
        if ennemy1_spawn_timer <= 0:
            data["cycle_count"] += 1
            ennemy1_spawn_timer = (5*60) + random.randint(-10,10)
            ennemy["position"] = [random.randint(0,1) for i in range(16)]
            ennemy["velocity"] = [random.randint(7,12)/10 for i in range(16)]
            ennemy['img']=[random.randint(0,2) for i in range(16)]
        #Définir la vélocité horizontale du joueur et l'image appropriée
        get_axis()
        player['velocity'][0] = player['h_speed'] * player['direction']
        if player['vulnerable'] == False :
            player['img'][1] = 16
            player['img'][0] = (pyxel.frame_count//9)%4*16 if player['direction'] != 0 else 0
    
        
        grounded = is_grounded()
     
        #Appliquer la gravité
        if grounded and player['velocity'][1]>0:
            player['y'] += 256-5*16 - player['y']
            player['velocity'][1] = 0  
        else:
            player['velocity'][1] += data['gravity_force']
        if player['velocity'][1]>0:
            data['gravity_force'] = 0.3
        else:
            data['gravity_force'] = 0.1
        
        
        #Gérer le saut
        if pyxel.btnp(pyxel.KEY_SPACE) and grounded:
            player['velocity'][1] -= player['jump_speed']
        if pyxel.btnr(pyxel.KEY_SPACE) and player['velocity'][1]<0:
            player['velocity'][1]*=0.3
    
        player['x'] += player['velocity'][0] 
        player['y'] += player['velocity'][1]
        
        if player['x'] >= 256-16:
            player['x'] = 256-16
        if player['x'] <= 0:
            player['x'] = 0
        if player['vulnerable'] == True:
            life_timer -= 1
            player['img'][0] = 80
            player['img'][1] = 32
            if life_timer <= 0:
                player['vulnerable'] = False
        
        #Position des ennemis
        for i in range(16):
            ennemy['position'][i] += ennemy['velocity'][i]
            if pyxel.frame_count % 15 == 0:
                ennemy['img'][i] = ennemy['img'][i]+1 if ennemy['img'][i] <= 2  else 0
            if (collision1(player['x']+4,player['y']+3,player['x']+14,player['y']+16,i*16+4,ennemy['position'][i]+3,i*16+11,ennemy['position'][i]+15) or collision2(player['x']+4,player['y']+3,player['x']+14,player['y']+16,ennemy2['x']+2,256-5*16,ennemy2['x']+14,256-4*16)) and not player['vulnerable']:
                player['life'] -= 1
                player['vulnerable'] = True
                if player['life'] == 0:
                    game['phase'] = 2
        if ennemy2['side'] == -1:
            ennemy2['x'] += 1
        else:
            ennemy2['x'] -= 1

def spawn_ennemy2():
    ennemy2['side'] = [-1,1][random.randint(0,1)]
    if ennemy2['side'] == -1:
        ennemy2['x'] = -10
    elif ennemy2['side'] == 1:
        ennemy2['x'] = 256

def collision1(A_x1, A_y1, A_x2, A_y2, B_x1, B_y1, B_x2, B_y2):
    return not (A_x1 > B_x2 or A_y1 > B_y2 or A_x2 < B_x1 or A_y2 < B_y1)

def collision2(A_x1, A_y1, A_x2, A_y2, B_x1, B_y1, B_x2, B_y2):
    return not (A_x1 > B_x2 or A_y1 > B_y2 or A_x2 < B_x1 or A_y2 < B_y1)

def is_grounded():
        if player['y']>=250-5*16:
            return True
        else :
            return False
def get_axis(): #Obtenir la direction de déplacement horizontale du joueur
    if player['direction'] != 0:
        player['last_direction'] = player['direction']
    if pyxel.btn(pyxel.KEY_RIGHT):
        player['direction'] = 1
    elif pyxel.btn(pyxel.KEY_LEFT):
        player['direction'] = -1
    else:
        player['direction'] = 0

def draw():
    pyxel.cls(2)
    if game["phase"] == 1:
        pyxel.blt(player['x'],player['y'],0,player['img'][0],player['img'][1],16 * player["last_direction"],16,2)
        pyxel.text(16,16,str(player['life']),8)
        pyxel.blt(25,10,0,112,48,16,16,2)
        for i in range(16):
            pyxel.blt(i*16, ennemy['position'][i],0,ennemy["img"][i]*16,80,16,16,2,-90)
        pyxel.bltm(0,0,0,0,0,256,256,2)
        pyxel.text(256-48,16,f"Cycles : {data['cycle_count']}", 8)
        pyxel.blt(ennemy2['x'],256-5*16,0,128,16,16*ennemy2['side'],16,2) 
    elif game["phase"] == 2:
        pyxel.text(110, 120 ,'Game Over', 8)
        pyxel.text(110,140,f"Cycles : {data['cycle_count']}", 8)
pyxel.run(update,draw)