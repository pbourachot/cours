import random

import pickle

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

    def reponseValide(self, reponse):
        if reponse == self.bonnereponse :
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


    def __init__(self,nomDeFichier=None):
        self.questions = []

        if (nomDeFichier != None):
            fichier=open(nomDeFichier)
            lignes=fichier.readlines()
            fichier.close()
            
            for ligne in lignes:
                ligne = ligne.strip()
        
                value = ligne.split(';')
        
               
                enonce = value[0]
                reponsea = value[1]
                reponseb = value[2]
                reponsec= value[3]

                Q1 = Question(enonce, reponsea, reponseb, reponsec)
        
                self.rajouteQ(Q1)

    def affichage(self):
        print("Ce questionnaire a %s question(s)" %len(self.questions))

    def rajouteQ(self,question):
        self.questions.append(question)

    def retourneUnequestionAuHasard(self):
        print ("Affiche une question au hasard")
        from random import randrange
        nb = randrange(0, len(self.questions))

        return self.questions[nb] 


######################




ques = lireQcsv() 
ques.affichage()

ques2 = Questionnaire()
ques2.affichage()


ques3 = Questionnaire('question.csv')
ques3.affichage()

ques3 = Questionnaire('question2.csv')
ques3.affichage()
question = ques3.retourneUnequestionAuHasard()
question.affichage()




