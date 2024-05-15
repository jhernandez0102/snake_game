import pygame

from game_world import World
from block import Block
      
pygame.init()
size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake game")
clock = pygame.time.Clock()
gameOver = False

world_game = World(screen)

bloque2 = Block(screen, (200, 200), (255, 0, 0), None)
bloque1 = Block(screen, (400, 400), (0, 255, 0), bloque2)
bloque3 = Block(screen, (400, 400), (0, 255, 0), bloque1)
bloque4 = Block(screen, (400, 400), (0, 255, 0), bloque3)

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    
    world_game.paint()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        bloque2.move("up")
        bloque1.move("up")
        bloque3.move("up")
        bloque4.move("up")
    if keys[pygame.K_s]:
        bloque2.move("down")
        bloque1.move("up")
        bloque3.move("up")
        bloque4.move("up")
    if keys[pygame.K_a]:
        bloque2.move("left")
        bloque1.move("up")
        bloque3.move("up")
        bloque4.move("up")
    if keys[pygame.K_d]:
        bloque2.move("rigth")
        bloque1.move("up")
        bloque3.move("up")
        bloque4.move("up")
    
    
    bloque1.paint()
    bloque2.paint()
    bloque3.paint()
    bloque4.paint()
    
    clock.tick(5)
pygame.quit()


