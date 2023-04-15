from tkinter import *
import random
import time


class Ball:
    def __init__(self, canvas, paddle, score, color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.score.hit()
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.started = False
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<Button-1>', self.start_game)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2

    def start_game(self, ev):
        self.started = True


class Score:
    def __init__(self, canvas, color):
        self.score = 0
        self.canvas = canvas
        # self.counter_text = "Your Score: %s" % self.score
        self.id = canvas.create_text(450, 10, text="Your Score: %s" % self.score, fill=color, font=("Times", -15))

    def hit(self):
        self.score = self.score + 1
        self.canvas.itemconfig(self.id, text="Your Score: %s" % self.score)


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

score = Score(canvas, "green")
# end_game = End_game(canvas, "red")
paddle = Paddle(canvas, "blue")
ball = Ball(canvas, paddle, score, "red")
game_over_text = canvas.create_text(250, 200, text="Game Over", state="hidden", fill="red", font=("Times", -40))


# Main loop - infinite loop in order not to close game window
while 1:
    if ball.hit_bottom == False and paddle.started == True:
        ball.draw()
        paddle.draw()
    if ball.hit_bottom == True:
        time.sleep(1)
        canvas.itemconfig(game_over_text, state='normal')
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
