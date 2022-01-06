import random

import tkinter as tk

# --- constants --- # UPPERCASE name

RES_X = 800
RES_Y = 600

# --- classes --- # CamelCase name 

class Ennemis(object):

    def __init__(self, canvas):

        # access to canvas
        self.canvas = canvas

        # started amount of enemies
        self.amount = 5

        # list for all enemies
        self.enemies = list()

        self.direction = 1

        # create enemies
        for _ in range(self.amount):
            self.create_one_enemy()

    def create_one_enemy(self):
        radius = 5 # random

        x = random.uniform(radius, RES_X-radius)
        y = random.uniform(30, 60)

        rectangle = self.canvas.create_rectangle(x-radius, y-radius, x+radius, y+radius, fill="black", outline="black")

        # one enemy
        enemy = [x, y, radius, rectangle]

        # append to list - but I don't need this list 
        self.enemies.append(enemy)

        # move this enemy after random time
        time = 300
        root.after(time, self.move_one_enemy, enemy)

    def move_one_enemy(self, enemy):

        #print('moving:', enemy)

        # get old values
        x, y, radius, rectangle = enemy


        if x+20+radius > RES_X:
            x = 2*(RES_X-20)-x
            radius = -radius
            y += 30

        if x-20+radius < 0:
            x = 2*20-x
            radius = -radius
            y += 30

        x += radius    

        self.canvas.coords(rectangle, x-radius, y-radius, x+radius, y+radius)

        # remember new values
        enemy[0] = x
        enemy[1] = y

        # move this enemy after random time
        time = 300
        root.after(time, self.move_one_enemy, enemy)

# --- functions --- # lower_case name 

def add_new_enemy():

    enemies.create_one_enemy()

    # add next enemy after random time
    timer = random.randint(1000, 3000)
    root.after(timer, add_new_enemy)

# --- main ---

root = tk.Tk()
root.title("")

canvas = tk.Canvas(root, width=RES_X, height=RES_Y, bg="white")
canvas.pack()

# create enemies and move it using `root.after`
enemies = Ennemis(canvas)

# add new enemy after random time
random_time = random.randint(150, 3000)
root.after(random_time, add_new_enemy)

root.mainloop()