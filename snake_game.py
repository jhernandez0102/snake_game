import pygame

from game_world import World
from block import Block
from snake import Snake
from food import Food
    
pygame.init()
size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake game")
clock = pygame.time.Clock()
gameOver = False

world_game = World(screen)
snake = Snake(screen)
food = Food(screen)
n = 0

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    
    world_game.paint()
    snake.paint()
    food.paint()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        snake.move("up")
    if keys[pygame.K_s]:
        snake.move("down")
    if keys[pygame.K_a]:
        snake.move("left")
    if keys[pygame.K_d]:
        snake.move("rigth")
    #if keys[pygame.K_SPACE]:
        #food.disappear()
    snake.match(food)
    
    clock.tick(8)
pygame.quit()


