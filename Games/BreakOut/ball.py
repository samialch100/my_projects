from random import randint
import pygame
from tkinter import messagebox

from blocks import Blocks
from heart import Heart
from paddle import Paddle


class Ball:
    WIN_SCORE=150
    def __init__(self,canvas,width,height,window,photo):
        self.width = width
        self.height = height
        self.image = canvas
        self.ball = self.image.create_oval(self.width//2,self.height//2,self.width//2+30,self.height//2+30,fill="#ebc334",tags="ball")
        self.window = window
        self.xVelocity = 5
        self.yVelocity = 10
        self.score= 0
        self.on_collision=False
        self.result = self.image.create_text(450,600,text=f"Score: {self.score}",font=("'Arial",20,"bold"),fill="white",anchor="se",tags="result")

        pygame.mixer.init()
        self.game_over_sound= pygame.mixer.Sound("game-over.mp3")
        self.win_game_sound = pygame.mixer.Sound("winner-game-sound.mp3")

        self.blocks= Blocks(self.image)
        self.blocks.create_blocks()

        self.paddle = Paddle(self.image,self.width,self.height,window)
        self.paddle.move_paddle()
        self.photo =photo
        self.heart = Heart(self.image,self.photo)
        self.heart.create_lives()

    def move_ball(self):

        if not self.on_collision:
            self.image.move(self.ball,0,self.yVelocity)
        else:
            self.image.move(self.ball,self.xVelocity,self.yVelocity)

        x,y,x2,y2 = self.image.bbox(self.ball)

        if y <= 0:
            self.yVelocity = -self.yVelocity
       

        if y2 >= self.height:
            self.ball_respawn()
                    

        if x <= 0 or x2 >= self.width:
            self.xVelocity = -self.xVelocity
           

        self.ball_paddle_collision()
        self.ball_blocks_collision()

        if self.end_game():
            pygame.mixer.music.stop()
            answer = messagebox.askquestion(title="New Game",message="Do you want to play a new game?")
            if answer=="yes":
                self.reset()
            else:
                self.window.destroy()

        self.window.after(20,self.move_ball)

   

    def ball_paddle_collision(self):
        bx1, by1, bx2, by2 = self.image.bbox(self.ball)

        overlapping = self.image.find_overlapping(
            bx1, by1, bx2, by2
        )

        for item in overlapping:
            if "paddle" in self.image.gettags(item) and self.yVelocity > 0:
                self.yVelocity = -self.yVelocity
                self.on_collision=True
                break
    
    def ball_blocks_collision(self):
        bx1, by1, bx2, by2 = self.image.bbox(self.ball)
        overlapping = self.image.find_overlapping(
            bx1, by1, bx2, by2
        )
        for item in overlapping:
            if "block" in self.image.gettags(item):
                
                if self.image.itemcget(item,"fill")!="#888888":
                    self.image.itemconfig(item,fill="#888888")
                    
                else:
                    self.image.delete(item)
                    self.score+=5
                    self.image.itemconfig("result",text=f"Score: {self.score}")
                self.yVelocity = -self.yVelocity
                
                break
    

    
    def changeRandomColor(self):
        colors =["#FDC500","#EEEF20","#FFFF3F","#dd2d4a","#89fc00"]
        return colors[randint(0,4)]
        

    def RandomColorText(self):
        self.image.itemconfig("result",fill=self.changeRandomColor())
        self.image.itemconfig("Lives",fill=self.changeRandomColor())
        self.window.after(500,self.RandomColorText)


    def end_game(self):
        if Ball.WIN_SCORE==self.score:
            self.remove_all()
            self.win= self.image.create_text(self.width//2,self.height//2,text="You Win!",font=("Arial",20,"bold"),fill="green",anchor="center",tags="win")
            self.win_game_sound.play()
            return True
        
        if not self.heart.lives_number:
            self.remove_all()
            self.game_over=self.image.create_text(self.width//2,self.height//2,text="Game over!",font=("Arial",20,"bold"),fill="red",anchor="center",tags="game over")
            self.game_over_sound.play()
            return True

        return False 
    
    
    def remove_all(self):

        for item in self.image.find_all():
            if not "background" in self.image.gettags(item):
                self.image.delete(item)
        
        self.paddle.stop_paddle()    

    def ball_respawn(self):
        if self.heart.lives_number:
            
            self.image.delete(self.heart.lives_number.pop())
            self.image.delete("ball")
            self.ball = self.image.create_oval(self.width//2,self.height//2,self.width//2+30,self.height//2+30,fill="#ebc334",tags="ball")
            self.on_collision=False
    

    def reset(self):
        
        self.remove_all()
        self.score=0
        self.on_collision=False
        self.blocks= Blocks(self.image)
        self.blocks.create_blocks()
        self.ball = self.image.create_oval(self.width//2,self.height//2,self.width//2+30,self.height//2+30,fill="#ebc334",tags="ball")
        self.result = self.image.create_text(450,600,text=f"Score: {self.score}",font=("'Arial",20,"bold"),fill="white",anchor="se",tags="result")
        self.paddle = Paddle(self.image,self.width,self.height,self.window)
        self.heart = Heart(self.image,self.photo)
        self.heart.create_lives()
        
        self.paddle.move_paddle()
        pygame.mixer.music.play()
        