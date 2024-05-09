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

class Block:
    size = (48, 48)
    color = (255, 0, 0) #rojo
    position = (200, 200)
    screen = pygame.display.get_surface()
    
    def __init__(self, screen, position, color):
        self.screen = screen
        self.position = position
        self.color = color        
        
    def paint(self):
        pygame.draw.rect(self.screen, self.color, [self.position[0], self.position[1], self.size[0], self.size[1]], 0)
        pygame.display.flip()
        

      
pygame.init()
size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake game")
clock = pygame.time.Clock()
gameOver = False

world_game = World(screen)
bloque1 = Block(screen, (400, 400), (0, 255, 0))
bloque2 = Block(screen, (200, 200), (255, 0, 0))

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    
    world_game.paint()
    bloque1.paint()
    bloque2.paint()
    
    
    clock.tick(5)
pygame.quit()


