import pygame

class World:
    size = (600, 600)
    block_size = (50, 50)
    bg_color = (255, 255, 255)
    block_color = (0, 0, 0)
    screen = pygame.display.get_surface()
    
    def __init__(self, screen):
        self.size = (600, 600)
        self.screen = screen
    
    def paint(self):
        self.screen.fill(self.bg_color)
    
        for i in range(0, self.size[0], self.block_size[0]):
            for j in range(0, self.size[1], self.block_size[1]):
                pygame.draw.rect(self.screen, self.block_color, [i, j, self.block_size[0]-2, self.block_size[1]-2], 0)
    
        pygame.display.flip()