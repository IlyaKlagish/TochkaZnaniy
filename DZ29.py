from turtle import *
'''
screen = Screen()

shape("turtle")
def move_forward():
    fd(10)
def move_backward():
    bk(10)
def move_stop():
    home()
def move_mouse(x,y):
    goto(x,y)
def move_time():
    setheading(heading() + 90)
    fd(100)
    ontimer(move_time, 1000)

screen.onkey(move_forward, "q")
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward, "s")
screen.onkeyrelease(move_stop, "e")
screen.onscreenclick(move_mouse)

screen.ontimer(move_time, 1000)

screen.listen()
screen.mainloop()
'''

screen = Screen()


t = Turtle()
t.color("blue")
t.shape("turtle")

def move_forward():
    t.fd(10)
def move_backward():
    t.bk(10)
def move_right():
    t.setheading(t.heading() - 90)
    t.fd(10)
def move_left():
    t.setheading(t.heading() + 90)
    t.fd(10)
def move_stop(x,y):
    t.pu()
    t.home()
    t.pd()

screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward, "s")
screen.onkeypress(move_right, "d")
screen.onkeypress(move_left, "a")
screen.onscreenclick(move_stop)

screen.listen()
screen.mainloop()