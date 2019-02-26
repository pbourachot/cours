import turtle as tu


#Recommencer
#Sauver
#Charger
#Jouer
#Verifier

def click(x,y):    
    print("Click %s %s " %(x,y))

    

def menu(num, text):
    tu.pu()
    tu.goto( 60*num +10 , 450)        
    tu.pd()
    tu.goto( 60*num +10 +60 , 450)        
    tu.goto( 60*num +10 +60 , 475)        
    tu.goto( 60*num +10 , 475)        
    tu.goto( 60*num +10, 450)        
    tu.pu()
    tu.goto(60*num +10 + 10 , 450 +10)
    tu.write(text)

def dessinePiece(x,y):
    tu.pu()
    tu.goto(x + 60*x +10 , y + 60*y + 30)        
    tu.pd()
    tu.circle(20)

def initialiseTableau():

    #Initialize le tableau et la tortue
    tu.setworldcoordinates(0,0,430,480)    
    tu.pensize(1)
    tu.speed(0)

    
    # Colonne
    for i in range(0,8):
        tu.pu()
        tu.goto(i + i*60,366)        
        tu.pd()
        tu.goto(i + i*60,0)        

    # ligne
    for i in range(0,7):
        tu.pu()
        tu.goto(0,i + 60*i)        
        tu.pd()
        tu.goto(427,i+60*i)

    tu.right(90)
    for x in range(0,7):
        for y in range(0,6):
            dessinePiece(x,y)
    
    menu(0,'Recommencer')
    menu(1,'Sauvegarder')
    menu(2,'Charger')
    menu(3,'Verifier')
    
    tu.onscreenclick(click)        
    


def main():

    #initialize la tortue


    #initialize le tableau de jeu
    initialiseTableau()


    # 




if __name__ == '__main__':
    main()
    tu.TK.mainloop()