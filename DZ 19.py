
# def hi():
#     print('Hi')
# hi()
#
# k = 0
# def inc():
#     global k
#     k += 1
# inc()
# print(k)
#
# def sq(side):
#     print(side * side)
# sq(5)
# sq(1024)
#
# def sq(width, height):
#     print(width * height)
# sq(5, 10)
#
# def greet(name='Гость'):
#     print("Привет, " + name)
#
# greet()
# greet('Илья')
# greet(input('Введите имя:'))


game=True
def book_tickets():
    a = input('Введите название города: ')
    k = input('Введите количество дней: ')

    print('Билеты звбронированы на ' + a + ' на ' + k + ' дней.')

def find_hotel():
    place = input('Введите название города: ')
    k = input('Введите количество звезд: ')

    print('Гостиница найдена в ' + place + ' (' + k + ' звезд)')

def buy_souvenirs():
    place = input('Введите название города: ')
    k = input('Введите количество денег: ')
    print('Сувениры куплены ' + place + ' (' + k + ' рублей)')

def travel_plan():
    print('Выберите действие:')
    a = print('1. Забронировать билеты')
    b = print('2. Найти гостиницу')
    c = print('3. Купить сувениры')
    d = print('4. Выход')
travel_plan()

nnn = (input('Ваш выбор:'))
if nnn == '1':
    book_tickets()
if nnn == '2':
    find_hotel()
if nnn == '3':
    buy_souvenirs()
elif nnn == '4':
    print('Удачи!')
    game=False