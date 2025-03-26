from turtle import *
'''''
def koch(order, size):
    if order == 0: fd(size)
    else:
        koch(order - 1, size / 3)
        left(60)
        koch(order - 1, size / 3)
        right(120)
        koch(order - 1, size / 3)
        left(60)
        koch(order - 1, size / 3)

def draw_snowflake():
    koch(5,400)
    right(120)

def main_koch():
    speed(0)
    pu()
    goto(-200,100)
    pd()
    draw_snowflake()
    draw_snowflake()
    draw_snowflake()
    done()
main_koch()

'''''
def draw_branch(n, w):
    width(w)
    if n > 5:
        forward(n)
        # width(w)
        right(20)
        draw_branch(n - 10, w - 1)
        left(40)
        draw_branch(n - 10, w - 1)
        right(20)
        backward(n)


def main_tree():
    speed(0)
    pu()
    left(90)
    backward(200)
    width(10)
    color("brown")
    pd()
    draw_branch(100,10)
    done()
main_tree()
