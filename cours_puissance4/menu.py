# pylint: disable=no-member
import turtle as tu

MENU_0 = 0
MENU_0_NOM = "Recommencer"

MENU_1 = 1
MENU_1_NOM = "Sauver"

MENU_2 = 2
MENU_2_NOM = "Charger"

MENU_3 = 3
MENU_3_NOM = "Verifier"

# Permet de savoir sur quel button on a cliquer
def returnNumeroDuMenu(x, y):
    return 1


def actionMenu(x,y):
    return
    '''
    numActionSelectionne = returnNumeroDuMenu(x, y)

    if (numActionSelectionne == MENU_0):
        reset()
    elif (numActionSelectionne == MENU_1):
        sauver()
    elif (numActionSelectionne == MENU_2):
        charger()
    elif (numActionSelectionne == MENU_3):
        verifie()
    '''


# Reset
# On reinitialize tout
def reset():
    print("TODO : Implementer le Reset du puissance4")


# Sauver
# On sauve la partie en cours dans un fichier
def sauver():
    print("TODO : Implementer le sauver du puissance4")

# Charger
# On sauve la partie en cours dans un fichier
def charger():
    print("TODO : Implementer le charger du puissance4")


# On verifie si un des joueurs a gagne
def verifie():
    print("TODO : Implementer la verification du puissance4")



# Dessine un menu
# num : numero du menu
# text : text a afficher
def dessinMenu(num, text):
    tu.pu()
    tu.goto(60*num + 10, 450)
    tu.pd()
    tu.goto(60*num + 10 + 60, 450)
    tu.goto(60*num + 10 + 60, 475)
    tu.goto(60*num + 10, 475)
    tu.goto(60*num + 10, 450)
    tu.pu()
    tu.goto(60*num + 10 + 10, 450 + 10)
    tu.write(text)


def createMenu():
    dessinMenu(MENU_0, MENU_0_NOM)
    dessinMenu(MENU_1, MENU_1_NOM)
    dessinMenu(MENU_2, MENU_2_NOM)
    dessinMenu(MENU_3, MENU_3_NOM)