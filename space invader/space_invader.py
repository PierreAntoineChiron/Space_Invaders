"""
Que fait le programme : Programme principal du SpaceInvaders
Qui l'a fait : Pierre-Antoine Chiron , Morgan Conche
Quand :Depuis le 16/12/2021
"""

#Importation des bibliotheques nécessaires
import tkinter as tk
from random import randint
from sqlalchemy import false

#Objets
Partie_en_cours = False

class Protection:     
    def __init__(self,PosX,PosY): #Initialise les arguments de l'affichage des protections
        self.x = PosX
        self.y = PosY
        self.apparence=canevas.create_image(self.x,self.y,anchor='nw',image=ImgMur)
    
    
class VaisseauAllie:
    def __init__(self,posX,posY): #Initialise les arguments du vaisseau allié ainsi que son aparence
        self.x=posX
        self.y=posY
        self.apparence=canevas.create_image(self.x,self.y,anchor='center',image=ImgVaisseau)

    def deplacement(self,direction):  #Gère le déplacement du vaisseau et sa collision avec le bord de la fenêtre
        if self.x>=45 and direction==-1:
            self.x+=15*direction
        elif self.x<=960-45 and direction==1:
            self.x+=15*direction
        canevas.coords(self.apparence,self.x,self.y)
        
        
class Invader:
    Compteur = 0
    def __init__(self):  #Initialisation des aliens avec arguments par alien (self.{argument}), ou de groupe (Invader.{argument})
        self.Compteur=Invader.Compteur
        self.x=self.Compteur*(20+70) + 10
        self.vivant=True
        Invader.y = 120
        Invader.direction=1
        Invader.vitesse=0.7
        Invader.Compteur+=1
        self.apparence=canevas.create_image(self.x,self.y,anchor='nw',image=ImgAlien)
        
    def affichage(self):  #affichage des aliens
        canevas.coords(self.apparence,self.x,self.y)
        
class InvaderBonus:
    def __init__(self): #Initialisation de l'aliens bonus
        self.x = 480
        self.vivant=True
        self.y = 20
        self.direction=1
        self.vitesse=0.7
        self.apparence=canevas.create_image(self.x,self.y,anchor='nw',image=ImgAlienBonus)
        
    def affichage(self):   #Fonction nécéssaire car appelée après
        canevas.coords(self.apparence,self.x,self.y)
        

class TirsInvaders: 
    def __init__(self,i):   #Initialise les arguments des missiles des aliens
        self.x = ListeEnnemis[i].x + 35 
        self.y = ListeEnnemis[i].y +33
        self.apparence = canevas.create_line(self.x , self.y-10 , self.x ,self.y , fill='yellow')
        self.existe = True
        self.deplacement_tir_invader()
        
    def affichage_tir_invader(self):   #Création des tirs
        canevas.coords(self.apparence , self.x , self.y-8 , self.x , self.y)
        
    def deplacement_tir_invader(self):   #Déplacement des tirs des aliens
        if self.existe:
            self.y += 1
            self.affichage_tir_invader()
            self.fin_tir_invader()
            gamewindow.after(5,self.deplacement_tir_invader)
            
    def fin_tir_invader(self):  #Gère la "fin de vie" des tirs aliens, par collision avec les bord de la fenêtre, le vaisseau allié ou les protections
        global Vies
        if self.y >= 720:
            canevas.delete(self.apparence)
            del TirsAliens[0]
        elif self.y >= vaisseau.y - 5 and self.y <= vaisseau.y + 24 and self.x <= vaisseau.x + 23 and self.x >= vaisseau.x - 23:
            canevas.delete(self.apparence)
            del TirsAliens[0]
            Vies -= 1
            affichage_vies(Vies)
            if Vies <= 0:
                partie_perdue()
        elif self.y>= mur1.y and self.y<= mur1.y+35 and self.x>=mur1.x and self.x<=mur1.x+100:
            canevas.delete(self.apparence)
            del TirsAliens[0]
        elif self.y>= mur2.y and self.y<= mur2.y+35 and self.x>=mur2.x and self.x<=mur2.x+100:
            canevas.delete(self.apparence)
            del TirsAliens[0]
        elif self.y>= mur3.y and self.y<= mur3.y+35 and self.x>=mur3.x and self.x<=mur3.x+100:
            canevas.delete(self.apparence)
            del TirsAliens[0]
        
        

liste_tire_allie=[]
class Tire_allié:
    def __init__(self):   #Initialise les arguments des missiles du vaisseau 
        self.x=vaisseau.x
        self.y=vaisseau.y-30
        self.tire=canevas.create_line(self.x,self.y,self.x,self.y-10, fill="red")
        self.deplacement_tire()
    
    def affichage(self):  #affiche les tires 
        canevas.coords(self.tire , self.x , self.y , self.x , self.y-5)

    def deplacement_tire(self): #Gère la "fin de vie" des tirs du vaisseau, par collision avec les bord de la fenêtre, les aliens
        self.y-=5
        canevas.coords(self.tire , self.x , self.y , self.x , self.y-5)
        if not self.y<0 :
            gamewindow.after(5,self.deplacement_tire)
        elif self.y>=Boss.y and self.y<=Boss.y + 79 and self.x>=Boss.x and self.x<=Boss.x + 109:
            canevas.delete(Boss)
            canevas.delete(self)
        else: 
            for i in ListeEnnemis:
                if self.y>=i.y+33 and self.y<=i.y and self.x>=i.x and self.x<=i.x+70 :
                    canevas.delete(self)
                    del liste_tire_allie[0]


class TirsInvadersBonus:      #Classe similaire à la classe TireInvaders : Crée, affiche, gère le mouvement et la fin de vie des tirs de l'ennemi bonus

    def __init__(self):
        self.x = Boss.x
        self.y = Boss.y + 80
        self.apparence = canevas.create_rectangle(self.x -2 , self.y-2 , self.x + 2 ,self.y + 20 ,fill='green')
        self.existe = True
        self.deplacement_tir_invader_bonus()
        
    def affichage_tir_invader_bonus(self):
        canevas.coords(self.apparence , self.x  -2 , self.y-2 , self.x + 2, self.y + 20)
        
    def deplacement_tir_invader_bonus(self):
        if self.existe:
            self.y += 1.5
            self.affichage_tir_invader_bonus()
            self.fin_tir_invader_bonus()
            gamewindow.after(5,self.deplacement_tir_invader_bonus)
            
    def fin_tir_invader_bonus(self):
        global Vies
        if self.y >= 720:
            canevas.delete(self.apparence)
            del TirsAliens[0]
        elif self.y >= vaisseau.y - 24 and self.y <= vaisseau.y + 24 and self.x <= vaisseau.x + 24 and self.x >= vaisseau.x - 24:
            canevas.delete(self.apparence)
            del TirsAliens[0]
            Vies -= 2
            affichage_vies(Vies)
            if Vies <= 0:
                partie_perdue() 
        elif self.y>= mur1.y and self.y<= mur1.y+35 and self.x>=mur1.x and self.x<=mur1.x+100:
            canevas.delete(self.apparence)
            del TirsAliens[0]
        elif self.y>= mur2.y and self.y<= mur2.y+35 and self.x>=mur2.x and self.x<=mur2.x+100:
            canevas.delete(self.apparence)
            del TirsAliens[0]
        elif self.y>= mur3.y and self.y<= mur3.y+35 and self.x>=mur3.x and self.x<=mur3.x+100:
            canevas.delete(self.apparence)
            del TirsAliens[0]
            

    

        




#Fonctions
def action_clavier(event): #Permet au vaisseau allié de bouger avec les touches 'q', 'd', flèche gauche ou flèche droite    
    touche=event.keysym
    if touche=='q' or touche=='Left':
        vaisseau.deplacement(-1)
    elif touche=='d' or touche=='Right':
        vaisseau.deplacement(1)
    elif touche=="space":
        liste_tire_allie.append(Tire_allié())
            

def mouvement_invaders(): #Mouvement par bloc et collision des Invaders avec le bords de la fenêtre de jeu (Regarde quels aliens sont vivants et augmente la vitesse de ceux-ci lorsqu'un meurt)
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
            
def mouvement_invader_bonus(): #Mouvement du "Boss"
    global Boss
    if (Boss.x + 110/2 >= 960 and Boss.direction==1) or (Boss.x - 70<=0 and Boss.direction==-1):
        Boss.direction *= -1
    Boss.x+=Boss.vitesse*Boss.direction
    Boss.affichage()
    gamewindow.after(20,mouvement_invader_bonus)

TirsAliens = []
def tirs_invaders(): #Création des tirs des aliens toutes les 0.2 secondes
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
def tirs_invader_bonus():  #Création des tirs de l'aliens toutes les 1.5 secondes
    global Boss, TirsInvadersBonus   
    if Partie_en_cours:
        TirsBoss.append(TirsInvadersBonus())
        gamewindow.after(1500,tirs_invader_bonus)
    else:
        gamewindow.after(1,tirs_invader_bonus)

def partie_perdue():  #Ferme la fenêtre de jeu et propose de rejouer lorsque la partie est perdue
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

def nouvelle_partie():  #Ouvre la fenêtre de jeu quand le bouton jouer ou rejouer est préssé
    global alien, vaisseau, vies, Partie_en_cours, ListeEnnemis, Vies ,Boss,mur1,mur2,mur3
    canevas.grid()     #Paragraphe créant la fenêtre de jeu
    canevas.create_image(0,0,anchor='nw',image=ImgEspace)
    winlose.grid_remove()
    BoutonJouer.grid_remove()
    vaisseau=VaisseauAllie(480,650)
    mur1=Protection(100,500)
    mur2=Protection(430,500)
    mur3=Protection(800,500)
    Partie_en_cours=True
    Vies = 12
    Boss = InvaderBonus()  #Crée l'alien bonus, lance son mouvement et ses tirs
    mouvement_invader_bonus()
    tirs_invader_bonus()
    ListeEnnemis=[]   #Crée la ligne d'aliens, lance leur mouvement et leurs tirs
    Invader.Compteur=0
    for i in range(9):
        ListeEnnemis.append(Invader())
    mouvement_invaders()
    tirs_invaders()
    affichage_vies(Vies)


def affichage_vies(vies):  #Affiche les vies restantes
    NbVies.config(text='Vies: '+str(vies))

#Fenètre de jeu
gamewindow = tk.Tk()
gamewindow.title("Space Invaders")
ImgVaisseau=tk.PhotoImage(file='spaceship.gif')    #Images du fond de la fenêtre ainsi que toutes les entités existantes (hormis les tirs)
ImgAlien=tk.PhotoImage(file='invader.gif')
ImgEspace=tk.PhotoImage(file='space.gif')
ImgAlienBonus=tk.PhotoImage(file='invader_bonus.gif')
ImgMur=tk.PhotoImage(file='mur.gif')
NbVies=tk.Label(gamewindow,text="Vies: 3")     #Permet d'afficher les vies 
NbVies.grid(row=1,column=2)
BoutonJouer=tk.Button(gamewindow,text='Jouer',command=nouvelle_partie)   #Bouton pour lancer une partie
BoutonJouer.grid(row=0,column=1)
canevas=tk.Canvas(gamewindow,height=720,width=960, bg='black')    #Fenêtre de jeu et initialisation de la reconnaissance des touches du clavier
canevas.grid(row=2,column=1,columnspan=2)
canevas.grid_remove()
canevas.focus_set()
canevas.bind('<Key>',action_clavier)
BoutonQuitter=tk.Button(gamewindow,text='Quitter',command=gamewindow.destroy)  #Quitte le jeu
BoutonQuitter.grid(row=0,column=2)
winlose=tk.Label(gamewindow,text='Vous avez gagné')
winlose.grid(row=1,column=0)
winlose.grid_remove()
gamewindow=tk.mainloop()
