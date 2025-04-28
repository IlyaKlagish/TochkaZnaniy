from turtle import *
from random import *

screen = Screen()
screen.setup(800,600)
screen.bgpic('fon.gif')

screen.addshape("cat.gif")
screen.addshape("dog.gif")
screen.addshape("tiger.gif")

player = Turtle()
player.shape("cat.gif")
player.pu()

enemy = Turtle()
enemy.shape("dog.gif")
enemy.pu()
enemy.goto(100,0)
enemy.speed(1)

enemy2 = Turtle()
enemy2.shape("tiger.gif")
enemy2.pu()
enemy2.goto(-200,0)
enemy2.speed(0.5)

def move_player(x, y):
    player.goto(x,y)

def move_enemy():
    x = randint(-380,380)
    y = randint(-280,280)
    enemy.goto(x, y)

def move_enemy2():
    x = player.xcor() - randint(40,100)
    y = player.ycor() - randint(40,100)
    enemy2.goto(x, y)
def game():
    move_enemy()
    move_enemy2()
    if player.distance(enemy) < 64:
        player.write("Вы проиграли!", align="center",font=("Arial",24,"bold"))
        return
    # screen.ontimer(game, 1000)
    elif player.distance(enemy2) < 64:
        player.write("Вы проиграли!", align="center",font=("Arial",24,"bold"))
        return
    screen.ontimer(game, 1000)

game()
screen.onclick(move_player)
screen.mainloop()