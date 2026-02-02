class Ball:
    def __init__(self,canvas,width,height,window,paddle):
        self.width = width
        self.height = height
        self.image = canvas
        self.ball = canvas.create_oval(self.width//2,self.height//2,self.width//2+30,self.height//2+30,fill="#ebc334",tags="ball")
        self.window = window
        self.xVelocity = 5
        self.yVelocity = 10
        self.paddle = paddle

    def move_ball(self):
        x,y,x2,y2 = self.image.coords(self.ball)
     
        
        if self.height<=y2 or y<=0:
            self.yVelocity=-self.yVelocity
        if self.width<=x2 or x<=0:
            self.xVelocity=-self.xVelocity

        self.ball_paddle_collision()
        
        self.image.move(self.ball,self.xVelocity,self.yVelocity)
        self.window.after(20,self.move_ball)
    

    def ball_paddle_collision(self):
        bx1, by1, bx2, by2 = self.image.bbox(self.ball)
        px1, py1, px2, py2 = self.image.bbox(self.paddle)

        if (bx2 >= px1 and
        bx1 <= px2 and
        by2 >= py1 and
        by1 <= py2 and
        self.yVelocity > 0):
            self.yVelocity = -self.yVelocity

        