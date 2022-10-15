from tkinter import *
from Square import Square
from Game import Game
from Preset import Preset
from tkinter import messagebox

#Wyczysc
#Dodac walec powierczhnie i inne

#constants
TITLE = 'Life'

#window initialization
root = Tk()
root.title(TITLE)

welcome_box = Preset()
welcome_box.buildStartWindow(root)


mainloop()