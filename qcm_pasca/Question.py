import random
import pickle
import json
FICHIER = 'data.bin'
FICHIER_CSV = 'Classeur1.csv'


class Questionnaire:

    def __init__(self):
        self.questions = []

    def ajouteQuestion(self, question):
        self.questions.append(question)

#    def to_json(self):
#        return json.dumps(self, default=lambda o: o.__dict__,
#                          sort_keys=True, indent=4)


class Question:

    def __init__(self, intitule, bonneReponse, mauvaiseReponses):

        self.intitule = intitule
        self.bonneReponse = bonneReponse
        self.mauvaiseReponses = mauvaiseReponses

    def printQuestion(self):

        print(self.intitule)
        for rep in self.getProposition():
            print(rep)

    def printObject(self):
        print("Intitule => %s" % self.intitule)
        print("Bonne Reponse => %s" % self.bonneReponse)
        print("Mauvaises Reponses => %s" % self.mauvaiseReponses)

    def getProposition(self):
        propositions = []
        propositions.append(self.bonneReponse)
        propositions.extend(self.mauvaiseReponses)
        random.shuffle(propositions)
        return propositions

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


def save(object):
    fichier = open(FICHIER, 'wb')
    pickle.dump(object, fichier)
    #json.dumps(object, fichier)
    fichier.close()


def load():
    fichier = open(FICHIER, 'rb')
    question = pickle.load(fichier)
#    fichier.load(fichier)
    fichier.close()
    return question


def loadCSV(questionnaire):
    fichier = open(FICHIER_CSV, 'r')
    for line in fichier.readlines():
        print(line)
        tab = line.split(';')
        print (tab)



q1 = Question("Capitale", "Paris", ["Lyon", "Marseille"])
q2 = Question("1+1", "2", ["3", "4"])

questionnaire = Questionnaire()
questionnaire.ajouteQuestion(q1)
questionnaire.ajouteQuestion(q2)


save(q1)
print("==================")
q2 = load()
# q2.printObject()


import os

#loadCSV()