import random
from time import sleep


class Player:

    """Главный герой."""

    # Атрибуты героя
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    # Создание героя
    @staticmethod
    def create_hero(name, race):

        # В зависимости от выбранного персонажа - свой уровень урона и здоровья
        if race == "эльф":
            damage = 7
            hp = 10
        elif race == "гном":
            damage = 5
            hp = 12
        elif race == "хоббит":
            damage = 2
            hp = 15
        elif race == "ассасин":
            damage = 6
            hp = 11
        elif race == "человек":
            damage = 3
            hp = 13
        elif race == "маг":
            damage = 4
            hp = 14
        else:
            print("Не распознан выбранный персонаж!\nБудет создан персонаж по умолчанию.")
            hp = 15
            damage = 2

        # Создание персонажа
        return Player(name, hp, damage)

    # Метод атаки героя
    def hero_attack(self, vrag):
        print('Ты стремительно наносишь удар..\n')
        sleep(sleep_time)
        # Вероятность попадания в голову, тело или промах
        event = random.randint(1, 3)
        if event == 1:
            print('И попадаешь прямо в голову!!!\n')
            sleep(sleep_time)
            enemy.hp -= self.damage
        elif event == 2:
            print(f'Удар принимает тело {enemy.name}, и ему приходится не сладко. )))\n')
            sleep(sleep_time)
            enemy.hp -= self.damage / random.randint(2, 4)
        elif event == 3:
            print('Но... наверное ты забыл о том, что это битва... промахнулся.. :-((\n')
            sleep(sleep_time)
        # Проверка, жив ли враг
        if enemy.hp <= 0:
            plus_hp = random.randint(1, 10)
            self.hp += plus_hp
            print(f'{enemy.name} повержен! Ты получаешь {plus_hp} здоровья :-)\n')
            # Если враг повержен, то вернем False рассказать об этом
            return False
        else:
            print('Ты нанес достойный удар, но не достаточно хороший...\n')
            print(f'У {enemy.name} осталось {enemy.hp} здоровья.\n')
            sleep(sleep_time)
            # Если враг жив, то вернем True рассказать об этом
            return True


class Enemy:
    """Враг."""
    # Атрибуты врага
    def __init__(self):
        self.name = random.choice(enemies)
        self.hp = random.randint(1, 10)
        self.damage = random.randint(1, 5)

    # Метод атаки врага
    def enemy_attack(self, hero):
        print(f'{self.name} занес мощнейший удар..\n')
        sleep(sleep_time)
        # Куда попал враг, на помощь приходит атрибут скорости героя
        event = random.randint(1, 3)
        if event == 1:
            print(f'{self.name} попадает прямиком в голову... ухххх....\n')
            sleep(sleep_time)
            hero.hp -= self.damage
        elif event == 2:
            print(f'{self.name} целится тебе в тело... сделай же что-нибудь....\n')
            sleep(sleep_time)
            hero.hp -= self.damage / 2
        elif event == 3:
            print(f'{self.name} похоже плохо целится... интересно, он вообще попадет?!?!..\n')
            sleep(sleep_time)
            hero.hp -= self.damage / 3
        # Проверка, остался ли герой жив
        if hero.hp <= 0:
            print(f'Ты повержен!\nЭто был славный путь... Но ты не дошел до конца..')
            hero.game_over = True
        else:
            print(f'{self.name} провел атаку, но ты выстоял!\n')
            sleep(sleep_time)
            print(f'У тебя осталось {hero.hp} здоровья.\n')
            sleep(sleep_time)

def combat():
    print(f'Характеристики {enemy.name}: {enemy.hp} здоровья, {enemy.damage} урона.\n')
    print(f'Твои характеристики: {player.hp} здоровья, {player.damage} урона.\n')
    sleep(sleep_time)
    answer = input('В атаку или бежим (+, -)?')
    print()
    if answer == "+":
        is_enemy_alive = player.hero_attack(enemy)
        if is_enemy_alive:
            enemy.enemy_attack(player)
            if player.hp > 0:
                combat()
            else:
                return
    elif answer == "-":
        print('Бежать... пока есть силы... я еще не готов..\n')
        sleep(sleep_time)
        # Вероятность побега
        event = random.randint(1, 2)
        if event == 1:
            print(f'Благодаря своей скорости, тебе удается играючи покинуть поле боя..\n')
            sleep(sleep_time)
        else:
            print(f'''Не смотря на свою скорость , ты бежишь уворачиваясь...
Но {enemy.name} все равно успевает тебе нанести удар.. удар в спину.. подлый удар в спину...\n''')
            sleep(sleep_time)
            enemy.enemy_attack(player)
    else:
        print('У тебя не получается сосредоточиться, повтори свое решение!')
        sleep(sleep_time)
        combat()


# Перечень возможных рас и персонажей
heroes = ['эльф', 'гном', 'хоббит', 'ассасин', 'человек', 'маг']

# Перечень возможных врагов
enemies = ['орк', 'гоблин']

# Параметр скорости самой игры
sleep_time = 4

# Приветствие игры
print("Здравствуй путник!\n")
sleep(sleep_time)
print("Что привело тебя в наш мир...\nОн далеко не добр и не учтив..\n")
sleep(sleep_time)
print("""Придется не сладко..
Но как бы не было - я очень рад видеть новое лицо на этих землях!
Назови себя..\n""")
sleep(sleep_time)

# Ввод имени
name = input("Ваше имя: ")

print(f'''\nКакое необычное имя.... {name}...\n''')
sleep(sleep_time)
print(f"""Вспомнил пророчество, в котором говорилось,
что некий {name} освободит наши земли от зла..\n""")
sleep(sleep_time)
print('Может это ты?! Ха-ха.. Не думаю...\n')
sleep(sleep_time)

print(f'''Не могу распознать твою расу из-за лохмотьев на тебе...
Кто ты: {', '.join(heroes)}?\n''')
sleep(sleep_time)

# Ввод расы
race = input("Ваша раса: ").lower()

print(f'''\nДавно я не видел {race}-ов...
Даже промелькнула идея - а вдруг пророчество не врет....\n''')
sleep(sleep_time)

# Создание главного героя
player = Player.create_hero(name, race)

# Вывод характеристик для пользователя
print('''\nХа, я вижу кто ты ))
Расскажу и тебе, потому что похоже ты не помнишь...\n''')
sleep(sleep_time)

print(f'Ты {race}, а значит у тебя {player.hp} здоровья и {player.damage} урона.\n')
sleep(sleep_time)

print('Удачи путник! Пропускаю тебя.. Ни пуха... Ни пера.. Как говорится.. хмм..\n')
sleep(sleep_time)

# Игровой цикл
while True:
    if player.hp > 0:
        # Событие - встречается нам кто-то или нет
        event = random.randint(1, 2)
        if event == 1:
            print('''Здесь все чисто, зла нет.. Но..
На горизонте виднеется что-то темное.. возможно злое..
нужно бы направиться туда и проверить..\n''')
            sleep(sleep_time)
        elif event == 2:
            enemy = Enemy()
            print(f'Вы замечаете неподалеку {enemy.name}...\n')
            print('Что же сделать - остаться пока незамеченным или начать внезапную атаку..\n')
            sleep(sleep_time)
            combat()
    else:
        print('''Это был хороший опыт... может в следующей жизни все будет по другому..
А может ты пока не был тем самым избранным, о котором говорилось в пророчестве..
И в следующий раз - это все таки будешь ты!''')
