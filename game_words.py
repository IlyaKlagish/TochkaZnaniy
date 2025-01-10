import random

words = ("питон", "программирование", "компьютер", "игра")
word = random.choice(words)
letters = set()
attemps = 6
win = False
print("Я загадал слово. У тебя есть",attemps,"попыток")
while not win:
    current = ""
    for letter in word:
        if letter in letters:
            current += letter
        else:
            current += "_"
    print("Слово:", current)

    letter = input("Угадай букву:")
    if letter in letters:
        print("Ты уже угадал эту букву!")
    elif letter in word:
        letters.add(letter)
        print("Правильно!")
    else:
        attemps -= 1
        print("Неправильно! У тебя осталось", attemps, "попыток")

    if attemps <= 0:
        print("Увы, ты проиграл. Загаданное слово было",word)
        a = input('Хотите сыграть еще раз? (нет/да): ')
        if a == 'да':
            win = True
            attemps = 6
            letters = set()
            word = random.choice(words)

        elif a == 'нет':
            print('Досвидания!')
            break

    win = True
    for letter in word:
        if letter not in letters:
            win = False
            break

    if win:
        print("Поздравляю! Ты угадал слово:", word)
        break