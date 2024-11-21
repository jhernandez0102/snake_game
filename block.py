import pygame

class Block:
    size = (50, 50)
    color = (255, 0, 0) #rojo
    position = (200, 200)
    last_position = position
    screen = pygame.display.get_surface()
    block_father = None
    block_child = None
    
    def __init__(self, screen, position, color, father):
        self.screen = screen
        self.position = position
        self.color = color 
        self.block_father = father      
        
    def paint(self):
        pygame.draw.rect(self.screen, self.color, [self.position[0], self.position[1], self.size[0], self.size[1]], 0)
        pygame.display.flip()
        if(self.block_child is not None):
            self.block_child.paint()
        
    def add_child(self, child):
        if(self.block_child is None):
            self.block_child = child
        else:
            child.set_position(self.block_child.last_position)
            child.set_father(self.block_child)
            self.block_child.add_child(child)
    
    def set_position(self, position):
        self.position = position
    
    def set_color(self, color):
        self.color = color
        
    def set_father(self, father):
        self.block_father = father
                  
    def move(self, direction):
        self.last_position = self.position
        if(self.block_father is None):
            if direction == "up":
                if self.position[1] - self.size[1] < 0:
                    self.position = (self.position[0], 550)
                else:
                    self.position = (self.position[0], self.position[1] - self.size[1])
                    
            if direction == "down":
                if self.position[1] - self.size[1] > 550:
                    self.position = (self.position[0], 0)
                else:
                    self.position = (self.position[0], self.position[1] + self.size[1])
            
            if direction == "left":
                if self.position[0] - self.size[0] < 0:
                    self.position = (550, self.position[1])
                else:
                    self.position = (self.position[0] - self.size[0], self.position[1] ) 
            
            if direction == "rigth":
                if self.position[0] - self.size[0] > 550:
                    self.position = ( 0 , self.position[1])
                else:
                    self.position = (self.position[0] + self.size[0], self.position[1] )
        else:
            self.position = self.block_father.last_position
            
        if(self.block_child is not None):
            self.block_child.move(direction)
        
        if(self.position[0] > 600):
            self.position = (0, self.position[1])
        if(self.position[0] < 0):
            self.position = (550, self.position[1])
        if(self.position[1] > 600):
            self.position = (self.position[0], 0)
        if(self.position[1] < 0):
            self.position = (self.position[0], 550)

