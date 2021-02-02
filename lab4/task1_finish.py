import pygame
from pygame.draw import *
from random import randint, random
import math

print('Введите свое имя игрок:')
name=input()
pygame.init()
FPS=30
screen=pygame.display.set_mode((900, 600))
RED=(255, 0, 0)
BLUE=(0, 0, 255)
YELLOW=(255, 255, 0)
GREEN=(0, 255, 0)
MAGENTA=(255, 0, 255)
CYAN=(0, 255, 255)
BLACK=(0, 0, 0)
COLORS=[RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
Score=0
Balls=7
SPEED=10
SURFACE_TARGET=[0, 0, 550, 850]
list_ball=[0] * Balls
TIME=0


def file_processing():
    global Score
    temp=[]
    number_name=[]
    name_list=[]
    sccore_name=[]
    line=[]
    with open('best_score.txt', 'r+', encoding = 'utf-8') as file:
        for l in file.read().split('\n'):
            temp.append(l)
        for i in temp:
            a=i.split()
            line.append(a)
        line.pop(0)
        for i in line:
            try:
                number_name.append(i [0])
                name_list.append(i [1])
                sccore_name.append(i [2])
            except Exception:
                continue
        count=-1
        for i in sccore_name:
            count+=1
            a=int(i)
            if a < Score:
                sccore_name.insert(count, Score)
                name_list.insert(count, name)
                sccore_name.pop()
                name_list.pop()
                print('ВЫ ПОПАЛИ В ТАБЛИЦУ ЛИДЕРОВ')
                break
    with open('best_score.txt', 'w', encoding = 'utf-8') as file:
        file.write('     NAME  / / SCORE              # Таблица лучших игроков'+'\n')
        for i in range(9):
            file.write('{}  {}   {} \n '.format(str(number_name [i]), str(name_list [i]), str(sccore_name [i])))
            # file.write(str(number_name[i])+ (' ') + str(name_list[i]) + ('      ')+ str(sccore_name[i]) + '\n')


def click(position):
    global Score
    for i in range(Balls):
        T=list_ball [i]
        (x, y, r, color, x_forward, y_forward)=T
        up=x+r
        down=x-r
        left=y-r
        right=y+r
        if position [0] < up and position [0] > down and position [1] < right and position [1] > left:
            Score+=1
            print('ПРОСТАЯ ЦЕЛЬ + 1    ОБЩ:', Score)


def new_ball():
    for k in range(Balls):
        x=randint(100, 800)
        y=randint(100, 500)
        r=randint(10, 50)
        color=COLORS [randint(0, 5)]
        alpha=randint(0, 360)
        x_forward=SPEED * math.cos(alpha)
        y_forward=SPEED * math.sin(alpha)
        circle(screen, color, (x, y), r)
        list_ball [k]=(x, y, r, color, x_forward, y_forward)


def new_target():
    global SURFACE_TARGET
    list=SURFACE_TARGET
    position_surface1_x, position_surface1_y, position_surface2_x, position_surface2_y=list
    new_target_surface=pygame.Surface((50, 50))
    color=COLORS [randint(0, 5)]
    circle(new_target_surface, color, [25, 25], 20, 0, draw_top_right = True)
    color_2=COLORS [randint(0, 5)]
    circle(new_target_surface, color_2, [25, 25], 20, 30, draw_top_left = True)
    color_3=COLORS [randint(0, 5)]
    circle(new_target_surface, color_3, [25, 25], 20, 20, draw_bottom_left = True)
    color_4=COLORS [randint(0, 5)]
    circle(new_target_surface, color_4, [25, 25], 20, 10, draw_bottom_right = True)
    screen.blit(new_target_surface, (position_surface1_x, position_surface1_y))
    screen.blit(new_target_surface, (position_surface2_x, position_surface2_y))
    position_surface1_x+=1 * SPEED
    position_surface2_x-=1 * SPEED
    if position_surface1_x >= 900:
        position_surface1_x=-50
        position_surface1_y=randint(0, 600)
    if position_surface2_x <= 0:
        position_surface2_x=850
        position_surface2_y=randint(0, 600)
    SURFACE_TARGET=[position_surface1_x, position_surface1_y, position_surface2_x, position_surface2_y]


def click_new_target(position):
    global Score
    (position_surface1_x, position_surface1_y,
     position_surface2_x, position_surface2_y)=SURFACE_TARGET
    up1, up2=position_surface1_x, position_surface2_x
    down1, down2=position_surface1_x+50, position_surface2_x+50
    left1, left2=position_surface1_y, position_surface2_y
    right1, right2=position_surface1_y+50, position_surface2_y+50
    if up1 < position [0] < down1 and position [1] < right1 and position [1] > left1:
        Score+=3
        print('СПЕЦ ЦЕЛЬ + 3 ОЧК    ОБЩ:', Score)
    if position [0] > up2 and position [0] < down2 and position [1] < right2 and position [1] > left2:
        Score+=3
        print('СПЕЦ ЦЕЛЬ + 3 ОЧК    ОБЩ:', Score)


def move_ball():
    for i in range(len(list_ball)):
        M=list_ball [i]
        (x, y, r, color, x_forward, y_forward)=M
        M=(int(x+x_forward), int(y+y_forward), r, color, int(x_forward), int(y_forward))
        circle(screen, M [3], (M [0], M [1]), M [2])
        list_ball [i]=M


def reflection():
    for i in range(Balls):
        R=list_ball [i]
        (x, y, r, color, x_forward, y_forward)=R
        if x+r+5 >= 900 and x_forward > 0:
            R=(x, y, r, color, -x_forward, y_forward)
        elif x-r+5 <= 0 and x_forward < 0:
            R=(x, y, r, color, -x_forward, y_forward)
        elif y+r+5 >= 580 and y_forward > 0:
            R=(x, y, r, color, x_forward, -y_forward)
        elif y-r+5 <= 0 and y_forward < 0:
            R=(x, y, r, color, x_forward, -y_forward)
        list_ball [i]=R


clock=pygame.time.Clock()
finished=False
new_ball()
while not finished and TIME < 300:
    clock.tick(FPS)
    for event in pygame.event.get():
        reflection()
        if event.type == pygame.QUIT:
            finished=True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            position=event.pos
            click(position)
            click_new_target(position)
    reflection()
    new_target()
    move_ball()
    pygame.display.update()
    screen.fill(BLACK)
    TIME+=1
    if TIME == 290:
        print('СЕАНС ИСТЕЧЕН ПО ВРЕМЕНИ')
file_processing()
pygame.quit()
