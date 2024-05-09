import pygame

black = (0, 0, 0)
white = (255, 255, 255)

block_size = (50,50)

pygame.init()
size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Hello World on PYGAME")
clock = pygame.time.Clock()
gameOver = False

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    screen.fill(white)
    
    for i in range(0, size[0], block_size[0]):
        for j in range(0, size[1], block_size[1]):
            pygame.draw.rect(screen, black, [i, j, block_size[0]-2, block_size[1]-2], 0)
    
    pygame.display.flip()
    
    clock.tick(5)
pygame.quit()