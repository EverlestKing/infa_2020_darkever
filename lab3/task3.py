import pygame as py
from pygame.draw import *


def window(x0, y0, koff,location) :
    # function creature window
    surface_window = py.Surface( (x0 /koff,y0/koff) )
    surface_window.fill( (255, 255, 255) )

    color_window = 0, 191, 255

    rect( (surface_window), (color_window), (10/koff, 10/koff, 80/koff, 100/koff) )
    rect( (surface_window), (color_window), (110/koff, 10/koff, 80/koff, 100/koff) )

    rect( surface_window, (color_window), (10/koff, 130/koff, 80/koff, 140/koff) )
    rect( surface_window, (color_window), (110/koff, 130/koff, 80/koff, 140/koff) )

    win.blit( surface_window, (location) )


def koshka(x0, y0, n ,color_cat, location,flip) :
    #ALL SURFACE
    surface_all = py.Surface( (x0 , y0 ) )
    surface_all.fill( (222, 184, 135) )

    # tail cat with a turn
    color_ear = (205,133,63)
    color_eyes = (180, 220, 0)
    surface_tail = py.Surface( (320 / n, 100 / n) )  # create surface
    surface_tail.fill( (222, 184, 135) )
    black = (0,0,0)


    ellipse( surface_tail, color_cat, (0, 0, 300/n, 100/n) )  # tail
    ellipse( surface_tail, black, (0, 0, 300/n, 100/n), 1 )  # tail 2 ottline
    surface_tail = py.transform.rotate( surface_tail, 160 )  # turn tail
    surface_all.blit( surface_tail, (330 / n, 80 / n) )  # surface_tail in a surface_all

    # body
    ellipse( surface_all, color_cat, (40 / n, 30 / n, 400/n, 190/n) )
    ellipse( surface_all, black, (40 / n, 30 / n, 400/n, 190/n), 1 )

    circle( surface_all, color_cat, (360 / n, 190 / n), 60 / n )
    circle( surface_all, black, (360 / n, 190 / n), 60 / n, 1 )

    ellipse( surface_all, color_cat, (390 / n, 190 / n , 40 / n, 90/n) )
    ellipse( surface_all, black, (390/n, 190/n, 40/n,90/n), 1 )

    ellipse( surface_all, color_cat, (70/n, 190/n, 80/n, 40/n) )
    ellipse( surface_all, black, (70/n, 190/n, 80/n, 40/n), 1 )

    ellipse( surface_all, color_cat, (40/n, 120/n, 50/n, 80/n) )
    ellipse( surface_all, black, (40/n, 120/n, 50/n, 80/n), 1 )

    # head
    circle( surface_all, color_cat, (80 / n, 110 / n), 80 / n )
    circle( surface_all, black, (80 / n, 110 / n), 80 / n, 1 )

    # right earn
    polygon( surface_all, color_cat, ((75 / n, 45 / n), (130 / n, 60 / n), (130 / n, 0)) )
    polygon( surface_all, black, ((75 / n, 45 / n), (130 / n, 60 / n), (130 / n, 0)), 1 )

    polygon( surface_all, color_ear, ((95 / n, 40/n), (125/n, 55/n), (125/n, 10/n)) )
    polygon( surface_all, black, ((95/n, 40/n), (125/n, 54/n), (125/n, 10/n)), 1 )

    # left earn
    polygon( surface_all, color_cat, ((15/n, 65/n), (60/n, 45/n), (27/n, 0)) )
    polygon( surface_all, black, ((15/n, 65/n), (60/n, 45/n), (27/n, 0)), 1 )

    polygon( surface_all, color_ear, ((20/n, 60/n), (50/n, 40/n), (30/n, 10/n)) )
    polygon( surface_all, black, ((20/n, 60/n), (50/n, 40/n), (30/n, 10/n)), 1 )

    # right eye
    ellipse( surface_all, color_eyes, (100/n, 80/n, 40/n, 60/n) )
    ellipse( surface_all, black, (100/n, 80/n, 40/n, 60/n), 1 )
    ellipse( surface_all, black, (115/n, 90/n, 10/n, 40/n) )

    # left eye
    ellipse( surface_all, color_eyes, (30/n, 80/n, 40/n, 60/n) )
    ellipse( surface_all, black, (30/n, 80/n, 40/n, 60/n),  1 )
    ellipse( surface_all, black, (45/n, 90/n, 10/n, 40/n) )

    # noise
    polygon( surface_all, (205, 133, 63), ((70/n, 140/n), (90/n, 140/n), (80/n, 150/n)) )
    polygon( surface_all, black, ((70/n, 140/n), (90/n, 140/n), (80/n, 150/n)), 1 )

    # math
    arc( surface_all, black, (80/n, 142/n,20/n, 15/n), 3.14, 2 * 3.14, 2 )
    arc( surface_all, black, (60/n, 142/n, 20/n, 15/n), 3.14, 2 * 3.14, 2 )

    # mustache
    aalines( surface_all, black, False, ((90/n, 145/n), (120/n, 150/n), (150/n, 160/n)), 1 )
    aalines( surface_all, black, False, ((87/n, 147/n), (120/n, 160/n), (150/n, 180/n)) )
    aalines( surface_all, black, False, ((69/n, 145/n), (40/n, 150/n), (10/n, 160/n)), 1 )
    aalines( surface_all, black, False, ((71/n, 147/n), (40/n, 160/n), (10/n, 180/n)), 1 )

    if flip ==1: # mirror surface if flip =1 then don't mirror
        win.blit( surface_all, (location) )
    else:   # if don't 1 the surface to the mirror
        surface_all2 =  py.transform.flip ( surface_all, True, False )
        win.blit( surface_all2, (location) )


def clew(x0, y0, razmer_coff) :
    color_grey = (128, 128, 128)
    circle( win, color_grey, (x0, y0), 50 / razmer_coff )
    circle( win, (0, 0, 0), (x0, y0), 50 / razmer_coff, 2 )

    aalines( win, (0, 0, 0), False,
             ((x0 - 30 / razmer_coff, y0 + 30 / razmer_coff),
              (x0 - 20 / razmer_coff, y0 + 25 / razmer_coff),
              (x0 - 10 / razmer_coff, y0 + 20 / razmer_coff),
              (x0, y0 + 10 / razmer_coff),
              (x0 + 30 / razmer_coff, y0 - 20 / razmer_coff)) )
    aalines( win, (0, 0, 0), False, (
        (x0 - 25 /razmer_coff, y0 + 40 /razmer_coff),
        (x0 - 20 /razmer_coff, y0+35 /razmer_coff),
        (x0-10/razmer_coff, y0 +30/razmer_coff),
        (x0 , y0+20/razmer_coff),
        (x0 +30 /razmer_coff, y0 -10 / razmer_coff)) )
    aalines( win, (0, 0, 0), False, (
        (x0 -30 /razmer_coff, y0+20 /razmer_coff),
        (x0-20/razmer_coff, y0+10/razmer_coff),
        (x0-10/razmer_coff, y0),
        (x0 , y0-10/razmer_coff),
        (x0 +20 /razmer_coff, y0 - 40 /razmer_coff)) )


py.init()
FPS = 20
win = py.display.set_mode( (600, 800) )

clock = py.time.Clock( )
finish = False

# Background
rect( win, (180, 69, 19), (0, 0, 600, 400) )
rect( win, (222, 184, 135), (0, 380, 600, 400) )

# draw window
window( 200,300, 1.24,(350,50))
window(200,300, 1,(50,50))

#draw cats
koshka(150,100,3.14,(150, 75, 0), (0,380),-1)
koshka(300,200, 1.89, (150, 75, 0) ,(300,380),1)
koshka(350,200,1.90,(128, 128,128), (20,500),-1)
koshka(200,150,3.67,(0,0,0) ,(450,650),1)
koshka(200,150,3.67,(255,255,255),(50,700),-1)

#draw clew's
clew(300,750,4)
clew (160,460,2.34)
clew (430,600,2.0)


py.display.update( )

while not finish :
    for event in py.event.get( ) :
        clock.tick( FPS )
        if event.type == py.quit :
            finish = True
py.quit( )
