from turtle import *
from random import *

screen = Screen()
screen.bgcolor("black")

enemies = []
active = True
score = 0

score_t = Turtle()
score_t.ht()
score_t.speed(0)
score_t.color("white")
score_t.pu()
score_t.goto(0,100)

player = Turtle()
player.shape("turtle")
player.color("green")
player.pu()
player.speed(0)

def create_enemy():
    global score
    enemy = Turtle()
    enemy.ht()
    enemy.speed(0)
    enemy.shape("turtle")
    enemy.color("red")
    enemy.pu()
    x = -500
    y = randint(-500, 500)
    enemy.goto(x, y)
    enemy.st()
    enemies.append(enemy)
    score += 1
    score_write()

def score_write():
    score_t.clear()
    score_t.write(f"Счет: {score}", align="center", font=("Arial", 24, "bold"))

def go_up():
    y = player.ycor()
    player.sety(y + 20)

def go_down():
    y = player.ycor()
    player.sety(y - 20)

def go_right():
    x = player.xcor()
    player.setx(x + 20)

def go_left():
    x = player.xcor()
    player.setx(x - 20)

screen.listen()
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_right, "d")
screen.onkeypress(go_left, "a")

def game_reset():
    for enemy in enemies:
        enemy.ht()
        enemy.clear()
    enemies.clear()
    player.clear()
    global active, score
    active = True
    score = 0
    score_write()

    game()

def game_over():
    global active
    active = False
    player.home()
    player.write("Вы проиграли!", align="center", font=("Arial", 24, "bold"))
    screen.onkeypress(game_reset, "space")
def game():
    global active
    while active:
        create_enemy()

        for enemy in enemies:
            enemy.fd(randint(10, 30))
            if player.distance(enemy) < 20:
                game_over()
                return

game()
screen.mainloop()