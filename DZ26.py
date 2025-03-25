import random
from turtle import *
from random import *

Screen().bgcolor("skyblue")
speed(0)
def draw_glass():
    pu()
    goto(-1000,-200)
    pd()
    color("green")
    begin_fill()
    for i in range(2):
        fd(2000)
        rt(90)
        fd(300)
        rt(90)
    end_fill()

def draw_house():
    pu()
    goto(-100,-200)
    pd()
    color('brown')
    begin_fill()
    for i in range(3):
        fd(200)
        lt(90)
    end_fill()
    color("#ed8713")
    begin_fill()
    goto(-100,0)
    goto(0,100)
    goto(100,0)
    end_fill()

def draw_cloud():
    pu()
    goto(randint(-1000,1000),randint(100,300))
    pd()
    color("azure")
    for i in range(randint(3,6)):
        begin_fill()
        circle(randint(10,30))
        rt(randint(30,90))
        end_fill()

def draw_sun():
    pu()
    goto(-400,200)
    pd()
    color("yellow")
    begin_fill()
    circle(50)
    end_fill()

def draw_tree(x,y,height):
    pu()
    goto(x,y)
    setheading(270)
    pd()
    for i in range(3):
        begin_fill()
        color("#8c510d")
        left(90)
        fd(20)
        lt(90)
        fd(height)
        end_fill()
    for i in range(randint(5,6)):
        color("green")
        begin_fill()
        circle(randint(30,50))
        rt(randint(30,90))
        end_fill()

def draw_window():
        pu()
        goto(-50, -150)
        setheading(0)
        pd()
        color("grey","blue")
        width(5)
        begin_fill()
        for i in range(4):
            fd(100)
            lt(90)
        end_fill()

        pu()
        goto(0,-150)
        pd()
        color("grey")
        width(5)
        setheading(90)
        fd(100)

        pu()
        goto(-50,-100)
        pd()
        rt(90)
        fd(100)

def draw_flowers():
    pu()
    goto(randint(-1000, 1000), randint(-300, -200))
    pd()
    color("#ed13a8")
    for i in range(randint(1, 3)):
        begin_fill()
        circle(randint(10, 15))
        rt(randint(30, 90))
        end_fill()

draw_glass()
draw_house()
for i in range(20):
    draw_cloud()
draw_sun()
draw_tree(-200,-200,200)
draw_tree(200,-200,200)
draw_window()
for i in range(20):
    draw_flowers()

done()
