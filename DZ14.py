
diary = []
diary.append("Пойти в школу")
diary.append("Помочь маме")
diary.append("Играть в игру")
diary.append("Изучать списки")
diary.append("Посмотреть фильм")
print("Записи в дневнике: ")
for entry in diary:
    # print("Записи в дневнике: ")
    print(entry)
print("Обновленные записи в дневнике: ")
diary[3] = "Понять списки!"
diary.append("Прочитать книгу")
del diary[0]

for entry in diary:
    print(entry)