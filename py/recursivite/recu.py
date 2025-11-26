import pylab   # Le module matplotlib doit être installé

def Disque(x, y, r):
    """ disque de centre (x,y) et de rayon r """
    disque = pylab.Circle([x, y], radius = r)
    F.add_patch(disque)
    
def DisquesRecursif(x, y, r):
    """ Construction récursive de la figure """
    Disque(x, y, r)
    if r > 1:
        DisquesRecursif(x+r+r/2, y, r/2)

# Création de la figure
F = pylab.gca()
DisquesRecursif(0, 0, 8)
# Affichage de la figure
pylab.axis('scaled')
pylab.show()