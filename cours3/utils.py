pendu_img1 = """
---------
 |     |
 |
 |
 |
 |
 |"""

pendu_img2 = """
 ---------
 |     |
 |     o
 |
 |
 |
 |"""

pendu_img3 = """
 ---------
 |     |
 |     O
 |    -+-
 |
 |
 |"""

pendu_img4 = """
 ---------
 |     |
 |     O
 |   /-+-
 |
 |
 |"""

pendu_img5 = """
 ---------
 |     |
 |     O
 |   /-+-/
 |
 |
 |"""

pendu_img6 = """
 ---------
 |     |
 |     O
 |   /-+-/
 |    |
 |
 |"""

pendu_img7 = """
 ---------
 |     |
 |     O
 |   /-+-/
 |    | |
 |
 |"""


''' Contient les images du pendu '''
IMAGES_PENDU = [pendu_img1,pendu_img2,pendu_img3,pendu_img4,pendu_img5,pendu_img6,pendu_img7]

''' Affiche l'image correspondant a l'echec numero nb '''
def affichePendu(nb):
    print (IMAGES_PENDU[nb])

from random import randrange
''' Retourne un mot au hasard pris dans le fichier liste_francais.txt '''
def retourneUnMotAuHasard():

    fichierDeMots = open('liste_francais.txt','r')
    mots = fichierDeMots.readlines()
    fichierDeMots.close()

    nb = randrange(0, len(mots))
    return mots[nb].strip()


def titre():
    message("Jeu du pendu")

def gagne():
    message("Gagne")

def perdu():
    message("Perdu")


''' Affiche un message dans un titre ''' 
def message(text):
    print ("########################## ")
    print ("       %s        " %text) 
    print ("########################## ")