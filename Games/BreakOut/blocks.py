from random import randint

class Blocks:
    ROWS=3
    COLUMNS=10
    BLOCK_WIDTH=50
    BLOCK_HEIGHT = 30
    
    def __init__(self,canvas):
        self.blocks = []
        self.image = canvas
    
    def create_blocks(self,x1=0,y1=BLOCK_HEIGHT,x2=BLOCK_WIDTH,y2=BLOCK_HEIGHT*2):
        for _ in range(Blocks.ROWS):
            x1,x2=0,Blocks.BLOCK_WIDTH
            for _ in range(Blocks.COLUMNS):
                self.blocks.append(self.image.create_rectangle(x1,y1,x2,y2,fill=self.changeRandomColor(),tags="block"))
                x1,x2=x2,x2+Blocks.BLOCK_WIDTH
            
            y1,y2=y2,y2+Blocks.BLOCK_HEIGHT

    def changeRandomColor(self):
        colors = [
            "#FDC500",  # yellow
            "#FF5733",  # orange-red
            "#33FF57",  # green
            "#3357FF",  # blue
            "#FF33A8",  # pink
            "#A833FF",  # purple
            "#33FFF3",  # cyan
            "#FF8C33",  # orange
            "#8CFF33",  # lime
            "#FF3333",  # red
            "#33FF8C",  # mint
            "#8C33FF",  # violet
            "#FFC300",  # golden yellow
            "#FF6F61",  # coral
            "#6BFFB8",  # aqua green
            "#6B83FF",  # light indigo
            "#FF6BD6",  # magenta
            "#B8FF6B",  # light lime
            "#6BFFF5",  # turquoise
            "#FF9F1C",  # dark orange
            "#2EC4B6",  # teal
            "#E71D36",  # crimson
            "#9D4EDD",  # amethyst
            "#00BBF9",  # bright blue
            "#00F5D4",  # bright turquoise
            "#F15BB5",  # strong pink
            "#FEE440"   # bright yellow
        ]

        
        return colors[randint(0,26)]
        


