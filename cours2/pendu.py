listeDeMots = ['coucou']


lettreProposee = []

from random import randrange

fichierDeMots = open('C:\\Users\\pbour\\Desktop\\liste_francais.txt','r')
mots = fichierDeMots.readlines()
fichierDeMots.close()

#print (mots)
#print (len(mots))
nb = randrange(0, len(mots))
motATrouve = mots[nb].strip()

for i in range(1,10):
    lettre = input('entrez une lettre :')
    lettreProposee.append(lettre)

    if (lettre in motATrouve):
        print ("lettre OK")

    print ("Mot a trouve :")
    for a in motATrouve:
        if (a in lettreProposee):
            print(a,end='')
        else:
            print('.',end='')

    print ('')
    print ('vous avez proposee : %s' %lettreProposee)

print("done")