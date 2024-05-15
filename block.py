import pygame

class Block:
    size = (50, 50)
    color = (255, 0, 0) #rojo
    position = (200, 200)
    last_position = position
    screen = pygame.display.get_surface()
    block_father = None
    
    def __init__(self, screen, position, color, father):
        self.screen = screen
        self.position = position
        self.color = color 
        self.block_father = father      
        
    def paint(self):
        pygame.draw.rect(self.screen, self.color, [self.position[0], self.position[1], self.size[0], self.size[1]], 0)
        pygame.display.flip()
    
    def move(self, direction):
        self.last_position = self.position
        if(self.block_father is None):
            if direction == "up":
                if self.position[1] - self.size[1] < 0:
                    self.position = (self.position[0], 0)
                else:
                    self.position = (self.position[0], self.position[1] - self.size[1])
                    
            if direction == "down":
                if self.position[1] - self.size[1] > 550:
                    self.position = (self.position[0], 550)
                else:
                    self.position = (self.position[0], self.position[1] + self.size[1])
            
            if direction == "left":
                if self.position[0] - self.size[0] < 0:
                    self.position = (self.position[0], 0)
                else:
                    self.position = (self.position[0] - self.size[0], self.position[1] ) 
            
            if direction == "rigth":
                if self.position[0] - self.size[0] > 550:
                    self.position = (self.position[0], 550)
                else:
                    self.position = (self.position[0] + self.size[0], self.position[1] )
        else:
            self.position = self.block_father.last_position
