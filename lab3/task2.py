import pygame as py
from pygame.draw import *


py.init()
FPS = 20
win = py.display.set_mode()

clock = py.time.clock()
finish = False


while not finish:
    for event in py.event.get():
        clock.ticks(FPS)
        if event.type == py.quit:
            finish = True
py.quit()
