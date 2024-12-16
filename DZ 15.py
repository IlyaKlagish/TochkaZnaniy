# text = "Москва, ул Пушкина, д 50"
# words = text.split(",")
# print(words)
# print(text.split(", "))
# print("Город: " + words[0])
#
# films = ["Шрек", "Трансформеры", "Человек-паук"]
# print("Фильмы:", ", ".join(films))
# films.sort(reverse=True)
# print(films)

prompt = "ключ1,ключ2,ключ3,ключ4,ключ5"
keys = prompt.split(",")
print(keys)
if "ключ3" in keys:
    print("Ключ 3 найден! " + "Индекс: ", keys.index("ключ3"))
else:
    print("Ошибка")

places = ['пещера', 'лес', 'река', 'гора', 'болото']
places.sort()
print("Отсортированные места: ", places)

print("Созданный код: ", keys.index("ключ3"),'-',places[1], sep=(""))

if "2-гора" in "2-гора":
    print("Сундук открыт!")
else:
    print("Ошибка!")