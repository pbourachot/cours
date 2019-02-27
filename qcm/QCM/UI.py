

import tkinter
import tkinter.ttk as ttk
import Questions
from tkinter.messagebox import showinfo,showerror
import os.path


FILE_QUESTION = os.path.join(os.path.dirname(os.path.abspath(__file__)),'question.csv')


root = tkinter.Tk()
root.title("Mon QCM")
root.minsize(1000,450)
root.maxsize(1400,850)
#root.geometry(1400,850)

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

        self.questionnaire = None
        self.questionEnCours = None

        # On initialize la position des Widgets
        #self.initPosition()

        # Menu
        menubar = tkinter.Menu(root)
        partiebar = tkinter.Menu(menubar,tearoff=0)

        apropos = tkinter.Menu(menubar,tearoff=0)
        
        menubar.add_cascade(label="Partie", menu=partiebar)
        partiebar.add_command(label="Nouvelle Partie", command=self.nouvellePartie)
        partiebar.add_separator()
        partiebar.add_command(label="Propriete", command=self.propriete)
        partiebar.add_separator()
        partiebar.add_command(label="Quitter", command=self.quitter)

        menubar.add_cascade(label="A Propos", menu=apropos)
        apropos.add_command(label="Version", command=self.version)

        root.config(menu=menubar)

    # Quitte
    def quitter(self):
        root.quit()


    def version(self):
        print ("TODO")

    def propriete(self):
        print ("TODO")

    # Lance une nouvelle Partie
    def nouvellePartie(self):
        
        # initialize les widgets
        self.initPosition()
       #self.nouvelleQuestion()

        self.questionnaire = Questions.Questionnaire('question.csv')
        self.questionEnCours = self.questionnaire.retourneUnequestionAuHasard()
        self.afficheQuestion(self.questionEnCours)

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
        self.intituleQuestion.config(text=question.enonce)

        # met a jour les reponses
        reponses = question.reponses
        self.reponse1.config(text=reponses[0], value=reponses[0])
        self.reponse2.config(text=reponses[1], value=reponses[1])
        self.reponse3.config(text=reponses[2], value=reponses[2])

    # On valide la reponse
    def valider(self):
        print("La reponse proposee est %s" % self.reponseValue.get())

        resultat = self.questionEnCours.reponseValide(self.reponseValue.get())

        if (resultat):
            showinfo("Bonne Reponse")
        else :
            showerror("Mauvaise reponse")
        

    # Afficher une nouvelle question
    def nouvelleQuestion(self):
        self.questionEnCours = self.questionnaire.retourneUnequestionAuHasard()
        self.afficheQuestion(self.questionEnCours)


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
