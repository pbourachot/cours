

import tkinter
import tkinter.ttk as ttk
import Questions
from Questions import Questionnaire
from tkinter.messagebox import showinfo,showerror
from tkinter import Toplevel, Message, Button
root = tkinter.Tk()
root.title("Mon QCM")
root.minsize(1000,450)
root.maxsize(1400,850)
# Cette classe represente une question


class QuestionUI:

    # Constructeur
    def __init__(self):

        # Label pour l'intitule de la question
        self.intituleQuestion = tkinter.Label(text="Question")
        self.reponseValue = tkinter.StringVar(value="defaultValue")

        self.questionnaire = None
        self.question = None

        # COMPTEUR self.compteur=0  fois 3

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

        

         # Menu
        menubar = tkinter.Menu(root)
        partiebar = tkinter.Menu(menubar,tearoff=0)
        aproposbar = tkinter.Menu(menubar, tearoff=0)

        menubar.add_cascade(label="Partie", menu=partiebar)
        partiebar.add_command(label="Nouvelle Partie", command=self.nouvellePartie)
        partiebar.add_separator()
        partiebar.add_command(label="Quitter", command=self.quitter)

        menubar.add_cascade(label="A Propos", menu=aproposbar)
        aproposbar.add_command(label="Version", command=self.version)
        

        root.config(menu=menubar)
    
    # Affiche la version
    def version(self):
        
        top = Toplevel(root)
        top.title("Au sujet de ce QCM")
        msg = Message(top, text="Version xx")
        msg.pack()
        button = Button(top, text="Fermer", command=top.destroy)
        button.pack()


    def nouvellePartie(self):
        # On initialize la position des Widgets
        self.initPosition()
        self.questionnaire = Questionnaire('question.csv')
        #self.questionnaire.affichage()
        q = self.questionnaire.retourneUnequestionAuHasard()
        self.afficheQuestion(q)
        
    def quitter(self):
        root.quit()

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
        self.question = question
        # met a jour l'intitule de la question
        self.intituleQuestion.config(text=question.enonce)

        # met a jour les reponses
        reponses = question.reponses
        self.reponse1.config(text=reponses[0], value=reponses[0])
        self.reponse2.config(text=reponses[1], value=reponses[1])
        self.reponse3.config(text=reponses[2], value=reponses[2])

    # On valide la reponse
    def valider(self):
        reponseCorrect = self.question.reponseValide(self.reponseValue.get())
        if reponseCorrect :
            showinfo('bonne reponse')
        else :
            showerror('mauvaise reponse')
        #print("La reponse proposee est %s" % self.reponseValue.get())

    # Afficher une nouvelle question
    def nouvelleQuestion(self):
       q = self.questionnaire.retourneUnequestionAuHasard()
       self.afficheQuestion(q)
       

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
