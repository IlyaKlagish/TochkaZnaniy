from turtle import *

screen = Screen()
screen.setup(800,310)
screen.bgpic("castle.gif")

hero1 = "hero1.gif"
hero2 = "hero2.gif"
hero3 = "hero3.gif"

screen.addshape("hero1.gif")
screen.addshape("hero2.gif")
screen.addshape("hero3.gif")

hero = Turtle()
hero.shape(hero1)
hero.pu()
hero.goto(-300,-60)

images = [hero1, hero2, hero3]
index = 0

def move_hero():
    global index
    hero.fd(10)

    if hero.xcor() > screen.window_width() / 2:
        hero.setheading(180)
    if hero.xcor() < -screen.window_width() / 2:
        hero.setheading(0)
    index = (index + 1) % len(images)
    hero.shape(images[index])
    screen.ontimer(move_hero, 100)

def jump():
    for y in range(0, 50, 4):
        hero.sety(hero.ycor() + 4)
        screen.update()
    for y in range(50, 0, -4):
        hero.sety(hero.ycor() - 4)
        screen.update()

def leave_stamp():
    hero.stamp()

screen.listen()
screen.onkeypress(leave_stamp, 'space')
screen.onkeypress(jump, "Up")

move_hero()
screen.mainloop()