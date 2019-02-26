import random

# Fonction qui retourne une liste de chiffre au hasard
def genereUnListeDeChiffreAuHasard():

    liste = []
    for i in range(0, 10):
        liste.append(random.randint(1, 101))
    return liste


def retourneLeChiffreLeplusGrandDuneListe(liste):
    chiffreLePlusGrand = 0
    # A Completer

    # Fin de A Completer
    return chiffreLePlusGrand


def retourneLeChiffreLeplusGrandEtLePlusPetitDuneListe(liste):
    chiffreLePlusGrand = 0
    chiffreLePlusPetit = 0
    # A Completer

    # Fin de A Completer
    return chiffreLePlusGrand, chiffreLePlusPetit


def retourneLaSommeDeLaListe(liste):
    somme = 0
    # A Completer

    # Fin de A Completer
    return somme


retourneLaSommeDeLaListe
# Exercice 1

listeAuHasard = genereUnListeDeChiffreAuHasard()
print("Liste de chiffre")
print(listeAuHasard)
print("Le chiffre le plus grand est %s" %
      retourneLeChiffreLeplusGrandDuneListe(listeAuHasard))


# Exercice 2

listeAuHasard = genereUnListeDeChiffreAuHasard()
print("Liste de chiffre")
print(listeAuHasard)
plusGrand, plusPetit = retourneLeChiffreLeplusGrandEtLePlusPetitDuneListe(
    listeAuHasard)
print("Le chiffre le plus grand est %s et le plus petit est %s" %
      (plusGrand, plusPetit))

# Exercice 3

listeAuHasard = genereUnListeDeChiffreAuHasard()
print("Liste de chiffre")
print(listeAuHasard)
somme = retourneLaSommeDeLaListe(
    listeAuHasard)
print("La somme de la liste est %s" %
      (somme))
