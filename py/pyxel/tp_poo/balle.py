import pygame, sys
import time
from pygame.locals import *
from math import *
from random import randint

LARGEUR = 640
HAUTEUR = 480
RAYON = 20

pygame.display.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
fenetre.fill([0,0,0])

def distance(a, b):
    return sqrt((b.x - a.x)**2 + (b.y - a.y)**2)


class balle:
    
    def __init__(self, couleur, v):
        self.x = randint(0 + RAYON, LARGEUR - RAYON)
        self.y = randint(0 + RAYON, HAUTEUR - RAYON)
        self.dx = v
        self.dy = v
        #self.couleur = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.couleur = couleur

    def draw(self):
        pygame.draw.circle(fenetre, self.couleur, (self.x, self.y), RAYON)
        
    def move(self):
        if self.x + RAYON >= LARGEUR:
                self.dx = -self.dx
                self.x = LARGEUR - RAYON
        elif self.x - RAYON <= 0:
            #if not self.x + self.dx +RAYON < 0:
                self.dx = -self.dx
                self.x = 0 + RAYON
        elif self.y + RAYON >= HAUTEUR:
            #if not self.y + self.dy + RAYON > LARGEUR:
                self.dy = -self.dy
                self.y = HAUTEUR - RAYON
        elif self.y - RAYON <= 0:
            #if not self.y + self.dy + RAYON < 0:
                self.dy = -self.dy
                self.y = 0 + RAYON
        
        self.x += self.dx
        self.y += self.dy
        

            
    def collision(self):
        for i in sac_a_balle:
            if distance(self, i) <= (2*RAYON):
                self.dx , i.dx = i.dx, self.dx
                self.dy, i.dy = i.dy, self.dy
                #difference = RAYON - distance(self, i)
                
                if i.couleur == balleSeule.couleur or self.couleur == balleSeule.couleur:
                    self.couleur = balleSeule.couleur
                    #print(f"touché x:{self.x}, y:{self.y}, dx:{self.dx}, dy:{self.dy}")

sac_a_balle = [balle((255, 255, 255), randint(2, 4)) for i in range(30)]

balleSeule = balle((255,1,1), randint(2, 4))
sac_a_balle.append(balleSeule)


while True:
    fenetre.fill([0, 0, 0])
    
    for bal in sac_a_balle:
        bal.move()
        bal.collision()
        bal.draw()
        
    balleSeule.move()
    balleSeule.collision()
    balleSeule.draw()

#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             pygame.display.update()
    pygame.display.update()

    # routine pour pouvoir fermer «proprement» la fenêtre Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()

    time.sleep(0.01)

