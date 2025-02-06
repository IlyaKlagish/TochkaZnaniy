import random

def start_game():
    name = input('Как тебя зовут?\n')
    print(name, ', добро пожаловать в текстовый квест!')
    Hp = 100

    stats = {
        'имя': name,
        'здоровье': Hp,
        'уровень': 1
    }
    show_stats(stats)
    game_stop = False

    while game_stop is False:
        first_choice(stats)
        show_stats(stats)
        if stats['здоровье'] <= 0:
            print('Увы, вы проиграли.')
            continue_game = input('Хотите продолжить приключения? (да/нет)')
            if continue_game.lower() != 'да':
                print('"Спасибо за игру! До новых встреч!')
                game_stop = True
        if stats['уровень'] >= 20:
            print('Ты победил в игре!')
            continue_game = input('Хотите продолжить приключения? (да/нет)')
            if continue_game.lower() != 'да':
                print('"Спасибо за игру! До новых встреч!')
                game_stop = True

def show_stats(stats):
    print(f"Здоровье: {stats['здоровье']}\nУровень: {stats['уровень']}")

def first_choice(stats):
    choice = input('Ты стоишь на развилке. Пойти прямо, налево или направо?  (введите "прямо", "налево" или "направо")')

    if choice == random.choice(["прямо","налево","направо"]):
        encounter_dragon(stats)
    else:
        all_f = [find_treasure, ravine, abandoned_castle]
        get_random = random.choice(all_f)
        return get_random(stats)

def encounter_dragon(stats):
    print('Ты встретил дракона!')
    action = input('Ты хочешь сражаться или убежать? (введите "сражаться" или "убежать")')
    if action == 'сражаться':
        if random.random() < 0.5:
            print('Ты победил дракона!')
            stats['здоровье'] += 30
            stats['уровень'] += 2
            print('Ты повысил уровень и восстановил здоровье!')
        else:
            damage = random.randint(30,50 )
            stats['здоровье'] -= damage
            print(f'Дракон ранил тебя на {damage} здоровья')
    elif action == 'убежать':
        print('Ты успешно убежал от дракона.')
    else:
        encounter_dragon(stats)

def find_treasure(stats):
    treasure = random.choice(['Золотые монеты', 'Магический артефакт', 'Древняя книга', 'Яд', 'Эликсир'])
    print(f'Ты нашел {treasure}!')

    if treasure == 'Золотые монеты':
        stats['уровень'] += 1
        print('Ты повысил уровень!')
    if treasure == 'Магический артефакт':
        stats['здоровье'] += 10
        print('Ты восстановил немного здоровья!')
    if treasure == 'Древняя книга':
        stats['уровень'] += 1
        print('Ты повысил уровень!')
    if treasure == 'Яд':
        damage = random.randint(10, 20)
        stats['здоровье'] -= damage
        print(f'Ты потерял {damage} здоровья.')
    if treasure == 'Эликсир':
        health = random.randint(10, 20)
        stats['здоровье'] += health
        print(f'Ты получил {health} здоровья')

def abandoned_castle(stats):
    print('Ты попал в заброшенный замок!')
    action = input('Ты хочешь исследовать, убежать или попытаться открыть дверь? (введите "исследовать" или "убежать" или "открыть дверь")')
    if action == 'исследовать':
        if random.random() > 0.2:
            print('Ты прошел через этот замок!')
        else:
            print('Ты встретил призрака!')
            stats['здоровье'] -= 15
            stats['уровень'] += 1
    elif action == 'открыть дверь':
        if random.random() < 0.5:
            print('Тебе удалось открыть дверь и ты нашел магический предмет!')
            stats['здоровье'] += 10
        else:
            print('Увы, тебе не повезло! Ты потерял немного здоровья.')
            stats['здоровье'] -= 5
    elif action == 'убежать':
        print('Ты успешно убежал из замка!')
    else:
        abandoned_castle(stats)
    return
def ravine(stats):
    print('Ты попал в овраг!')
    action = input('Ты хочешь идти дальше или собрать лечебные травы? (введите "идти дальше" или "собрать травы") ')
    if action == 'собрать травы':
        if random.random() > 0.3:
            print('Увы, ты не нашел ничего полезного.')
        else:
            health = random.randint(10, 20)
            stats['здоровье'] += health
            print(f'Ты нашел травы и восстановил {health} здоровья')
    elif action == 'идти дальше':
        print('Ты решил идти дальше!')
    else:
        ravine(stats)
    return

start_game()