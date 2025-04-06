from turtle import *
from random import *

screen = Screen()
screen.bgcolor("lightblue")

colors = ["red","green","blue","yellow","purple"]
turtles = []
red_wins = 0
green_wins = 0
blue_wins = 0
yellow_wins = 0
purple_wins = 0

for i in range(len(colors)):
    t = Turtle()
    turtles.append(t)

def start_race():
    screen.reset()
    pu()
    ht()
    goto(-200, 140)
    pd()
    rt(90)
    forward(200)
    pu()
    goto(200,140)
    pd()
    forward(200)
    for i, t in enumerate(turtles):
        t.color(colors[i])
        t.shape("turtle")
        t.pu()
        t.goto(-200,100 - i * 30)
    race()
def race():
    while True:
        for t in turtles:
            distance = randint(1,10)
            t.forward(distance)
            if t.xcor() >= 200:
                display_winner(t)
                return
def display_winner(t):
    t.home()
    t.write(t.color()[0] + " черепашка победила!",align="center", font=("Arial",24,"bold"))
    wins(t)
def wins(t):
    if t.color()[0] == "red":
        global red_wins
        red_wins += 1
    elif t.color()[0] == "green":
        global green_wins
        green_wins += 1
    elif t.color()[0] == "blue":
        global blue_wins
        blue_wins += 1
    elif t.color()[0] == "yellow":
        global yellow_wins
        yellow_wins += 1
    elif t.color()[0] == "purple":
        global purple_wins
        purple_wins += 1
    t.goto(0,-100)
    t.color("black")
    t.ht()
    t.write("red: "+str(red_wins)+"  green: "+str(green_wins)+"  blue: "+str(blue_wins)+"  yellow: "+str(yellow_wins)+"  purple: "+str(purple_wins),align="center", font=("Arial",14,"bold"))


screen.listen()
screen.onkey(start_race, "space")

screen.mainloop()