class Paddle:
    def __init__(self,canvas,width,height,window):
        self.width=width
        self.height = height
        self.paddle= canvas.create_rectangle(self.width//2-50,self.height-30,self.width//2+50,self.height-10,fill="#D90429",tags="paddle")
        self.window=window
        self.image= canvas 

    def move_left(self,event):
        x1,_,_,_= self.image.coords(self.paddle)
        if x1<=0:
            self.image.move(self.paddle,0,0)
        else:
            self.image.move(self.paddle,-10,0)
       
       
    def move_right(self,event):
        _,_,x2,_= self.image.coords(self.paddle)
        if x2>=self.width:
            self.image.move(self.paddle,0,0)
        else:
            self.image.move(self.paddle,10,0)

    def move_up(self,event):
        _,y1,_,_= self.image.coords(self.paddle)
        if y1<=(self.height//2)+130:
            self.image.move(self.paddle,0,0)
        else:
            self.image.move(self.paddle,0,-10)
    
    
    def move_down(self,event):
        _,_,_,y2= self.image.coords(self.paddle)
        if y2>=self.height-10:
            self.image.move(self.paddle,0,0)
        else:       
            self.image.move(self.paddle,0,10)
    