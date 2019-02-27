# Exercice pour jouer avec la librarie os, os.path
# Documentation : http://apprendre-python.com/page-gestion-fichiers-dossiers-python

import os


def listerLesFichiersDUnRepertoire(repertoire):
    print ("Les fichiers du repertoire %s sont :" %(repertoire))

    #### A Completer
    #### Fin de A Completer


def listerLeRepertoireQuiContientCeFichier():
    print ("Le fichiers courant est %s" % (__file__))

    repertoire = ""

    #### A Completer
    #### Fin de A Completer
    return repertoire
   

def creeLeRepertoireDataSiIlNExistePas():
    print (" On cree le repertoire Data si il n'ecrit pas (Au meme niveau que ce fichier")

    rep = listerLeRepertoireQuiContientCeFichier()
    repertoireACreer = os.path.join(rep,'data')

    #### A Completer
    #### Fin de A Completer


# Les fichiers creer seront de la forme   x.txt ou x est un chiffre entre (0 et nbDeFichierACreer)
def creeDesFichiersDansLeRepertoireData(nbDeFichierACreer):

    rep = listerLeRepertoireQuiContientCeFichier()
    repertoireACreer = os.path.join(rep,'data')

    #### A Completer
    #### Fin de A Completer

# Les fichiers du repertoires doivent etre renomme avec l'extension .dat
def renommeLesFichiersDuRepertoireData():
    extension = '.dat'

    rep = listerLeRepertoireQuiContientCeFichier()
    repertoireACreer = os.path.join(rep,'data')
    #### A Completer
    #### Fin de A Completer


listerLesFichiersDUnRepertoire('/')
listerLeRepertoireQuiContientCeFichier()
creeLeRepertoireDataSiIlNExistePas()
creeDesFichiersDansLeRepertoireData(5)
renommeLesFichiersDuRepertoireData()