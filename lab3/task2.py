import pygame as py
from pygame.draw import *

def window(size_window,location_window):
    # функция создания окна
    surface_window = py.Surface( (size_window) )
    surface_window.fill((255,255,255))

    color_window = 0, 191, 255

    rect( surface_window, (color_window), ( 10,10,80,100) )
    rect( surface_window, (color_window), (110,10,80,100) )

    rect( surface_window, (color_window), (10, 130, 80, 140) )
    rect( surface_window, (color_window), (110, 130, 80, 140) )

    win.blit( surface_window , (location_window) )

def koshka(n):
     #ХВОСТ КОШКИ С ПОВОРОТОМ
    color_cat = (150, 75, 0)
    surface_tail = py.Surface( (320, 100) )  # создание поверхности
    surface_tail.fill((222,184,135))

    ellipse( surface_tail, color_cat, (0, 0, 300, 100) )  # хвост

    ellipse( surface_tail, (0, 0, 0), (0, 0, 300, 100), 1 )  # хвост 2 для обводки
    surface_tail = py.transform.rotate( surface_tail, 160 )  # поворачивание поверхности с хвостом
    win.blit( surface_tail, (340, 460) )  # нанесение поверхности на окно

    # туловище кошки
    ellipse( win, color_cat, (50, 410, 400, 200)  )
    ellipse( win, (0, 0, 0), (50, 410, 400, 200), 1 )

    circle( win, color_cat, (370, 570), 60 )
    circle( win, (0, 0, 0), (370, 570), 60, 1 )

    ellipse( win, color_cat, (400, 600, 40, 100) )
    ellipse( win, (0, 0, 0), (400, 600, 40, 100), 1 )

    ellipse( win, color_cat, (80, 570, 80, 50) )
    ellipse( win, (0, 0, 0), (80, 570, 80, 50), 1 )

    ellipse( win, color_cat, (50, 500, 50, 80) )
    ellipse( win, (0, 0, 0), (50, 500, 50, 80), 1 )

    # голова кошки

    circle( win, color_cat, (90, 490), 80 )
    circle( win, (0, 0, 0), (90, 490), 80, 1)

    #правое ухо
    polygon( win, color_cat, ((85, 425), (140, 440), (140, 380)))
    polygon( win, (0, 0, 0), ((95, 420), (140, 445), (140, 380)),1 )

    polygon(win,(205,133,63),((105,420),(135,435),(135,390)))
    polygon( win, (0, 0, 0), ((105, 420), (135, 435), (135, 390)),1)

     # левое ухо
    polygon( win, color_cat, ((25, 445), (80, 435), (37, 380)))
    polygon( win, (0, 0, 0), ((25, 450), (68, 420), (37, 380)),1)

    polygon( win, (205,133,63), ((30, 440), (60, 420), (40, 390)) )
    polygon( win, (0, 0, 0), ((30, 440), (60, 420), (40, 390)),1)

    # правый глаз
    ellipse( win, (180, 220, 0), (110, 460, 40, 60))
    ellipse( win, (0, 0, 0), (110, 460, 40, 60),1 )
    ellipse( win, (0, 0, 0), (125, 470, 10, 40) )


     # левый глаз
    ellipse( win, (180, 220, 0), (40, 460, 40, 60) )
    ellipse( win, (0, 0, 0), (40, 460, 40, 60),1 )
    ellipse( win, (0, 0, 0), (55, 470, 10, 40) )
     # НОС
    polygon( win, (205, 133, 63), ((80, 520), (100, 520), (90, 530)))
    polygon( win, (0, 0, 0), ((80, 520), (100, 520), (90, 530)),1)
    # ГУБЫ
    arc(win,(0,0,0),(90,522,20,15),3.14,2*3.14,2)
    arc( win, (0, 0, 0), (70, 522, 20, 15),3.14,2 * 3.14,2 )


    # УСЫ
    aalines(win,(0, 0, 0),False,((100,525),(130,530),(160,540)),1)
    aalines( win, (0, 0, 0,), False, ((97, 527), (130, 540), (160, 560)))


    aalines( win, (0, 0, 0), False, ((79, 525), (50, 530), (20, 540)), 1 )
    aalines( win, (0, 0, 0), False, ((81, 527), (50, 540), (20, 560)), 1 )

def clew():
    color_grey = (128, 128, 128)

    circle( win, color_grey, (200, 700), 50 )
    circle( win, (0,0,0), (200, 700), 50 ,2)

    aalines( win, (0, 0, 0),False,((170, 730), (180, 725), (190, 720), (200, 710), (230, 680)))
    aalines( win, (0, 0, 0), False, ((175, 740), (180, 735), (190, 730), (200, 720), (230, 690)) )
    aalines( win, (0, 0, 0), False, ((170, 720), (180, 710), (190, 700), (200, 690), (220, 660)) )


py.init()
FPS = 20
win = py.display.set_mode((600,800))

clock = py.time.Clock()
finish = False

# ФОН
rect(win,(180,69,19),(0,0,600,400))
rect(win,(222,184,135),(0,400,600,400))

# ОКНО в функции


window((200 ,300),(350, 50))
#window((200,300),(100, 50))

koshka(1)
clew()

py.display.update()

while not finish:
    for event in py.event.get():
        clock.tick(FPS)
        if event.type == py.quit:
            finish = True
py.quit()

