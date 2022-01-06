"""
Que fait le programme : Programme principal du SpaceInvaders
Qui l'a fait : Pierre-Antoine Chiron , Morgan Conche
Quand :169/12/2021
Que reste t-il? : Plein de choses
"""

#Importation des bibliotheques nécessaires
from tkinter import Tk,Label,Button,Canvas,Menu,PhotoImage

from prog import X, Y

#Création de classe

class Entity(object):
    def __init__(self,canvas):
        self.canvas = canvas
        self.x = X
        self.y = Y