from turtle import *
from random import *

screen = Screen()
screen.bgcolor("tan")

screen.addshape("tank.gif")
screen.addshape("enemy.gif")
game = True

player = Turtle()
player.shape("tank.gif")
player.pu()
player.speed(0)
player.goto(0,-250)

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

score = 0
score_t = Turtle()
score_t.color("white")
score_t.ht()
score_t.pu()
score_t.goto(0,260)

enemies = []

def create_enemy():
    enemy = Turtle()
    enemy.shape("enemy.gif")
    enemy.pu()
    enemy.speed(0)
    x = randint(-390,390)
    enemy.goto(x,300)
    enemies.append(enemy)

def move_enemies():
    for enemy in enemies:
        enemy.setheading(enemy.towards(player))
        enemy.fd(20)

def click_enemy(x,y):
    global score
    for enemy in enemies:
        if enemy.distance(x,y) < 50:
            enemy.goto(randint(-390,390), 300)
            score += 1
            score_t.clear()
            score_t.write(f"{score}", align="center", font=("Arial", 16))

def reset_game():
    global score
    global game

    score = 0
    game = True
    score_t.clear()
    score_t.write(f"{score}", align="center", font=("Arial", 16))
    player.clear()
    player.goto(0,-250)

    for enemy in enemies:
        enemy.ht()
    enemies.clear()

    for i in range(5):
        create_enemy()

def game_over():
    global game
    for enemy in enemies:
        if player.distance(enemy) < 20:
            game = False
            player.home()
            player.write("Вы проиграли!", align="center", font=("Arial", 24, "bold"))
            screen.update()
            screen.ontimer(reset_game, 2000)
            return True
    return False

screen.listen()
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_right, "d")
screen.onkeypress(go_left, "a")
screen.onclick(click_enemy)

for i in range(5):
    create_enemy()

while True:
    if game:
        screen.update()
        move_enemies()
        game_over()
    else:
        screen.update()