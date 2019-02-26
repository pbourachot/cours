1) Deux fichiers questions
exemple : animaux.csv
          geologie.csv


2) Exercice1 et Exercice2


 # Menu
        menubar = tkinter.Menu(root)
        partiebar = tkinter.Menu(menubar,tearoff=0)
        
        menubar.add_cascade(label="Partie", menu=partiebar)
        partiebar.add_command(label="Nouvelle Partie", command=self.nouvellePartie)
        partiebar.add_separator()
        partiebar.add_command(label="Quitter", command=self.quitter)

        root.config(menu=menubar)