import pygame
import random
 
pygame.init()
 

black = (0, 0, 0)
red = (213, 50, 80)
blue = (150, 255, 255)
 
win_width = 700
win_height = 500
 
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('snake game')
 
clock = pygame.time.Clock()
 
razmer_zmei = 10
snake_speed = 15

pygame.font.init()
pygame.font = pygame.font.Font(None, 70)
lose = pygame.font.render('YOU LOSE!', True, (255, 0, 0))
 

def our_snake(razmer_zmei, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, black, (x[0], x[1], razmer_zmei, razmer_zmei))
 

def game():
    game_over = False

    x1 = 300
    y1 = 300

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, win_width - razmer_zmei) / 10.0) * 10.0
    foody = round(random.randrange(0, win_height - razmer_zmei) / 10.0) * 10.0
 
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -razmer_zmei
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = razmer_zmei
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -razmer_zmei
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = razmer_zmei
                    x1_change = 0

        if x1 >= win_width or x1 < 0 or y1 >= win_height or y1 < 0:
            game_over = True
        x1 += x1_change
        y1 += y1_change
        window.fill(blue)
        pygame.draw.rect(window, red, (foodx, foody, razmer_zmei, razmer_zmei))
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        our_snake(razmer_zmei, snake_List)
 
 
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, win_width - razmer_zmei) / 10.0) * 10.0
            foody = round(random.randrange(0, win_height - razmer_zmei) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
        pygame.display.update()
    
    
 
 
game() 
