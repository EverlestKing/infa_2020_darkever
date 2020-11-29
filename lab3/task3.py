import pygame as py
from pygame.draw import circle, rect, ellipse, polygon, arc, aalines


def main():
    # This is a general function, creates background and parameters of other functions

    # Background
    rect(win, (180, 69, 19), (0, 0, 600, 400))
    rect(win, (222, 184, 135), (0, 380, 600, 400))

    # Draw window , (location),size coefficient
    window((350, 50), 1.24)
    window((50, 50), 1)

    # Draw cat's
    # Location , color_cat , coefficient_size, flip: if flip = "1" cat are look to the right ,
    # or if flip not a "1" cat are look to the left
    cat((0, 380), (150, 75, 0), 3.14, -1)
    cat((300, 380), (150, 75, 0), 1.89, 1)
    cat((20, 500), (128, 128, 128), 1.90, -1)
    cat((450, 650), (0, 0, 0), 3.67, 1)
    cat((50, 700), (255, 255, 255), 3.67, -1)

    # Draw clew's
    # Location , coefficient size
    clew((300, 750), 4)
    clew((160, 460), 2.34)
    clew((430, 600), 2.0)


def window(location, coefficient_size):
    # This function creates windows

    surface_window = py.Surface((200 / coefficient_size, 300 / coefficient_size))
    surface_window.fill((255, 255, 255))
    color_window = 0, 192, 255

    rect(surface_window, color_window,
         (10 / coefficient_size, 10 / coefficient_size, 80 / coefficient_size, 100 / coefficient_size))
    rect(surface_window, color_window,
         (110 / coefficient_size, 10 / coefficient_size, 80 / coefficient_size, 100 / coefficient_size))

    rect(surface_window, color_window,
         (10 / coefficient_size, 130 / coefficient_size, 80 / coefficient_size, 140 / coefficient_size))
    rect(surface_window, color_window,
         (110 / coefficient_size, 130 / coefficient_size, 80 / coefficient_size, 140 / coefficient_size))
    # surface application
    win.blit(surface_window, location)


def cat(location, color_cat, coefficient_size, flip):
    # ALL SURFACE
    surface_all = py.Surface((350 / (coefficient_size / 2), 200 / (coefficient_size / 2)))
    surface_all.fill((222, 184, 135))
    color_ear = (205, 133, 63)
    color_eyes = (180, 220, 0)

    # Tail cat with a turn
    surface_tail = py.Surface((320 / coefficient_size, 100 / coefficient_size))  # create surface
    surface_tail.fill((222, 184, 135))
    black_color = (0, 0, 0)

    ellipse(surface_tail, color_cat,
            (0, 0, 300 / coefficient_size, 100 / coefficient_size))  # tail
    ellipse(surface_tail, black_color,
            (0, 0, 300 / coefficient_size, 100 / coefficient_size), 1)
    surface_tail = py.transform.rotate(surface_tail, 160)  # turn tail
    surface_all.blit(surface_tail,
                     (330 / coefficient_size, 80 / coefficient_size))  # surface_tail in a surface_all

    # Body
    ellipse(surface_all, color_cat,
            (40 / coefficient_size, 30 / coefficient_size, 400 / coefficient_size, 190 / coefficient_size))
    ellipse(surface_all, black_color,
            (40 / coefficient_size, 30 / coefficient_size, 400 / coefficient_size, 190 / coefficient_size), 1)

    circle(surface_all, color_cat,
           (360 / coefficient_size, 190 / coefficient_size), 60 / coefficient_size)
    circle(surface_all, black_color,
           (360 / coefficient_size, 190 / coefficient_size), 60 / coefficient_size, 1)

    ellipse(surface_all, color_cat,
            (390 / coefficient_size, 190 / coefficient_size, 40 / coefficient_size, 90 / coefficient_size))
    ellipse(surface_all, black_color,
            (390 / coefficient_size, 190 / coefficient_size, 40 / coefficient_size, 90 / coefficient_size), 1)
    ellipse(surface_all, color_cat,
            (70 / coefficient_size, 190 / coefficient_size, 80 / coefficient_size, 40 / coefficient_size))
    ellipse(surface_all, black_color,
            (70 / coefficient_size, 190 / coefficient_size, 80 / coefficient_size, 40 / coefficient_size), 1)
    ellipse(surface_all, color_cat,
            (40 / coefficient_size, 120 / coefficient_size, 50 / coefficient_size, 80 / coefficient_size))
    ellipse(surface_all, black_color,
            (40 / coefficient_size, 120 / coefficient_size, 50 / coefficient_size, 80 / coefficient_size), 1)

    # Head
    circle(surface_all, color_cat,
           (80 / coefficient_size, 110 / coefficient_size), 80 / coefficient_size)
    circle(surface_all, black_color,
           (80 / coefficient_size, 110 / coefficient_size), 80 / coefficient_size, 1)

    # Right an ear
    polygon(surface_all, color_cat,
            ((75 / coefficient_size, 45 / coefficient_size),
             (130 / coefficient_size, 60 / coefficient_size),
             (130 / coefficient_size, 0)))
    polygon(surface_all, black_color,
            ((75 / coefficient_size, 45 / coefficient_size),
             (130 / coefficient_size, 60 / coefficient_size),
             (130 / coefficient_size, 0)), 1)  # border
    polygon(surface_all, color_ear,
            ((95 / coefficient_size, 40 / coefficient_size),
             (125 / coefficient_size, 55 / coefficient_size),
             (125 / coefficient_size, 10 / coefficient_size)))
    polygon(surface_all, black_color,
            ((95 / coefficient_size, 40 / coefficient_size),
             (125 / coefficient_size, 54 / coefficient_size),
             (125 / coefficient_size, 10 / coefficient_size)), 1)  # border

    # Left an ear
    polygon(surface_all, color_cat,
            ((15 / coefficient_size, 65 / coefficient_size),
             (60 / coefficient_size, 45 / coefficient_size),
             (27 / coefficient_size, 0)))
    polygon(surface_all, black_color,
            ((15 / coefficient_size, 65 / coefficient_size),
             (60 / coefficient_size, 45 / coefficient_size),
             (27 / coefficient_size, 0)), 1)  # border
    polygon(surface_all, color_ear,
            ((20 / coefficient_size, 60 / coefficient_size),
             (50 / coefficient_size, 40 / coefficient_size),
             (30 / coefficient_size, 10 / coefficient_size)))
    polygon(surface_all, black_color,
            ((20 / coefficient_size, 60 / coefficient_size),
             (50 / coefficient_size, 40 / coefficient_size),
             (30 / coefficient_size, 10 / coefficient_size)), 1)

    # Right eye
    ellipse(surface_all, color_eyes,
            (100 / coefficient_size, 80 / coefficient_size, 40 / coefficient_size, 60 / coefficient_size))
    ellipse(surface_all, black_color,
            (100 / coefficient_size, 80 / coefficient_size, 40 / coefficient_size, 60 / coefficient_size), 1)
    ellipse(surface_all, black_color,
            (115 / coefficient_size, 90 / coefficient_size, 10 / coefficient_size, 40 / coefficient_size))

    # Left eye
    ellipse(surface_all, color_eyes,
            (30 / coefficient_size, 80 / coefficient_size, 40 / coefficient_size, 60 / coefficient_size))
    ellipse(surface_all, black_color,
            (30 / coefficient_size, 80 / coefficient_size, 40 / coefficient_size, 60 / coefficient_size), 1)
    ellipse(surface_all, black_color,
            (45 / coefficient_size, 90 / coefficient_size, 10 / coefficient_size, 40 / coefficient_size))

    # Nose
    polygon(surface_all, (205, 133, 63),
            ((70 / coefficient_size, 140 / coefficient_size),
             (90 / coefficient_size, 140 / coefficient_size),
             (80 / coefficient_size, 150 / coefficient_size)))
    polygon(surface_all, black_color,
            ((70 / coefficient_size, 140 / coefficient_size),
             (90 / coefficient_size, 140 / coefficient_size),
             (80 / coefficient_size, 150 / coefficient_size)), 1)

    # Lips
    arc(surface_all, black_color,
        (80 / coefficient_size, 142 / coefficient_size, 20 / coefficient_size,
         15 / coefficient_size), 3.14, 2 * 3.14, 2)
    arc(surface_all, black_color,
        (60 / coefficient_size, 142 / coefficient_size, 20 / coefficient_size,
         15 / coefficient_size), 3.14, 2 * 3.14, 2)

    # Mustache
    aalines(surface_all, black_color, False,
            ((90 / coefficient_size, 145 / coefficient_size),
             (120 / coefficient_size, 150 / coefficient_size),
             (150 / coefficient_size, 160 / coefficient_size)), 1)
    aalines(surface_all, black_color, False,
            ((87 / coefficient_size, 147 / coefficient_size),
             (120 / coefficient_size, 160 / coefficient_size),
             (150 / coefficient_size, 180 / coefficient_size)))
    aalines(surface_all, black_color, False,
            ((69 / coefficient_size, 145 / coefficient_size),
             (40 / coefficient_size, 150 / coefficient_size),
             (10 / coefficient_size, 160 / coefficient_size)), 1)
    aalines(surface_all, black_color, False,
            ((71 / coefficient_size, 147 / coefficient_size),
             (40 / coefficient_size, 160 / coefficient_size),
             (10 / coefficient_size, 180 / coefficient_size)), 1)

    if flip == 1:  # mirror surface if flip =1 then don't mirror
        win.blit(surface_all, location)
    else:  # if don't 1 the surface to the mirror
        surface_all2 = py.transform.flip(surface_all, True, False)
        win.blit(surface_all2, location)


def clew(location, coefficient_size):

    # This function creates clew

    color_grey = (128, 128, 128)
    circle(win, color_grey, (location[0], location[1]), 50 / coefficient_size)
    circle(win, (0, 0, 0), (location[0], location[1]), 50 / coefficient_size, 2)

    aalines(win, (0, 0, 0), False,
            ((location[0]-30 / coefficient_size, location[1]+30 / coefficient_size),
             (location[0]-20 / coefficient_size, location[1]+25 / coefficient_size),
             (location[0]-10 / coefficient_size, location[1]+20 / coefficient_size),
             (location[0], location[1]+10 / coefficient_size),
             (location[0]+30 / coefficient_size, location[1]-20 / coefficient_size)))
    aalines(win, (0, 0, 0), False, (
        (location[0]-25 / coefficient_size, location[1]+40 / coefficient_size),
        (location[0]-20 / coefficient_size, location[1]+35 / coefficient_size),
        (location[0]-10 / coefficient_size, location[1]+30 / coefficient_size),
        (location[0], location[1]+20 / coefficient_size),
        (location[0]+30 / coefficient_size, location[1]-10 / coefficient_size)))
    aalines(win, (0, 0, 0), False, (
        (location[0]-30 / coefficient_size, location[1]+20 / coefficient_size),
        (location[0]-20 / coefficient_size, location[1]+10 / coefficient_size),
        (location[0]-10 / coefficient_size, location[1]),
        (location[0], location[1]-10 / coefficient_size),
        (location[0]+20 / coefficient_size, location[1]-40 / coefficient_size)))


py.init()
FPS = 20
win = py.display.set_mode((600, 800))

clock = py.time.Clock()
finish = False

main()
py.display.update()
while not finish:
    for event in py.event.get():
        clock.tick(FPS)
        if event.type == py.quit:
            finish = True

py.quit()
