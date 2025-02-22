# from turtle import *
# for i in range(4):
#     forward(100)
#     left(90)
#
# done()

'''Снежинка_1'''
from turtle import *
speed(10)

for i in range(8):
    def snow(x, y):
        forward(x)
        right(45),
        forward(y),
        backward(y),
        left(90),
        forward(y),
        backward(y),
        right(45)

    snow(75, 40)
    snow(40, 20)
    snow(20, 10)
    backward(135)
    left(45)
penup()
backward(15)
right(90)
forward(15)
left(90)
pendown()
for i in range(8):
    forward(50)
    left(135)
    forward(20)
done()

'''Снежинка_2'''
# from turtle import *
# def draw_snow(x,y):
#     forward(y)
#     backward(y)
#     left(360 / x)
#
# x = int(input('Введите число лучей в снежинке: '))
# y = int(input('Введите длину лучей в снежинке: '))
#
# for i in range(x):
#     draw_snow(x,y)
#
# done()
