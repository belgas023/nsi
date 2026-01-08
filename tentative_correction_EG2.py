from random import choice
class Chemin:
    
    def __init__(self, itinéraire):
        self.itnéraire = itinéraire
        longueur, largeur = 0, 0
        for direction in  self.itnéraire:
            if direction == 'D':
                longueur += 1
            if direction == 'B':
                largeur += 1
        self.longeur = longueur
        self.largeur = largeur
        self.grille = [['.'for i in range(longueur+1)] for j in range (largeur+1)]
        
        
    def remplir_grille(self):
        i, j= 0, 0
        self.grille[0][0]='S'
        for direction in self.itinéraire:
            if direction=='D':
                j += 1
            elif direction=='B':
                i += 1
    
    
    def get_dimensions(self):
        return(self.longeur, self.largeur)
    
    def tracer_chemin(self):
        self.remplir_grille()
        for ligne in self.grille:
            print(ligne)
    
    def itinéraire_aleatoire(m, n):
        itinéraire = ''
        i, j =0, 0
        while i!= m and j != n:
            deplacement = choice(['D', 'B'])
            if deplacement == 'D':
                j+=1
            elif deplacement == 'B':
                i+=1
            itinéraire += deplacement
        if i == m:
            itinéraire += 'D'*(n-j)
        if j == n:
            itinéraire += 'B'*(m-i)
        return itinéraire
    
    
def nombre_chemin(m,n):
    if m==1 or n ==1:
        return 1
    else:
        return(nombre_chemin(m-1,n) + nombre_chemin(m,n-1))