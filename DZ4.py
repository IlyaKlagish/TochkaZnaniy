'''
out = ''
a = input('Введи код: ')
for i in range(0,len(a)):

    print(i+1, a[i], chr(1040 + i)* int(a[i]))
    if a[i] == '0':
        out ='Ловушка!'
        break
    else:
        out = out + chr(1040 + i)* int(a[i])

print(out)
'''
import random

treasures = ("бриллианты", "рубины", "изумруды", "золотые монеты", "жемчуг")

chest1 = random.choice(treasures), random.choice(treasures), random.choice(treasures), random.choice(treasures), random.choice(treasures)
print('Сундук 1: ',chest1)
chest2 = random.choice(treasures), random.choice(treasures), random.choice(treasures), random.choice(treasures), random.choice(treasures)
print('Сундук 2: ', chest2)
chest3 = random.choice(treasures), random.choice(treasures), random.choice(treasures), random.choice(treasures), random.choice(treasures)
print('Сундук 3: ', chest3)

