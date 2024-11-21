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
    
    snake.move_step();
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        snake.change_direction("up")
    if keys[pygame.K_s]:
        snake.change_direction("down")
    if keys[pygame.K_a]:
        snake.change_direction("left")
    if keys[pygame.K_d]:
        snake.change_direction("rigth")
    #if keys[pygame.K_SPACE]:
        #food.disappear()
    snake.match(food)
    if(snake.self_collition()):
        pygame.quit()

    clock.tick(8)
pygame.quit()


