    def __init__(self):
        self.début = None
    
    def est_vide(self):
        return self.début is None
    
    def longueur(self):
        if self.est_vide():
            return 0
        else:
            résultat = 1
            maillon = self.début
            while maillon.suivant != None:
                maillon = maillon.suivant
                résultat += 1
            return résultat
    
    def ajouter(self, valeur, indice=0):
        assert 0 <= indice < self.longueur(), "l'indice est incorrect"
        if indice == 0:
            self.début = Maillon(valeur, self.début)
        else:
            maillon_suivant = self.début
            for _ in range(indice):
                maillon_précédent = maillon_suivant
                maillon_suivant = maillon_suivant.suivant
            maillon_précédent.suivant = Maillon(valeur, maillon_suivant)
