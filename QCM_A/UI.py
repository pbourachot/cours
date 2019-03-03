

import tkinter
import tkinter.ttk as ttk
import Questions
from Questions import Questionnaire
from tkinter.messagebox import showinfo,showerror
from tkinter import Toplevel, Message, Button
import os
root = tkinter.Tk()
root.title("Mon QCM")
root.minsize(1000,450)
root.maxsize(1400,850)
# Cette classe represente une question

DATA_FOLDER = os.path.join(os.path.dirname(__file__),'data')
QUESTION_FILE = os.path.join(DATA_FOLDER,'question.csv')

class QuestionUI:

    # Constructeur
    def __init__(self):

        # Label pour l'intitule de la question
        self.intituleQuestion = tkinter.Label(text="Question")
        self.reponseValue = tkinter.StringVar(value="defaultValue")

        self.questionnaire = None
        self.question = None

        # COMPTEUR self.compteur=0  fois 3
        self.compteurQuestions = 0
        self.bonneReponse = 0
        self.mauvaiseReponse = 0

        # 3 RadioButtons pour les questions
        self.reponse1 = tkinter.Radiobutton(
            variable=self.reponseValue, text="reponse1", value='a')
        self.reponse2 = tkinter.Radiobutton(
            variable=self.reponseValue, text="reponse2", value='b')
        self.reponse3 = tkinter.Radiobutton(
            variable=self.reponseValue, text="reponse3", value='c')

        # Button pour valider, en cliquand sur le bouton valider, on validera la reponse
        #### self.button = ttk.Button(root, text="Valider", command=self.valider)

        # Button pour valider, en cliquand sur le bouton valider, on validera la reponse
        self.buttonNouvelleQuestion = ttk.Button(root, text="Question Suivant", command=self.nouvelleQuestion, state=tkinter.DISABLED)

        

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
        

        self.frameBas = tkinter.Frame(root)
        self.frameBas.pack(side=tkinter.BOTTOM)
        
        self.labelTheme = tkinter.Label(self.frameBas ,text="Theme")
        self.labelCommentaire = tkinter.Label(self.frameBas ,text="Choisissez une nouvelle partie")
        self.labelResultat = tkinter.Label(self.frameBas ,text="Question justes: 0/0 ")
        
        
        self.labelTheme.pack(side=tkinter.LEFT, padx=5, pady=5)
        self.labelCommentaire.pack(side=tkinter.LEFT, padx=5, pady=5)
        self.labelResultat.pack(side=tkinter.RIGHT, padx=5, pady=5)

        

        root.config(menu=menubar)


     # Initialization des widgets, les uns apres les autres
    def initPosition(self):
        
        self.intituleQuestion.pack()
        self.reponse1.pack()
        self.reponse2.pack()
        self.reponse3.pack()
        #self.button.pack()
        self.buttonNouvelleQuestion.pack()

        
    
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
        self.questionnaire = Questionnaire(QUESTION_FILE)
        #self.questionnaire.affichage()
        q = self.questionnaire.retourneUnequestionAuHasard()
        self.afficheQuestion(q)
        
        self.labelTheme['text'] = QUESTION_FILE


    def quitter(self):
        root.quit()

   
    
    # On afficher une question particuliere
    # Parametre de la fonction : question
    def afficheQuestion(self, question):
        self.question = question
        # met a jour l'intitule de la question
        self.intituleQuestion.config(text=question.enonce)

        # met a jour les reponses
        reponses = question.reponses
        self.reponse1.config(text=reponses[0], value=reponses[0], command = lambda : self.valide2(self.reponse1))
        self.reponse2.config(text=reponses[1], value=reponses[1], command = lambda : self.valide2(self.reponse2))
        self.reponse3.config(text=reponses[2], value=reponses[2], command = lambda : self.valide2(self.reponse3))

    # On valide la reponse
    def valider(self):
        reponseCorrect = self.question.reponseValide(self.reponseValue.get())
        if reponseCorrect :
            showinfo('bonne reponse')
        else :
            showerror('mauvaise reponse')
        #print("La reponse proposee est %s" % self.reponseValue.get())

    def valide2(self, widget):
        
        print (self.reponseValue.get())
        reponseCorrect = self.question.reponseValide(self.reponseValue.get())
        if reponseCorrect :
            #showinfo('bonne reponse')
            self.labelCommentaire.config(text = "Bonne reponse", background = 'blue2')
        else :
            self.labelCommentaire.config(text = "Mauvaise reponse", background = 'red')
            #showerror('mauvaise reponse')



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
