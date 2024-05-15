import pygame
import random

blueP = (20, 34, 238)
greenP = (20, 240, 50)
redP = (230, 0, 20)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
sizeSquare = 40
px = 50
py = 50

x = 80
y = 40
pygame.init()
size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Grid on PYGAME")
clock = pygame.time.Clock()
gameOver = False

def flash_block(currentColor):
    if currentColor[2] > 100:
        return (currentColor[0], currentColor[1], currentColor[2] - 200)
    else:
        return (currentColor[0], currentColor[1], currentColor[2] + 200)

    
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    
    screen.fill(WHITE)
    
    for i in range(0, size[0], 40):
        print(i)
        for j in range(0, size[1], 40):
            pygame.draw.rect(screen, BLACK, [i, j, 38, 38], 0)
            
    redP = flash_block(redP)
    pygame.draw.rect(screen, redP, [x, y, 38, 38], 0)
    pygame.display.flip()
    clock.tick(5)
pygame.quit()