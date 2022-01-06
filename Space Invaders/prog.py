"""
Que fait le programme : Programme principal du SpaceInvaders
Qui l'a fait : Pierre-Antoine Chiron , Morgan Conche
Quand :169/12/2021
Que reste t-il? : Plein de choses
"""

#Importation des bibliotheques nécessaires
from tkinter import Tk,Label,Button,Canvas,Menu,PhotoImage

#Fonctions importantes
class Ennemis():
    def __init__(self, coords, color):
        self.coords = coords
        self.color = color

    def draw(self, canvas):
        """Draw the rectangle on a Tk Canvas."""
        canvas.create_rectangle(*self.coords, fill=self.color)
        
def deplacement():
    global X,Y,DX,DY,largeur,hauteur
    
    if X+20+DX > largeur:
        X = 2*(largeur-20)-X
        DX = -DX
        Y += 30

    if X-20+DX < 0:
        X = 2*20-X
        DX = -DX
        Y += 30

    X += DX
    canevas.coords(Alien,X-20,Y-10,X+20,Y+10)

    mafenetre.after(50,deplacement)

    if Y >= 530:
        canevas.delete(Alien)
        canevas.delete(Vaisseau)
        canevas.create_text(400,300,text="Vous avez perdu", fill="black", font="Helvetica 15 bold")

#Programme principal

#Crétion de la fenètre principale
mafenetre = Tk()
mafenetre.title('SpaceInvaders : Hell Edition')

#Création du canvas
largeur = 800
hauteur = 600
canevas = Canvas(mafenetre, width = largeur, height = hauteur, bg = 'grey')
canevas.pack(padx =5, pady =5)

#Création du vaisseau alien
Alien = Ennemis((380,20,420,40), 'blue')
Alien.draw(canevas)

#Création du vaisseau allié
Vaisseau = canevas.create_rectangle(380,530,420,550, outline = 'black', fill = 'green')

#Mouvement de l'alien
X = largeur/2
Y = 30
DX = 5
deplacement()

#Mouvement du vaisseau allié
PosX = largeur/2
PosY = 570

def bouger_droite(event):
    canevas.move(Vaisseau,10,0)
def bouger_gauche(event):
    canevas.move(Vaisseau,-10,0)
def bouger_haut(event):
    canevas.move(Vaisseau,0,-10)
def bouger_bas(event):
    canevas.move(Vaisseau,0,10)
    
canevas.bind_all('<Right>', bouger_droite)
canevas.bind_all('<Left>', bouger_gauche)
canevas.bind_all('<Up>', bouger_haut)
canevas.bind_all('<Down>', bouger_bas)

#Affichage du score
LabelScore = Label(mafenetre, text = 'Score : 0', fg = 'black')
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