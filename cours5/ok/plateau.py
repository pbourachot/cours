# pylint: disable=no-member
import turtle as tu

import puissance4
import menu


LARGEUR = 430
HAUTEUR = 480

ESPACE_COTE = 60
RAYON_CIRCLE = 20

COULEUR1="blue"
COULEUR2="red"

COULEURS = [COULEUR1, COULEUR2]

tab = puissance4.TableauPuissance4()

joueur = 0


def ajouteUnJeton(couleur, colonne):
    global joueur
    joueur = (joueur + 1) %2
    print("TODO : On rajoute un jeton dans la column %s de couleur %s" %(couleur, colonne))
    posY = tab.retourneLaPremiereLigneVide(colonne)
    if (posY != -1):
        dessinePiece(colonne, posY, COULEURS[joueur])
        tab.ajouteUnePiece(posY,colonne,COULEURS[joueur])

    tab.affiche()


# Fonction appellee quand on click sur la souris
#  x : Coordonnee x de la souris
#  y : Coordonnee y de la souris
def click(x, y):
    print("Click %s %s " % (x, y))

    if (y > 450):
        print(" On selectionne un bouton du menu ")
        menu.actionMenu(x,y)
       

    if (y < 450):
        colonne = int(x/ESPACE_COTE)
        couleur = 'blue'

        ajouteUnJeton(couleur,colonne)


# Dessine la piece (rond) dans le tableau du puissance4
# x : Position en x dans le tableau
# y : Position en y dans le tableau
# couleur : Par default vide, sinon on dessine la piece de la couleur donne
def dessinePiece(x, y, couleur = None):
    tu.pu()
    tu.goto(x + ESPACE_COTE*x + 10, y + ESPACE_COTE*y + 30)
    tu.pd()
    if (couleur != None):
        tu.fillcolor(couleur)
        tu.begin_fill()
    tu.circle(RAYON_CIRCLE)
    if (couleur != None):        
        tu.end_fill()

# Initialize le tableau
def initialiseTableau():

    # Initialize le tableau et la tortue
    tu.setworldcoordinates(0, 0, LARGEUR, HAUTEUR)
    tu.pensize(1)
    tu.speed(0)

    
    # Dessine les colonnes
    for i in range(0, 8):
        tu.pu()
        tu.goto(i + i*ESPACE_COTE, 366)
        tu.pd()
        tu.goto(i + i*ESPACE_COTE, 0)

    # Dessine les lignes
    for i in range(0, 7):
        tu.pu()
        tu.goto(0, i + ESPACE_COTE*i)
        tu.pd()
        tu.goto(427, i+ESPACE_COTE*i)

    tu.right(90)
    for x in range(0, 7):
        for y in range(0, 6):
            dessinePiece(x, y)
    

    # Dessine un menu
    #menu.createMenu()
    
    
    # Associe une fonction au click de souris
    tu.onscreenclick(click)


def main():
    # initialize le tableau de jeu
    initialiseTableau()

    

if __name__ == '__main__':
    # tj = terrainDeJeu()
    main()
    tu.TK.mainloop()
