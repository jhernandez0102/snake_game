import pygame
from block import Block

class Snake:
    blocks = []
    direction = "up"
    
    def __init__(self, screen):
        self.screen = screen
        self.blocks.append(Block(self.screen, (200, 200), (255, 0, 0), None))
          
    def move(self, direction):
        self.blocks[0].move(direction)
        if(self.blocks[0].block_child is not None):
            self.blocks[0].block_child.move(direction)
    
    def move_step(self):
        self.move(self.direction)
        
    def change_direction(self, direction):
        self.direction = direction
    
    def paint(self):
        self.blocks[0].paint()
        if(self.blocks[0].block_child is not None):
            self.blocks[0].block_child.paint()
            
    def grow(self):
        print("Crecí")
        if(self.blocks[0].block_child is None):
            self.blocks[0].add_child(Block(self.screen, self.blocks[0].last_position, (0, 255, 0), self.blocks[0]))
        else:
            self.blocks[0].block_child.add_child(Block(self.screen, self.blocks[0].block_child.last_position, (0, 255, 0), self.blocks[0].block_child))
            
    def match(self, food):
        if(self.blocks[0].position == food.position):
            print("Comí")
            food.disappear()
            self.grow()

    def self_collition(self):
        collition = False
        position_head = self.blocks[0].position
        index = 0
        for block in self.blocks:
            if index == 0:
                continue
            else:
                if position_head == block.position:
                    collition = True
                    break
            
            index = index + 1

        return collition