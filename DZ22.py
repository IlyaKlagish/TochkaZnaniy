import math
import time
# print(math.pi)
# print(math.sqrt(float(input('Введите число: '))))

# r = float(input('Введите радиус круга (число): '))
# sq = math.pi * math.pow(r, 2)
# print(f'Площадь круга с радиусом {r} равенa: {sq}')


# import time
# print('Считаем до 5: ')
# for i in range(1, 6):
#     print(i)
#     time.sleep(1)
# print('Готово!')

# from time import *
# for i in range(100):
#     sleep(0.1)
#     print(time())

# from time import *
# t = 0
# while True:
#     sleep(0.01)
#     t += 1
#     hour = t//3600
#     minutes = (t % 3600) // 60
#     seconds = t % 60
#     print(hour, minutes, seconds, sep=':')

# from datetime import datetime
# date = (datetime.now())
# #print(f'Сегодня {date.strftime("%d-%m-%Y")}')
# print(f'Сегодня {date.strftime("%d-%m-%Y %H:%M")}')
# #print(f'Сегодня {date}')
# birthday = input('Введите дату дня рождения в этом году (дд-мм-гггг): ')
# birthday = datetime.strptime(birthday,"%d-%m-%Y")
# days = (birthday - date).days
# if days < 0:
#     print(f'Ваш день рождения уже прошел в этом году {days}')
# else:
#     print(f'До вашего дня рождения осталось {days} дней')

from time import *

tasks = ['Математика', 'Чтение', 'Игры']
a = input('Введите: ')
if a == 'Математика':
    t = 3600
    for k in range(t):
        sleep(0.001)
        t -= 1
        hour = t // 3600
        minutes = (t % 3600) // 60
        seconds = t % 60
        if t == 2701:
            print('Прошло 15 минут, осталось 45 минут')
        if t == 1801:
            print('Прошло 30 минут, осталось 30 минут')
        if t == 901:
            print('Прошло 45 минут, осталось 15 минут')
        if t == 0:
            print('Задание "Математика" завершено')
elif a == 'Чтение':
    t = 1800
    for k in range(t):
        sleep(0.001)
        t -= 1
        hour = t // 3600
        minutes = (t % 3600) // 60
        seconds = t % 60
        if t == 1201:
            print('Прошло 10 минут, осталось 20 минут')
        if t == 0:
            print('Задание "Чтение" завершено')
elif a == 'Игры':
    t = 2700
    for k in range(t):
        sleep(0.001)
        t -= 1
        hour = t // 3600
        minutes = (t % 3600) // 60
        seconds = t % 60
        if t == 1501:
            print('Прошло 20 минут, осталось 25 минут')
        if t == 0:
            print('Задание "Игры" завершено')