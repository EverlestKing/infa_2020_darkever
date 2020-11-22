import pygame as py
from pygame.draw import *


py.init()

win = py.display.set_mode((400,400))
win.fill((255,255,255))


FPS = 10
clock = py.time.Clock()



circle(win,(255,255,0),(200,200),150)
circle(win,(255,0,0),(140,150),20)
circle(win,(0,0,0),(140,150),5)
circle(win,(255,0,0),(250,150),25)
circle(win,[0,0,0],(250,150),8)
line(win, (0, 0, 0), (160, 120), (50, 50), 20)
line(win, (0, 0, 0), (200, 100), (350, 50), 20)
rect(win,(0,0,0),(150,250,150,30))

py.display.update()



finish = True

while finish:
    for event in py.event.get():
        clock.tick( FPS )
        if event.type == py.QUIT:
            finish = False
py.quit()