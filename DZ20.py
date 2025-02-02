
# def products(*args):
#     for i in args:
#         print(i)
# products('Ноутбук','Телефон','Компьютер')

# def products_2(**kwargs):
#     for name, products_2 in kwargs.items():
#         print(name, products_2)
# products_2(Apple="телефон",Samsung='Техника')

# def calc(a,b):
#     return a + b, a - b, a * b, a / b
# sum, diff, prod, div = calc(int(input('a : ')), int(input('b : ')))
# print(calc(int(input('Введите число: ')), int(input('Введите число: '))))
# print('Сyмма:', sum)
# print('Разность:', diff)
# print('Поизведение:', prod)
# print('Деление:', div)

# cube = lambda x: x * x * x
# print(cube(int(input('Введите число: '))))

# def factorial(x):
#     if x == 0: return 1
#     else: return x * factorial(x - 1)
# print(factorial(int(input('Введите число: '))))

# def  fairies(a,b):
#         print('Феи: ' + a + ',' +b)
# fairies('Лили','Аля')

def fairies(*args):
    str='Феи: '
    for i in args:
        str = str + i + ', '
    print(str[:-2])

fairies('Лили','Аля')

def troll(**kwargs):
    for troll, s in kwargs.items():
        print('Тролль ' + troll + ' имеет силу ' + s)
troll(Грот='100')

def count(a,b):
    return  a + b
print('Количество существ: ',count(2,1))
