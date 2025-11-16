longeur, largeur = float(input('longeur?')), float(input('largeur?'))

fichier = open('iris.csv', 'r')
liste = fichier.readlines()
fichier.close()

def distanceEuclidienne(a1, a2, b1, b2):
    return ((a1-a2)**2 +(b1-b2)**2)**0.5

del liste[0]

nouvListe = []
nouvListe1 = []
for i in liste:
    nouvListe.append(i.strip().split(","))
for i in nouvListe:
    longeur2, largeur2, espece = float(i[0]), float(i[1]), i[2]
    nouvListe1.append([distanceEuclidienne(longeur, largeur, longeur2, largeur2), longeur2, largeur2, espece])
nouvListe1.sort()
print(nouvListe1)
for i in range(5):
    print(nouvListe1[i][3])