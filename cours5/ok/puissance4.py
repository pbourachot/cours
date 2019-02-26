

TAILLE_X = 7
TAILLE_Y = 6
VIDE = ''

class TableauPuissance4:

    def __init__(self):
        self.data = [ [VIDE,VIDE,VIDE,VIDE,VIDE,VIDE,VIDE],
                 [VIDE,VIDE,VIDE,VIDE,VIDE,VIDE,VIDE],
                 [VIDE,VIDE,VIDE,VIDE,VIDE,VIDE,VIDE],
                 [VIDE,VIDE,VIDE,VIDE,VIDE,VIDE,VIDE],
                 [VIDE,VIDE,VIDE,VIDE,VIDE,VIDE,VIDE],
                 [VIDE,VIDE,VIDE,VIDE,VIDE,VIDE,VIDE],
                 [VIDE,VIDE,VIDE,VIDE,VIDE,VIDE,VIDE], ]

    # Affiche la valeur du tableau de puissance4
    def affiche(self):
        for line in reversed(self.data):
            print(line)
    

    def retourneLaPremiereLigneVide(self,column):

        for i in range(0,TAILLE_Y):
            print(i)
            print(self.data[i][column])
            if (self.data[i][column] == VIDE):
                print(i)
                return i
        return -1

    def ajouteUnePiece(self,ligne, colonne,couleur):        
        self.data[ligne][colonne] = couleur
