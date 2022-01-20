"""
Que fait le programme : Programme principal du SpaceInvaders
Qui l'a fait : Pierre-Antoine Chiron , Morgan Conche
Quand :Depuis le 16/12/2021
Que reste t-il? : Collisions des tirs alliés, protections, ennemi bonus
"""

#Importation des bibliotheques nécessaires
import tkinter as tk
from random import randint

#Objets
Partie_en_cours = False

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
    Compteur = 0
    def __init__(self):
        self.Compteur=Invader.Compteur
        self.x=self.Compteur*(20+70) + 10
        self.vivant=True
        Invader.y = 120
        Invader.direction=1
        Invader.vitesse=0.7
        Invader.Compteur+=1
        
        self.apparence=canevas.create_image(self.x,self.y,anchor='nw',image=ImgAlien)
        
    def affichage(self):
        canevas.coords(self.apparence,self.x,self.y)
        
class InvaderBonus():
    def __init__(self):
        self.x = 480
        self.vivant=True
        self.y = 20
        self.direction=1
        self.vitesse=0.7
        
        self.apparence=canevas.create_image(self.x,self.y,anchor='n',image=ImgAlienBonus)
        
    def affichage(self):
        canevas.coords(self.apparence,self.x,self.y)
        

class TirsInvaders:
    def __init__(self,i):
        self.x = ListeEnnemis[i].x + 35 
        self.y = ListeEnnemis[i].y +33
        self.apparence = canevas.create_line(self.x , self.y-10 , self.x ,self.y , fill='yellow')
        self.existe = True
        self.deplacement_tir_invader()
        
    def affichage_tir_invader(self):
        canevas.coords(self.apparence , self.x , self.y-8 , self.x , self.y)
        
    def deplacement_tir_invader(self):
        if self.existe:
            self.y += 1
            self.affichage_tir_invader()
            self.fin_tir_invader()
            gamewindow.after(5,self.deplacement_tir_invader)
            
    def fin_tir_invader(self):
        global Vies
        if self.y >= 720:
            self.existe = False
            canevas.delete(self.apparence)
            del TirsAliens[0]
        elif self.y >= vaisseau.y - 5 and self.y <= vaisseau.y + 24 and self.x <= vaisseau.x + 23 and self.x >= vaisseau.x - 23:
            self.existe = False
            canevas.delete(self.apparence)
            del TirsAliens[0]
            Vies -= 1
            affichage_vies(Vies)
            if Vies <= 0:
                partie_perdue()
        
class TirsInvadersBonus:
    def __init__(self):
        self.x = Boss.x
        self.y = Boss.y + 80
        self.apparence = canevas.create_rectangle(self.x -2 , self.y-2 , self.x + 2 ,self.y + 20 ,fill='green')
        self.existe = True
        self.deplacement_tir_invader_bonus()
        
    def affichage_tir_invader_bonus(self):
        canevas.coords(self.apparence , self.x -2 , self.y-2 , self.x + 2, self.y + 20)
        
    def deplacement_tir_invader_bonus(self):
        if self.existe:
            self.y += 1.5
            self.affichage_tir_invader_bonus()
            self.fin_tir_invader_bonus()
            gamewindow.after(5,self.deplacement_tir_invader_bonus)
            
    def fin_tir_invader_bonus(self):
        global Vies
        if self.y >= 720:
            self.existe = False
            canevas.delete(self.apparence)
            del TirsAliens[0]
        elif self.y >= vaisseau.y - 24 and self.y <= vaisseau.y + 24 and self.x <= vaisseau.x + 24 and self.x >= vaisseau.x - 24:
            self.existe = False
            canevas.delete(self.apparence)
            del TirsAliens[0]
            Vies -= 2
            affichage_vies(Vies)
            if Vies <= 0:
                partie_perdue()        
               
        
#Fonctions
def action_clavier(event):
    touche=event.keysym
    if touche=='q' or touche=='Left':
        vaisseau.deplacement(-1)
    elif touche=='d' or touche=='Right':
        vaisseau.deplacement(1)
            

def mouvement_invaders():
    global ListeEnnemis
    if Partie_en_cours:
        L=[i.vivant for i in ListeEnnemis]
        if True in L:
            i=L.index(True)
            L.reverse()
            j=L.index(True)
            if (ListeEnnemis[-j-1].x + 70>=960 and Invader.direction==1) or (ListeEnnemis[i].x <=0 and Invader.direction==-1):
                Invader.direction *= -1
                Invader.y += 20
                if Invader.y+33 >= 580:
                    partie_perdue()
            for i in ListeEnnemis:
                i.x+=Invader.vitesse*Invader.direction*((len(ListeEnnemis)/len(L)))
                i.affichage()
            gamewindow.after(20,mouvement_invaders)
            
def mouvement_invader_bonus():
    global Boss
    if (Boss.x + 110/2 >= 960 and Boss.direction==1) or (Boss.x - 70<=0 and Boss.direction==-1):
        Boss.direction *= -1
    Boss.x+=Boss.vitesse*Boss.direction
    Boss.affichage()
    gamewindow.after(20,mouvement_invader_bonus)

TirsAliens = []
def tirs_invaders():
    global TirsAliens,ListeEnnemis
    if Partie_en_cours:
        L = [i.vivant for i in ListeEnnemis]
        i = randint(0, len(ListeEnnemis)-1)
        if L[i]:
            TirsAliens.append(TirsInvaders(i))
            gamewindow.after(200,tirs_invaders)
        else:
            gamewindow.after(1,tirs_invaders)

TirsBoss = []
def tirs_invader_bonus():
    global Boss, TirsInvadersBonus   
    if Partie_en_cours:
        TirsBoss.append(TirsInvadersBonus())
        gamewindow.after(1500,tirs_invader_bonus)
    else:
        gamewindow.after(1,tirs_invader_bonus)

def partie_perdue():
    global Partie_en_cours, Partie_Perdue
    canevas.grid_remove()
    winlose.config(text='Perdu')
    winlose.grid()
    canevas.delete("all")
    BoutonJouer.grid()
    BoutonJouer.config(text='Rejouer')
    Invader.vitesse=0.7
    Partie_en_cours=False
    Partie_Perdue=True

def nouvelle_partie():
    global alien, vaisseau, vies, Partie_en_cours, ListeEnnemis, Vies ,Boss
    canevas.grid()
    canevas.create_image(0,0,anchor='nw',image=ImgEspace)
    winlose.grid_remove()
    BoutonJouer.grid_remove()
    vaisseau=VaisseauAllie(480,650)
    Partie_en_cours=True
    Vies = 12
    
    Boss = InvaderBonus()
    mouvement_invader_bonus()
    tirs_invader_bonus()
    
    ListeEnnemis=[]
    Invader.Compteur=0
    for i in range(9):
        ListeEnnemis.append(Invader())
    mouvement_invaders()
    tirs_invaders()
        
    affichage_vies(Vies)


def affichage_vies(vies):
    NbVies.config(text='Vies: '+str(vies))



#Fenètre de jeu
gamewindow = tk.Tk()

gamewindow.title("Space Invaders")

ImgVaisseau=tk.PhotoImage(file='spaceship.gif')
ImgAlien=tk.PhotoImage(file='invader.gif')
ImgEspace=tk.PhotoImage(file='space.gif')
ImgAlienBonus=tk.PhotoImage(file='invader_bonus.gif')

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

winlose=tk.Label(gamewindow,text='Vous avez gagné')
winlose.grid(row=1,column=0)
winlose.grid_remove()

gamewindow=tk.mainloop()