import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 2
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
Score = 0

x_forward = 0
y_forward = 0


def click(position):
    global Score ,x ,y, r
    up=x+r
    down=x-r
    left=y-r
    right=y+r
    if position [0] < up and position [0] > down and position [1] < right and position [1] > left:
        score+=1
        print(score)



def new_ball():
    global  x, y, r , color , gracie
    '''рисует новый шарик '''
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    n = 5
    list = [randint(100,1100) for i in range(n)]
    circle(screen, color, (x, y), r)



pygame.display.update()
clock = pygame.time.Clock()
finished = False
gracie = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            position = event.pos
            click(position)
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()