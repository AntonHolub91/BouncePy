from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)

    def draw(self):
        pass


tk = Tk()
# set name of the game window
tk.title("Game")
# make the window size uneditable, 1st attribute for horiz, 2nd one for vertical
tk.resizable(0, 0)
# command to set game window over all other windows
tk.wm_attributes("-topmost", 1)
# attributes bd and highlightthickness need to hide frames around the game window
canvas = Canvas(tk, width=500, height=500, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

input("fsd")




