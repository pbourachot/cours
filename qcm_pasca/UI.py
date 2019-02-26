

import tkinter
import tkinter.ttk as ttk
import Question

root = tkinter.Tk()

# Cette classe represente une question


class QuestionUI:

    # Constructeur
    def __init__(self):

        # Label pour l'intitule de la question
        self.intituleQuestion = tkinter.Label(text="Question")
        self.reponseValue = tkinter.StringVar(value="defaultValue")

        # 3 RadioButtons pour les questions
        self.reponse1 = tkinter.Radiobutton(
            variable=self.reponseValue, text="reponse1", value='a')
        self.reponse2 = tkinter.Radiobutton(
            variable=self.reponseValue, text="reponse2", value='b')
        self.reponse3 = tkinter.Radiobutton(
            variable=self.reponseValue, text="reponse3", value='c')

        # Button pour valider, en cliquand sur le bouton valider, on validera la reponse
        self.button = ttk.Button(root, text="Valider", command=self.valider)

        # Button pour valider, en cliquand sur le bouton valider, on validera la reponse
        self.buttonNouvelleQuestion = ttk.Button(root, text="Nouvelle", command=self.nouvelleQuestion)

        # On initialize la position des Widgets
        self.initPosition()

    # Initialization des widgets, les uns apres les autres
    def initPosition(self):

        self.intituleQuestion.pack()
        self.reponse1.pack()
        self.reponse2.pack()
        self.reponse3.pack()
        self.button.pack()
        self.buttonNouvelleQuestion.pack()

    # On afficher une question particuliere
    # Parametre de la fonction : question
    def afficheQuestion(self, question):

        # met a jour l'intitule de la question
        self.intituleQuestion.config(text=question.intitule)

        # met a jour les reponses
        reponses = question.getProposition()
        self.reponse1.config(text=reponses[0], value=reponses[0])
        self.reponse2.config(text=reponses[1], value=reponses[1])
        self.reponse3.config(text=reponses[2], value=reponses[2])

    # On valide la reponse
    def valider(self):
        print("La reponse proposee est %s" % self.reponseValue.get())

    # Afficher une nouvelle question
    def nouvelleQuestion(self):
        print ("Affiche une nouvelle question")
        q1 = Question.Question("Capitale", "Paris", ["Lyon", "Marseille"])
        self.afficheQuestion(q1)

def print_file():                     # voir le chapitre sur les événements
    print("Valider")


'''
v = tkinter.IntVar()


b = ttk.Button(root, text="Valider")
b.config(command=print_file)         # idem
b.pack()
'''

UI = QuestionUI()


#q1 = Question.Question("Capitale", "Paris", ["Lyon", "Marseille"])
#q2 = Question.Question("1+1", "2", ["3", "4"])

#UI.afficheQuestion(q1)


root.mainloop()
