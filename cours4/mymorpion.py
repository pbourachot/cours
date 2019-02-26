
import turtle as tu


# TODO:
#  **** Clear Button
#  **** Controler si croix presente
#  **** Gagner ???


# Settings
height = 400
width = 400
speed = 0
epaisseur = 5

nbEssai = 0


tableau = [['','',''], # ligne du base
           ['','',''], # ligne du milieu
           ['','','']] # ligne du haut


def printTableau():    
    for a in reversed(tableau):        
        print(a)

def addCase(x,y,signe):
    global tableau
     
    tableau[y][x] = signe

def caseEstVide(x,y):
    case = tableau[y][x]
    if (case == ''):
        return True
    else :
        return False

def verifieResultat(x,y):

    signe = tableau[y][x]

    # verifie ligne
    if (tableau[y][0] == tableau[y][1] == tableau[y][2]):
        print ("Ligne Complete")
        tu.textinput("GAGNE", "Ligne Complete")

    # Colonne
    if (tableau[0][x] == tableau[1][x] == tableau[2][x]):
        print ("Colonne Complete")
        tu.textinput("GAGNE", "Colonne Complete")

    # diagonale
    if (tableau[0][0] == tableau[1][1] == tableau[2][2] == signe):
        print ("Diagonale montante")
        tu.textinput("GAGNE", "Diagonale Complete")

    if (tableau[0][2] == tableau[1][1] == tableau[2][0] == signe):
        print ("Diagonale Descendante")
        tu.textinput("GAGNE", "Diagonale Complete")


#Reiinitialize tout
def clear():
    print("Clear" )

    global tableau 
    tu.reset()
    # initialize
    initialize()

    # Dessine la grille
    dessineGrille()


    tableau = [['','',''], # ligne du base
           ['','',''], # ligne du milieu
           ['','','']]

def dessineO(x,y):
    print("Dessine un rond dans la case x,y")
    tu.color("blue")
    tu.pu()
    tu.goto(20 + 120*x + 5*x , 60 + 120*y + 5*y)
    tu.pd()
    tu.circle(40)
    print(tu.position())

def dessineX(x,y):
    print("Dessine une croix dans la case x,y")
    tu.color("red")
    tu.pu()
    tu.goto(20 + 120*x + 5*x , 40 + 60 + 120*y + 5*y)
    tu.pd()
    tu.goto(20 + 120*x + 5*x + 80, -40 + 60 + 120*y + 5*y)


    tu.pu()
    tu.goto(20 + 120*x + 5*x + 80 , 40 + 60 + 120*y + 5*y)
    tu.pd()
    tu.goto(20 + 120*x + 5*x , -40 + 60 + 120*y + 5*y)


    #tu.circle(40)

def click(x,y):
    global nbEssai, tableau
    nbEssai +=  1
    print("Click %s %s " %(x,y))
    caseX = int(x / 120)
    caseY = int(y / 120)

    print("Click %s %s " %(caseX,caseY))

    if (caseX == 0 and caseY == 3):        
        clear()
    elif (caseEstVide(caseX, caseY)):

        if (nbEssai % 2 == 1):
            dessineX(caseX,caseY)
            addCase(caseX, caseY, 'X')
            
        else :
            dessineO(caseX,caseY)       
            addCase(caseX, caseY, 'O ')

        verifieResultat(caseX,caseY)

    printTableau()
    
         

def initialize():
    tu.setworldcoordinates(0,0,400,400)
     
    tu.pensize(epaisseur)
    tu.speed(speed)
    print(tu.position())

    tu.onscreenclick(click)
    #tu.onscreenclick(tu.goto)
    tu.pu()
    tu.goto(10,380)        
    tu.pd()
    tu.right(-90)
    tu.forward(10)
    tu.right(90)
    tu.forward(50)
    tu.right(90)
    tu.forward(10)
    tu.right(90)
    tu.forward(50)
    tu.right(-180)

    #tu.right(-90)
    tu.write('Recommence')

    #tu.ht()


def dessineGrille():
    tu.pu()
    tu.goto(0,120)    
    tu.pd()
    tu.fd(370)
    tu.pu()
    tu.goto(0,245)    
    tu.pd()
    tu.fd(370)
    tu.right(90)
    tu.pu()
    tu.goto(120,370)    
    tu.pd()
    tu.fd(370)
    tu.pu()
    tu.goto(245,370)    
    tu.pd()
    tu.fd(370)





def main():

    # initialize
    initialize()

    # Dessine la grille
    dessineGrille()


if __name__ == '__main__':
    main()
    tu.TK.mainloop()