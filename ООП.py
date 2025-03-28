from turtle import *
from random import *
'''
screen = Screen()
screen.bgcolor("Lightgreen")

t1 = Turtle()
t1.shape("turtle")
t1.color("blue")
t1.pu()
t1.goto(-200,0)
t1.pd()
t1.fd(100)

t2 = Turtle()
t2.shape("turtle")
t2.color("red")
t2.pu()
t2.goto(200,0)
t2.pd()
t2.lt(180)
t2.fd(100)


turtles = []

colors = ["red", "blue", "green", "yellow", "purple"] * 10

for color in colors:
    t = Turtle()
    t.color(color)
    t.shape("turtle")
    t.speed(0)
    turtles.append(t)

def draw(t):
    for i in range(4):
        t.fd(100)
        t.rt(90)

for i, t in enumerate(turtles):
    t.pu()
    t.goto(-200 + i * 10, 0)
    t.pd()
    draw(t)
'''
screen = Screen()
screen.bgcolor("Lightgreen")

t1 = Turtle()
t1.shape("turtle")
t1.color("red")
t1.pu()
t1.goto(-200,0)
t1.pd()
for i in range(4):
    t1.fd(100)
    t1.rt(90)

t2 = Turtle()
t2.shape("circle")
t2.color("blue")
t2.pu()
t2.goto(100,-100)
t2.pd()
for i in range(3):
    t2.fd(100)
    t2.lt(120)

t3 = Turtle()
t3.shape("arrow")
t3.color("yellow")
t3.pu()
t3.goto(0,-200)
t3.pd()
t3.circle(50)

screen.exitonclick()
