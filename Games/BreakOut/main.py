from tkinter import *
from random import randint
from blocks import Blocks
from ball import Ball
from heart import Heart
from paddle import Paddle
import pygame



WIDTH=500
HEIGHT=700



window = Tk()
pygame.mixer.init()
pygame.mixer.music.load("background-sound.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

window.geometry(f"{WIDTH}x{HEIGHT}")
window.resizable(False,False)
icon = PhotoImage(file="icon.png")
window.title("Breakout")
window.config(borderwidth=1)
window.iconphoto(True,icon)
background = PhotoImage(file="ibackground.png")
photo = PhotoImage(file="heart.png")
canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()
canvas.create_image(0,0,image=background,anchor="nw",tags="background")



ball = Ball(canvas,WIDTH,HEIGHT,window,photo)


ball.move_ball()


ball.RandomColorText()

window.mainloop()