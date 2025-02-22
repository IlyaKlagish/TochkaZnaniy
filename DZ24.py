# from random import *
# from turtle import *
# shape('turtle')
# speed(0)
# width(7)
# def random_color():
#     return(random(), random(), random())
# def draw_SPIRAL():
#     for i in range(1000):
#         color(random_color())
#         forward(i)
#         right(121)
# draw_SPIRAL()
# done()

# from turtle import *
# shape('turtle')
# color('#497feb')
#
# begin_fill()
# for i in range(4):
#     forward(150)
#     left(90)
#
# end_fill()
# done()

from turtle import *
speed(0)
left(90)
bgcolor('black')
# bgcolor('#8B4513')
# bgcolor('#008000')
def figure(x):
    for i in range(7):
        # color('purple')
        begin_fill()
        forward(100)
        right(40)
        forward(100)
        right(140)
        forward(100)
        right(40)
        forward(100)
        right(80)
        end_fill()
figure(color('yellow'))
right(30)
figure(color('purple'))
right(15)
figure(color('#ee71f5'))

penup()
right(45)
forward(400)
pendown()

colors = ('red','orange','yellow','blue','purple','green')
for i in range(200):
    pencolor(colors[i%6])
    width(i/100+1)
    forward(i)
    left(59)
penup()
right(90)
forward(600)
pendown()

from random import *
width(5)
def random_color():
    return(random(), random(), random())
def draw_SPIRAL():
    for i in range(400):
        color(random_color())
        forward(i)
        right(121)
draw_SPIRAL()

done()