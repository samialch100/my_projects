from random import randint

class Blocks:
    ROWS=3
    COLUMNS=10
    BLOCK_WIDTH=50
    BLOCK_HEIGHT = 30
    
    def __init__(self,canvas):
        self.blocks = []
        self.image = canvas
    
    def create_blocks(self,x1=0,y1=0,x2=BLOCK_WIDTH,y2=BLOCK_HEIGHT):
        for _ in range(Blocks.ROWS):
            x1,x2=0,Blocks.BLOCK_WIDTH
            for _ in range(Blocks.COLUMNS):
                self.blocks.append(self.image.create_rectangle(x1,y1,x2,y2,fill=self.changeColor(),tags="block"))
                x1,x2=x2,x2+Blocks.BLOCK_WIDTH
            
            y1,y2=y2,y2+Blocks.BLOCK_HEIGHT

    def changeColor(self):
        letters="0123456789ABCDEF"
        color="#"
        for _ in range(6):
            color+=letters[randint(0,15)]
        if color=="#888888" or color=="#000000" or color=="#FFFFFF":
            return "#EF233C"
        return color
        


