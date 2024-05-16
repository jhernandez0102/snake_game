import pygame
from block import Block

class Snake:
    blocks = []
    
    def __init__(self, screen):
        self.screen = screen
        self.blocks.append(Block(self.screen, (200, 200), (255, 0, 0), None))
        
        
    def move(self, direction):
        self.blocks[0].move(direction)
        if(self.blocks[0].block_child is not None):
            self.blocks[0].block_child.move(direction)
        
    
    def paint(self):
        self.blocks[0].paint()
        if(self.blocks[0].block_child is not None):
            self.blocks[0].block_child.paint()
            
    def grow(self):
        print("Growing snake")
        if(self.blocks[0].block_child is None):
            self.blocks[0].add_child(Block(self.screen, self.blocks[0].last_position, (0, 255, 0), self.blocks[0]))
        else:
            self.blocks[0].block_child.add_child(Block(self.screen, self.blocks[0].block_child.last_position, (0, 255, 0), self.blocks[0].block_child))
            

        
        
     