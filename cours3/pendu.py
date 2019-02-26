import utils, sys


''' Affiche le mot et les lettres proposees '''
def afficherLeMot(motATrouve, lettrePropose):
    print ("Mot a trouve :")
    for a in motATrouve:
        if (a in lettreProposee):
            print(a,end='')
        else:
            print('.',end='')
    print("")
    if (len(lettreProposee) > 0 ) :
        print ('vous avez proposee : %s' %lettreProposee)

''' Retourne True si on a trouvee toutes les lettres du mot '''
def gagne(motATrouve, lettrePropose):
    motTrouve = True
    for a in motATrouve:
        if (a not in lettreProposee):
            motTrouve = False
    return motTrouve


NB_ERROR = 0

utils.titre()
motATrouve = utils.retourneUnMotAuHasard()
lettreProposee = []

# Petit mode triche pour afficher le mot a trouve
if (len(sys.argv) > 1 and sys.argv[1] == 'cheat'):
    print(motATrouve)

leMotAEteTrouve = False

# On autorise 7 erreurs
while (NB_ERROR < 7):
    
    # On affiche le pendu
    utils.affichePendu(NB_ERROR)

    # On affiche le mot a trouve et les lettres proposees
    afficherLeMot(motATrouve, lettreProposee)
    

    lettre = input('entrez une lettre :')
    

    if (lettre in lettreProposee):
        print ("la lettre a deja ete proposee")
    else :
        lettreProposee.append(lettre)
        if (lettre in motATrouve):
            print ("La lettre est presente")
        else :
            print ("La lettre n'est pas presente")
            NB_ERROR += 1

    if (gagne(motATrouve, lettreProposee)):
        utils.gagne()
        leMotAEteTrouve = True
        break

if (not leMotAEteTrouve ):
    utils.perdu()
    print ("Le bon mot etait %s" %motATrouve)
    
    
    
    

print("done")