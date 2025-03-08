# from turtle import *
#
# # write('Привет!',font=('Impact',20))
# k = 200
#
# def draw_axes():
#     penup()
#     goto(-k,0)
#     pendown()
#     goto(k,0)
#     penup()
#     goto(0,-k)
#     pendown()
#     goto(0,k)
#
# def draw():
#     for i in range(-k, k+1, 50):
#         if i != 0:
#             penup()
#             goto(i,0)
#             dot()
#             goto(i,-20)
#             write(str(i))
#         if i !=0:
#             penup()
#             goto(0,i)
#             dot()
#             goto(-20,i)
#             write(str(i))
#         if i == 0:
#             penup()
#             goto(10,-20)
#             write(str(i))
#
# draw_axes()
# draw()
# done()

from turtle import *
penup()
goto(50,50)
dot(15,'red')
goto(-70,30)
dot(15,'blue')
goto(0,-80)
dot(15,'green')

goto(-20,0)
write('КЛАД!',font=('Impact',10))

home()
done()