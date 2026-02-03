class Heart:
    def __init__(self,canvas,photo):
        self.image=canvas
        self.lives_number=[]
        self.photo = photo
        self.text = canvas.create_text(10,600,text="Lives: ",font=("'Arial",20,"bold"),fill="white",anchor="sw",tags="Lives")
    def create_lives(self):
        for i in range(3):
            self.lives_number.append(self.image.create_image(100+i*10,590,image=self.photo,anchor="sw",tags="heart"))