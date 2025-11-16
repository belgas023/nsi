import pygame, sys
import time, random
from pygame.locals import *

LARGEUR = 640
HAUTEUR = 480
RAYON = 30

def distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

class Balle:
    def __init__(self, numéro):
        self.x = random.randint(RAYON, LARGEUR - RAYON)
        self.y = random.randint(RAYON, HAUTEUR - RAYON)
        self.dx = random.randint(1, 3)
        self.dy = random.randint(1, 3)
        self.couleur = (random.randint(20, 255), random.randint(20, 255), random.randint(20, 255))
        self.numéro = numéro
        
    def bouge_et_dessine(self, balles):
        # Gestion des rebonds sur les bords de la fenêtre
        if not (RAYON <= self.x + self.dx <= LARGEUR - RAYON):
            self.dx = -self.dx
        if not (RAYON <= self.y + self.dy <= HAUTEUR - RAYON):
            self.dy = -self.dy
        # Gestion des collisions avec les autres balles
        for balle in balles:
            if (self.numéro != balle.numéro) and (distance(self.x + self.dx, self.y + self.dy, balle.x, balle.y) <= 2 * RAYON):
                if distance(self.x + balle.dx, self.y + balle.dy, balle.x, balle.y) > distance(self.x + self.dx, self.y + self.dy, balle.x, balle.y):
                    self.dx, balle.dx = balle.dx, self.dx
                    self.dy, balle.dy = balle.dy, self.dy
        
        self.x += self.dx
        self.y += self.dy

        pygame.draw.circle(fenetre, self.couleur, (self.x, self.y), RAYON)
        #print(f"balle {self.numéro}:", self.x, self.dx, self.y, self.dy, f"balle {balle.numéro}:", balle.x, balle.dx, balle.y, balle.dy)



# Programme principal
pygame.display.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
sac_a_balles = [Balle(i) for i in range(15)]

while True:
    fenetre.fill([0, 0, 0])
    for balle in sac_a_balles:
        balle.bouge_et_dessine(sac_a_balles)

    pygame.display.update()

    # routine pour pouvoir fermer «proprement» la fenêtre Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
    
    time.sleep(0.02)

