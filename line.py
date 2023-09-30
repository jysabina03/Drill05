import random
from pico2d import *


TUK_WIDTH,TUK_HEICHT=1280,1024
open_canvas(TUK_WIDTH,TUK_HEICHT)
character = load_image('animation_sheet.png')
tuk_ground = load_image('TUK_GROUND.png')

# def stop():
#     turtle.bye()
#
# def draw_big_point(p):
#     turtle.goto(p)
#     turtle.color(0.8, 0.9, 0)
#     turtle.dot(15)
#     turtle.write('     '+str(p))
#
#
# def draw_point(p):
#     turtle.goto(p)
#     turtle.dot(5, random.random(), random.random(), random.random())
#
#
# def draw_line(p1, p2):
#     # fill here
#     draw_big_point(p1)
#     draw_big_point(p2)
#
#     x1,y1=p1[0],p1[1]
#     x2,y2=p2[0],p2[1]
#
#     for i in range(0,100+1,4):
#         t=i/100
#         x=(1-t)*x1+t*x2
#         y=(1-t)*y1+t*y2
#         draw_point((x,y))
#     draw_point(p2)

def make_hand():
    pass

def make_load():
    pass

clear_canvas()
tuk_ground.draw(TUK_WIDTH//2,TUK_HEICHT//2)

update_canvas()
#handle_events()
delay(0.1)

# fill here
#draw_line((-100,-100),(300,150))


close_canvas()
