# Exercice pour jouer avec la librarie os, os.path
# Documentation : http://apprendre-python.com/page-gestion-fichiers-dossiers-python

import os


def listerLesFichiersDUnRepertoire(repertoire):
    print ("Les fichiers du repertoire %s sont :" %(repertoire))
    for f in os.listdir(repertoire):
        print (f)



def listerLeRepertoireQuiContientCeFichier():
    print ("Le fichiers courant est %s" % (__file__))

    repertoire = None

    repertoire = os.path.dirname(__file__)
    print ("Il se trouve dans le repertoire %s" %repertoire)
    return repertoire
   

def creeLeRepertoireDataSiIlNExistePas():
    print (" On cree le repertoire Data si il n'ecrit pas (Au meme niveau que ce fichier")

    rep = listerLeRepertoireQuiContientCeFichier()
    repertoireACreer = os.path.join(rep,'data')

    if (os.path.exists(repertoireACreer)):
        print ("Le repertoire %s existe" %(repertoireACreer))
    else :
        print ("Le repertoire %s n'existe pas. Creeons le." %(repertoireACreer))
        os.makedirs(repertoireACreer)


# Les fichiers creer seront de la forme   x.txt ou x est un chiffre entre (0 et nbDeFichierACreer)
def creeDesFichiersDansLeRepertoireData(nbDeFichierACreer):

    rep = listerLeRepertoireQuiContientCeFichier()
    repertoireACreer = os.path.join(rep,'data')

    for a in range(0,nbDeFichierACreer):
        f = os.path.join(repertoireACreer,"%s.txt" %a)
        print ("Cree le fichier %s" %f)
        fileIn = open(f,'w')
        fileIn.close()

# Les fichiers du repertoires doivent etre renomme avec l'extension .dat
def renommeLesFichiersDuRepertoireData():
    extension = '.dat'

    rep = listerLeRepertoireQuiContientCeFichier()
    repertoireACreer = os.path.join(rep,'data')
    files = os.listdir(repertoireACreer)
    for f in files :
        dest = f.replace('.txt',extension)
        print ("Renome le fichier %s en %s " %(f,dest))
        os.rename(os.path.join(repertoireACreer,f),os.path.join(repertoireACreer,dest))


#listerLesFichiersDUnRepertoire('/')
#listerLeRepertoireQuiContientCeFichier()
#creeLeRepertoireDataSiIlNExistePas()
#creeDesFichiersDansLeRepertoireData(5)
#renommeLesFichiersDuRepertoireData()