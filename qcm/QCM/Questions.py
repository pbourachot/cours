import random

import pickle

from random import randrange

class Question:

    def __init__(self, enonce, reponsea, reponseb, reponsec):
        self.enonce = enonce
        self.bonnereponse= reponsea
        self.reponses=[reponsea, reponseb, reponsec]
        random.shuffle(self.reponses)

    def affichage(self):
        print("%s" %(self.enonce))
        for reponse in self.reponses:
            print(reponse)
        #print("a) %s" %(self.reponsea))
        #print("b) %s" %(self.reponseb))
        #print("c) %s" %(self.reponsec))

    def validerReponse(self):
        key = input("quelle est votre reponse ")
        #print(key)
        if key == self.bonnereponse:
            print("juste")
        else :
            print("faux")

    def reponseValide(self,reponse):
        if reponse == self.bonnereponse:
            return True
        else :
            return False




def sauveQ(question):
    pickle.dump(question, open('mypicklefile', 'wb'))
    #print("sauveQ")

def lireQ():
    Q = pickle.load(open('mypicklefile', 'rb'))
    return Q

def lireQcsv():
    quest = Questionnaire()
    fichier=open('question.csv')
    lignes=fichier.readlines()
    fichier.close()
    print(lignes)
    #Q1 = Question("quelle est la capitale de la France?", "Paris", "Marseille", "Nice")
    for ligne in lignes:
        ligne = ligne.strip()
        print(" je doies creer une question a partir de [%s]" %ligne)
        value = ligne.split(';')
        
        print(value)
        
        enonce = value[0]
        reponsea = value[1]
        reponseb = value[2]
        reponsec= value[3]

        Q1 = Question(enonce, reponsea, reponseb, reponsec)
        Q1.affichage()
        quest.rajouteQ(Q1)
    return quest

    
class Questionnaire:

    # Constructeur par defaut
    def __init__(self, fichier=None):
        self.questions = []

        if (fichier != None):
            fichier=open(fichier)
            lignes=fichier.readlines()
            fichier.close()

            for ligne in lignes:
                value = ligne.split(';')
                enonce = value[0]
                reponsea = value[1]
                reponseb = value[2]
                reponsec= value[3]

                Q1 = Question(enonce, reponsea, reponseb, reponsec)
                self.rajouteQ(Q1)
            


    
    # affiche des informations sur un questionnaire
    def affichage(self):
        print("Ce questionnaire a %s question(s)" %len(self.questions))

    # rajoute une question au questionnaire
    def rajouteQ(self,question):
        self.questions.append(question)

    # retourne une question au hasard
    def retourneUnequestionAuHasard(self):
        print ("Affiche une question au hasard")
        nb = randrange(0, len(self.questions))
        return self.questions[nb]
        #random, len(self.questions)

    # Retourne une liste de nb questions
    def retourneListeDeQuestion(self, nbDequestions):

        random.shuffle(self.questions)
        return self.questions[0:nbDequestions]


######################




ques = lireQcsv() 
ques.affichage()

ques.retourneUnequestionAuHasard()

