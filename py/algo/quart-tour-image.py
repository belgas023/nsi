from PIL import Image

img = Image.open("eiffel.gif")

def permute_quadrants(img, quadrant_1, quadrant_2, n):
    """
    Échange les contenus de deux quadrants carrés de taille n x n.
    Ces quadrants sont définis par les coordonnées du coin en haut à gauche et par leur largeur.
    Paramètres :
        img : Image carrée
        quadrant_1 : Tuple donnant les coordonnées du coin en haut et à gauche du quadrant 1
        quadrant_2 : Tuple donnant les coordonnées du coin en haut et à gauche du quadrant 2
        n : Entier positif donnant la largeur des deux cadrants
    Valeur renvoyée :
        Ne renvoie rien mais modifie le tableau donné en entrée
    """
    for i in range(n//2):
        for j in range(n//2):
            coul1 = img.getpixel( (quadrant_1[0]+i, quadrant_1[1]+j) )
            coul2 = img.getpixel( (quadrant_2[0]+i, quadrant_2[1]+j) )
            
            img.putpixel( (quadrant_1[0]+i, quadrant_1[1]+j), (coul2) )
            img.putpixel( (quadrant_2[0]+i, quadrant_2[1]+j), (coul1) )
            
            
            
def tourne_recursif(img, carré, n):
    """
    Découpe un carré de taille n x n en 4 quadrants, puis fait faire à ces quadrants un quart de tour dans le sens horaire :
         ┌───┬───┐                        ┌───┬───┐     
         │ A │ B │                        │ D │ A │    
    Ex : ├───┼───┤ devient après rotation ├───┼───┤
         │ D │ C │                        │ C │ B │  
         └───┴───┘                        └───┴───┘      
    Puis la fonction s'appelle récursivement pour chacun des quadrants qui sont à leur tour découpés en 4...
    Le carré de départ est défini par les coordonnées du coin en haut à gauche et par sa largeur.
    Paramètres :
        img : Image carrée
        carré : Tuple donnant les coordonnées du coin en haut à gauche du cadrant
        n : Entier positif donnant la largeur du carré de départ. (n doit être une puissance de 2)
    Valeur renvoyée :
        Ne renvoie rien mais modifie le tableau donné en entrée
    """
    if n >= 2:
        quadrant_A = (carré[0]+0,    carré[1]+0)
        quadrant_B = (carré[0]+n//2,    carré[1]+0)
        quadrant_C = (carré[0]+n//2, carré[1]+n//2)
        quadrant_D = (carré[0]+0, carré[1]+n//2)
        permute_quadrants(img, quadrant_A, quadrant_B, n)
        permute_quadrants(img, quadrant_A, quadrant_C, n)
        permute_quadrants(img, quadrant_A, quadrant_D, n)
        tourne_recursif(img, quadrant_A, n//2)
        tourne_recursif(img, quadrant_B, n//2)
        tourne_recursif(img, quadrant_C, n//2)
        tourne_recursif(img, quadrant_D, n//2)
        


img.show()
tourne_recursif(img, (0, 0), img.width)
img.show()

