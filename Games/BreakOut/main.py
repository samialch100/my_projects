from tkinter import *
from random import randint
from blocks import Blocks
from ball import Ball
from paddle import Paddle
WIDTH=500
HEIGHT=700



window = Tk()
window.geometry(f"{WIDTH}x{HEIGHT}")
window.resizable(False,False)
icon = PhotoImage(file="icon.png")
window.title("Breakout")
window.config(borderwidth=1)
window.iconphoto(True,icon)
background = PhotoImage(file="ibackground.png")
canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()
canvas.create_image(0,0,image=background,anchor="nw")

blocks = []

blocks=Blocks(canvas)
paddle = Paddle(canvas,WIDTH,HEIGHT,window)
ball = Ball(canvas,WIDTH,HEIGHT,window,paddle.paddle)


ball.move_ball()

blocks.create_blocks()
window.bind("<a>",paddle.move_left)
window.bind("<d>",paddle.move_right)
window.bind("<w>",paddle.move_up)
window.bind("<s>",paddle.move_down)
window.mainloop()