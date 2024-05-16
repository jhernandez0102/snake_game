from block import Block
import random

class Food(Block):
    
    def __init__(self, screen):
        size = (600, 600)
        random_position = (random.choice(range(0, size[0], 50)), random.choice(range(0, size[0], 50)))
        super().__init__(screen, random_position, (0, 0, 255), None)
    
    def appear(self):
        size = (600, 600)
        #Generate a random position
        random_position = (
            random.choice(range(0, size[0], 50)), 
            random.choice(range(0, size[0], 50)))
        #Set position
        self.set_position(random_position)
        #Set default color
        self.set_color((0, 0, 255))
        #Paint the block
        self.paint()
        
        
    def disappear(self):
        #Change block's color
        self.set_color((0, 0, 0))
        #Paint the block
        self.paint()
        #Appear
        self.appear()