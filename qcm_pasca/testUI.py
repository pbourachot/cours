
from tkinter import * 

fenetre = Tk()



# liste
liste = Listbox(fenetre)
liste.insert(1, "Q1")
liste.insert(2, "Q2")
liste.insert(3, "Q3")
liste.insert(4, "Q4")

liste.pack()

fenetre.mainloop()