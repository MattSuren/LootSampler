#Matthew Surendran Extra Credit Project

# The Objective for this project was to create a simple program
# with a loot table to roll for fun as well as dipping my toes into GUI creation
# in Python. As I am writing this after the final version of the program, there
# were alot of trial and errors in writing it with some more fleshing out I would
# like to do in the future. I added some of the unused code at the bottom of the 
# project that I decided not to go with. What we ended up with is just a simple
# UI with a couple buttons linked to functions that sample an artificially skewed 
# loot table.

#import configs
#decided to go with tkinter as it seemed to be pretty popular 
#with a lot of tutorials and support
from tkinter import *
from tkinter import messagebox
import random
from random import sample
import time

#GUI "box" definition creating our window and sizing it with a title
root = Tk()
root.geometry("650x250")
root.title("Feeling Lucky?")

#creating list of rewards since we are sampling, we modify the drop rate by quantity of the same element in the list
gear = [ 
        'Stick',
        'Stick',
        'Stick',
        'Stick',
        'Sword' ,
        'Bow'   ,
        'Bow'   ,
        'Dagger',
        'Dagger',
        'Dagger',
        'Shield',
        'Shield',
        'Shield',
        'Shield',
        'Magic Staff',
        'Excalibur',
        'Platebody',
]
        
#defining roll command
def roll():
    loot = random.sample(gear,1)
    Label(root, text=loot).pack(padx=5)\    

#defining a roll alot command
def keep_rolling():
    for i in range(len(gear)):
        roll()      

#creating two buttons
w = Button(root,text ='Roll', command = roll, border=5, height=2, width=5 )
x = Button(root,text ='Roll...a lot', command = keep_rolling, border=5, height=2, width=8 )

#w.place(x=85, y=85)
w.pack(side=LEFT, padx=5, pady=20)
x.pack(side=RIGHT, padx=5, pady=20)
root.mainloop()



#Other code that didnt quite work out

#attempts at weighting the drops with if statements on a random roll
#Label.after(1000, Label.destroy)
    # num = random.random() * 100
    # if num < 10:
    #     #msg = messagebox.showinfo("Roll","LOSE")
    #     result = ("lose")
    #     Label(root, text=str(result)).pack(padx=5)
    # elif num > 10 and num < 20:
    #     result = ("win")
    #     Label(root, text=str(result)).pack(padx=5)
    # elif num > 20 and num < 30:
    #     result = ("win")
    #     Label(root, text=str(result)).pack(padx=5)
    # elif num > 30 and num < 100:
    #     result = ("win")
    #     Label(root, text=str(result)).pack(padx=5) 
    # else:
    #     result = ("BIG WIN")
    #     Label(root, text=str(result)).pack(padx=5)

#attempting to add a delay to the roll alot function but 
#couldn't get the delay to work within a function, since it runs the whole function before displaying
#root.after(1000,roll())
        #Label.after(1000, Label.place())
    #Label.after(5000, Label.destroy)    