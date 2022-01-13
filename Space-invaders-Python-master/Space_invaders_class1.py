'''
BERTEAUX Vincent SILINSKI Remi
Groupe C
12/01/2017

To Do:
-Ajouter collision tir allie dans les protections
-Ajouter plusieurs lignes
-Alien Special
-liste Tirs plus propre
-cheatcodes
-commandes parametrables
'''

import tkinter as tk            #Tkinter ou tkinter
from random import randint
from time import time

##Initialisation et declaration de variables
#methode .height et .width de PhotoImage ne fonctionne pas donc oblige de hardcode les dimensions
#Partie
Partie_en_cours=False
Partie_Perdu=True
ViesInit=300

#Canevas
hauteur=480
largeur=640

#vaisseau
largeur_vaisseau=30
hauteur_vaisseau=32
posX=largeur/2
posY=hauteur-hauteur_vaisseau-5

#Aliens
largeur_alien=22      
hauteur_alien=16
ecart_alien=10
hauteur_alien_ligne1=50
nbre_alien_par_ligne=15
descente_alien=10
VitesseDeplacement=10
VitesseAlien=0.5
AccelerationAlien=0.05

#Protections
nbre_protections=4
posY_protections=posY-35
largeur_protections=1.5*largeur_vaisseau
hauteur_protections=15
resistance_protections=5

#tirs allies et ennemies
VitesseTir= 1
tps_entre_tir_alien=200  #rester au dessus de 50 pour eviter de planter
Tirs=[]
TempsTir=0
TirsAlien=[]
TempsEntreTirs=1

#Score et points
Score=0
PointsAlien=30

class Spaceship:
    
    def __init__(self):
        '''self.apparence=canevas.create_oval(posX-largeur_vaisseau/2,\
        posY-hauteur_vaisseau/2,posX+largeur_vaisseau/2,\
        posY+hauteur_vaisseau/2,width=2,outline='white')'''

        self.x=posX
        self.y=posY
        self.apparence=canevas.create_image(self.x,self.y,anchor='center',image=ImageVaisseau)


    def deplacement(self,dir):
        if self.x>=largeur_vaisseau and dir==-1:
            self.x+=VitesseDeplacement*dir
        elif self.x<=largeur-largeur_vaisseau and dir==1:
            self.x+=VitesseDeplacement*dir
        canevas.coords(self.apparence,self.x,self.y)
        
        
    def ViePerdue(self):
        canevas.itemconfig(self.apparence,image=ImageDestroy)
        mw.after(500,self.RetourApparenceNormale)
        
    def RetourApparenceNormale(self):
        canevas.itemconfig(self.apparence,image=ImageVaisseau)


class Alien:
    
    Compteur=0
    def __init__(self):
        Alien.Compteur += 1
        self.Compteur=Alien.Compteur
        self.vivant=True
        self.x=self.Compteur*(ecart_alien+largeur_alien)
        Alien.y=hauteur_alien_ligne1
        Alien.dir=1
        Alien.vitesse=VitesseAlien
    
    def Creation(self):
        #self.apparence=canevas.create_rectangle(self.x-largeur_alien/2,Alien.y-hauteur_alien/2,self.x+largeur_alien/2,Alien.y+hauteur_alien/2,width=2,outline='white')
        self.apparence=canevas.create_image(self.x,self.y,anchor='nw',image=ImageAlien)

    def Affichage(self):
        #canevas.coords(self.apparence , self.x-largeur_alien/2 ,Alien.y-hauteur_alien/2 , self.x+largeur_alien/2 ,Alien.y+hauteur_alien/2)
        canevas.coords(self.apparence,self.x,self.y)
    


class Tir:
    
    Compteur=0
    def __init__(self):
        self.x=vaisseau.x
        self.y=vaisseau.y
        self.apparence=canevas.create_line(self.x , self.y-4 , self.x ,\
        self.y , fill='white')
        self.encours=True
        Tir.Compteur+=1
    
    def Affichage(self):
        canevas.coords(self.apparence , self.x , self.y-4 , self.x , self.y)
    
    def Deplacement(self):
        if self.encours:
            self.y-=VitesseTir
            self.Affichage()
            self.FinTir()
            mw.after(5,self.Deplacement)
      

    def FinTir(self):
        if self.y<0:
            self.encours=False
            canevas.delete(self.apparence)
            del Tirs[0]
            Tir.Compteur-=1
        else:
            for i in ennemie:
                if i.vivant and self.y>=i.y and self.y<=i.y+hauteur_alien and self.x<=i.x+largeur_alien and self.x>=i.x:
                    self.Destruction()
                    canevas.delete(i.apparence)
                    i.vivant=False
                    Alien.vitesse+=AccelerationAlien
                    Points(PointsAlien)
                    PartieGagnee()


    def Destruction(self):
        self.encours=False
        canevas.delete(self.apparence)
        del Tirs[0]
        Tir.Compteur-=1
                    
class TirAlien:
    
    def __init__(self,i):
        self.x=ennemie[i].x
        self.y=ennemie[i].y
        self.apparence=canevas.create_line(self.x , self.y-4 , self.x ,\
        self.y , fill='white')
        self.encours=True
        self.Deplacement()

    def affichage(self):
        canevas.coords(self.apparence , self.x , self.y-4 , self.x , self.y)
        
    def Deplacement(self):
        if self.encours:
            self.y+=VitesseTir
            self.affichage()
            self.FinTir()
            mw.after(5,self.Deplacement)
    
    def FinTir(self):
        global Vies
        if self.y>hauteur:
            self.encours=False
            canevas.delete(self.apparence)
            del TirsAlien[0]
        elif self.y>=vaisseau.y-5 and self.y<=vaisseau.y+5 and\
            self.x<=vaisseau.x+largeur_vaisseau/2 and\
            self.x>=vaisseau.x-largeur_vaisseau/2 :
                self.encours=False
                canevas.delete(self.apparence)
                del TirsAlien[0]
                Vies-=1
                vaisseau.ViePerdue()
                AffichageVies(Vies)
                if Vies==0:
                    PartiePerdue()
        else:
            for i in Defences:
                if i.Resistance>0 and self.x>=i.x and self.x<=i.x+largeur_protections and self.y>=Protections.y and self.y<=Protections.y+hauteur_protections:
                    i.Update()
                    self.encours=False
                    canevas.delete(self.apparence)
                    del TirsAlien[0]
        

class Protections:
    Compteur=0
    def __init__(self):
        Protections.Compteur+=1
        self.Compteur=Protections.Compteur
        self.x=largeur*self.Compteur/(nbre_protections+1)
        Protections.y=posY_protections
        self.Resistance=resistance_protections
        self.Apparence=canevas.create_rectangle(self.x,self.y,self.x+largeur_protections,self.y+hauteur_protections,width=2,outline='purple',fill='white')
        self.VieProtection=canevas.create_text(self.x+largeur_protections/2,self.y+hauteur_protections/2,text=str(self.Resistance),fill='red')
        
    def Update(self):
        self.Resistance-=1
        if self.Resistance>0:
            canevas.itemconfig(self.VieProtection,text=(str(self.Resistance)))
        else:
            self.Destruction()
    
    def Destruction(self):
        canevas.delete(self.Apparence)
        canevas.delete(self.VieProtection)


def MouvementAlien():
    global ennemie
    if Partie_en_cours:
        L=[i.vivant for i in ennemie]
        if True in L:
            i=L.index(True)
            L.reverse()
            j=L.index(True)
            if (ennemie[-j-1].x+largeur_alien>=largeur and Alien.dir==1) or\
            (ennemie[i].x-largeur_alien<=0 and Alien.dir==-1):
                Alien.dir*=-1
                Alien.y+=descente_alien
                if Alien.y+hauteur_alien/2>=Protections.y:
                    PartiePerdue()
            for i in ennemie:
                i.x+=Alien.vitesse*Alien.dir
                i.Affichage()  
            mw.after(5,MouvementAlien)

def DelTirs():
    for i in Tirs:
        i.encours=False
    for i in TirsAlien:
        i.encours=False

def Tir_Alien():
    global ennemie,TirsAlien 
    if Partie_en_cours:
        L=[i.vivant for i in ennemie]
        i=randint(0,len(ennemie)-1)
        if L[i]:
            TirsAlien.append(TirAlien(i))
            mw.after(tps_entre_tir_alien,Tir_Alien)
        else:
            mw.after(1,Tir_Alien)



        
            
def AffichageVies(Vies):
    NbVies.config(text='Vies: '+str(Vies))
    
    
def Clavier(event):
    global TempsTir
    touche=event.keysym
    if touche=='q' or touche=='Left':
        vaisseau.deplacement(-1)
    elif touche=='d' or touche=='Right':
        vaisseau.deplacement(1)
    elif touche=='space':
        TempsTir1=time()
        if TempsTir1-TempsTir>=TempsEntreTirs or Tirs==[]:
            TempsTir=TempsTir1
            tir=Tir()
            Tirs.append(tir)
            Tirs[Tir.Compteur-1].Deplacement()

def PartieGagnee():
    global Partie_en_cours, Partie_Perdu
    gagne=True
    for i in ennemie:
        if i.vivant:
            gagne=False
    if gagne:
        canevas.grid_remove()
        winlose.config(text='Gagne')
        winlose.grid()
        canevas.delete("all")
        BoutonJouer.grid()
        BoutonJouer.config(text='Continuer')
        Alien.vitesse=VitesseAlien
        Partie_en_cours=False
        DelTirs()
        Partie_Perdu=False

def PartiePerdue():
    global Partie_en_cours, Partie_Perdu
    canevas.grid_remove()
    winlose.config(text='Perdu')
    winlose.grid()
    canevas.delete("all")
    BoutonJouer.grid()
    BoutonJouer.config(text='Rejouer')
    Alien.vitesse=VitesseAlien
    Partie_en_cours=False
    DelTirs()
    Partie_Perdu=True
    
    
def NouvellePartie():
    global ennemie, vaisseau, Partie_en_cours, Score, Vies, Defences
    canevas.grid()
    canevas.create_image(0,0,anchor='nw',image=ImageFond)
    winlose.grid_remove()
    BoutonJouer.grid_remove()
    vaisseau=Spaceship()
    Protections.Compteur=0
    Defences=[Protections() for i in range(nbre_protections)]
    Partie_en_cours=True
    if Partie_Perdu:
        Vies=ViesInit
        Score=0
        score.config(text='Score: '+str(Score))
    ennemie=[]
    AffichageVies(Vies)
    Alien.Compteur=0
    for i in range(nbre_alien_par_ligne):
        ennemie.append(Alien())
    for i in ennemie:
        i.Creation()
    MouvementAlien()
    Tir_Alien()

def Points(pts):
    global Score
    Score+=pts
    score.config(text='Score: '+str(Score))


#Fenetre de jeu
mw=tk.Tk()

ImageVaisseau=tk.PhotoImage(file='spaceship.gif')
ImageDestroy=tk.PhotoImage(file='spaceshipdestroy.gif')
ImageAlien=tk.PhotoImage(file='invader.gif')
ImageFond=tk.PhotoImage(file='space.gif')

score=tk.Label(mw,text='Score: 0')
score.grid(row=1,column=1)

NbVies=tk.Label(mw,text="Vies: 3")
NbVies.grid(row=1,column=2)

canevas=tk.Canvas(mw,height=hauteur,width=largeur, bg='black')
canevas.grid(row=2,column=1,columnspan=2)
canevas.grid_remove()
canevas.focus_set()
canevas.bind('<Key>',Clavier)

BoutonJouer=tk.Button(mw,text='Jouer',command=NouvellePartie)
BoutonJouer.grid(row=0,column=1)

BoutonQuitter=tk.Button(mw,text='Quitter',command=mw.destroy)
BoutonQuitter.grid(row=0,column=2)

winlose=tk.Label(mw,text='Gagne')
winlose.grid(row=1,column=0)
winlose.grid_remove()

mw.mainloop()