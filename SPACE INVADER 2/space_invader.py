"""
Que fait le programme : Programme principal du SpaceInvaders
Qui l'a fait : Pierre-Antoine Chiron , Morgan Conche
Quand :Depuis le 16/12/2021
Que reste t-il? : Tirs alliés et ennemis, plusieurs alliés, collisions, mouvement des ennemis
"""

#Importation des bibliotheques nécessaires
import tkinter as tk

#Objets
class VaisseauAllie:
    def __init__(self,posX,posY):

        self.x=posX
        self.y=posY
        self.apparence=canevas.create_image(self.x,self.y,anchor='center',image=ImgVaisseau)

    def deplacement(self,direction):
        if self.x>=45 and direction==-1:
            self.x+=15*direction
        elif self.x<=960-45 and direction==1:
            self.x+=15*direction
        canevas.coords(self.apparence,self.x,self.y)
        
class Invader:
    def __init__(self,nombre_aliens):
        self.nombre_aliens = nombre_aliens
        self.x=self.nombre_aliens*(20+70)
        self.y = 50
        #Pas d'aliens se créent :)))
        self.apparence=canevas.create_image(self.x,self.y,anchor='nw',image=ImgAlien)
        
        canevas.coords(self.apparence,self.x,self.y)
            
        
        
        


#Fonctions
def action_clavier(event):
    touche=event.keysym
    if touche=='q' or touche=='Left':
        vaisseau.deplacement(-1)
    elif touche=='d' or touche=='Right':
        vaisseau.deplacement(1)

def nouvelle_partie():
    global alien, vaisseau, vies
    canevas.grid()
    canevas.create_image(0,0,anchor='nw',image=ImgEspace)
    winlose.grid_remove()
    BoutonJouer.grid_remove()
    vaisseau=VaisseauAllie(480,650)
        
    
    affichage_vies(3)

def affichage_vies(vies):
    NbVies.config(text='Vies: '+str(vies))



#Fenètre de jeu
gamewindow = tk.Tk()

ImgVaisseau=tk.PhotoImage(file='spaceship.gif')
ImgAlien=tk.PhotoImage(file='invader.gif')
ImgEspace=tk.PhotoImage(file='space.gif')

NbVies=tk.Label(gamewindow,text="Vies: 3")
NbVies.grid(row=1,column=2)

BoutonJouer=tk.Button(gamewindow,text='Jouer',command=nouvelle_partie)
BoutonJouer.grid(row=0,column=1)

canevas=tk.Canvas(gamewindow,height=720,width=960, bg='black')
canevas.grid(row=2,column=1,columnspan=2)
canevas.grid_remove()
canevas.focus_set()
canevas.bind('<Key>',action_clavier)

BoutonQuitter=tk.Button(gamewindow,text='Quitter',command=gamewindow.destroy)
BoutonQuitter.grid(row=0,column=2)

winlose=tk.Label(gamewindow,text='Gagne')
winlose.grid(row=1,column=0)
winlose.grid_remove()

gamewindow=tk.mainloop()
