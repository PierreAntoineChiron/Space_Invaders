"""
Que fait le programme : Programme principal du SpaceInvaders
Qui l'a fait : Pierre-Antoine Chiron , Morgan Conche
Quand :169/12/2021
Que reste t-il? : Plein de choses
"""

#Importation des bibliotheques nécessaires
from tkinter import *

#Fonctions importantes
def deplacement():
    global X,Y,DX,DY,largeur,hauteur
    
    if X+20+DX > largeur:
        X = 2*(largeur-20)-X
        DX = -DX
        Y += 20
        
    if X-20+DX < 0:
        X = 2*20-X
        DX = -DX
        Y += 20
        
    X += DX
    
    canevas.coords(Alien,X-20,Y-10,X+20,Y+10)
    mafenetre.after(50,deplacement)

#fonction mouvement du vaisseau 
def bouger_droite(event,):
    canevas.move(Vaisseau,10,0)
    posX=365+10
def bouger_gauche(event,):
    canevas.move(Vaisseau,-10,0)
    posX=365-10
def bouger_haut(event,):
    canevas.move(Vaisseau,0,-10)
    posY=500-10
def bouger_bas(event,):
    canevas.move(Vaisseau,0,10)
    posY=500+10


    

#Programme principal

#Crétion de la fenètre principale
mafenetre = Tk()
mafenetre.title('SpaceInvaders : Hell Edition')

#Création du canvas
largeur = 800
hauteur = 600
canevas = Canvas(mafenetre, width = largeur, height = hauteur,)
canevas.pack(padx =5, pady =5) 

# ajouter un background
img = PhotoImage(file ="background.png")
canevas.create_image(0,0, image=img, anchor="nw")

#Création du vaisseau adverse
Alien = canevas.create_rectangle(300,20,420,40, outline = 'black', fill ='white')

#Création du vaisseau allié
img_allie = PhotoImage(file ="vaisseau_allié.png")
Vaisseau = canevas.create_image(365,500, image=img_allie, anchor="nw" )

#Mouvement de l'alien
X = largeur/2
Y = 30
DX = 3.5
deplacement()

#Mouvement du vaisseau allié
posX=365
posY=500

canevas.bind_all('<Right>', bouger_droite)
canevas.bind_all('<Left>', bouger_gauche)
canevas.bind_all('<Up>', bouger_haut)
canevas.bind_all('<Down>', bouger_bas)

if posY>600:
    Vaisseau = canevas.create_image(365,0, image=img_allie, anchor="nw" )
    

#Affichage du score
LabelScore = Label(mafenetre, text = 'Score : 100', fg = 'black')
LabelScore.pack()

#Boutons
BoutonJouer = Button(mafenetre,text = 'JOUER')
BoutonJouer.pack(side= 'left',padx =5, pady =5)

BoutonQuitter = Button(mafenetre, text='QUITTER', command = mafenetre.destroy)
BoutonQuitter.pack(side = 'right',padx =5, pady =5)

#Création du menu
mainmenu = Menu(mafenetre)
mainmenu.add_command(label = 'Rejouer')
mainmenu.add_command(label = 'Pause')
mainmenu.add_command(label = 'Parametres')
mainmenu.add_command(label = 'Règles du jeu')
mafenetre.config(menu = mainmenu)



mafenetre.mainloop()


