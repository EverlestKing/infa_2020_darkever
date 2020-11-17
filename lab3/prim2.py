import pygame as py



py.init()

FPS = 30
screen = py.display.set_mode((400, 400))

x1 = 100; y1 = 100
x2 = 300; y2 = 200
N = 10
color = (255, 255, 255)
py.draw.rect(screen, color, (x1, y1, x2 - x1, y2 - y1), 2)
h = (x2 - x1) // (N + 1)
x = x1 + h
for i in range(N):
    py.draw.line(screen, color, (x, y1), (x, y2))
    x += h

py.display.update()
clock = py.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in py.event.get():
        if event.type == py.QUIT:
            finished = True

py.quit()