import telebot, os, random
from telebot.types import ReplyKeyboardMarkup
from dotenv import load_dotenv


class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    @staticmethod
    def create_enemy():
        name = random.choice(enemies)
        hp = random.randint(1, 100)
        damage = random.randint(1, 100)
        return Enemy(name, hp, damage)

class Player:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def set_name(self, name):
        self.name = name

    def  hero_characteristics(self):
        if self.name == 'хоббит':
            self.hp = 75
            self.damage = 35
        elif self.name == 'эльф':
            self.hp = 90
            self.damage = 55
        elif self.name == 'друид':
            self.hp = 100
            self.damage = 45


load_dotenv()
TOKEN = os.getenv('TELEGRAM_RPG_TOKEN')
bot = telebot.TeleBot(TOKEN)

enemies = ['орк', 'Саруман', 'Саурон']
heroes = ['хоббит', 'эльф', 'друид']

hero = Player('рандом', 1, 1)
enemy = Enemy('random', 1, 1)


@bot.message_handler(commands=['start'])
def starting(message):
    text = "Приветствую тебя путник! Назови себя.."
    img = open('./photos/hello.jpg', 'rb')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = 'хоббит'
    btn2 = 'эльф'
    btn3 = 'друид'
    keyboard.add(btn1, btn2, btn3)
    bot.send_photo(message.chat.id, img, caption = text, reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def answer(message):
    global hero, enemy

    def combat():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = 'Вступить в бой'
        btn2 = 'Остаться незамеченным'
        btn3 = 'Меню'
        keyboard.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text= 'Твой выбор?', reply_markup=keyboard)

    if message.text in heroes:
        hero.set_name(message.text)
        hero.hero_characteristics()
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = 'Путешествие'
        btn2 = 'Меню'
        keyboard.add(btn1, btn2)
        img = open('./photo/start_quest.jpg', 'rb')
        text = f'''Значит ты {hero.name}.. Рад встретить тебя, давно я не видел таких как ты.
Ты должен знать, что у тебя {hero.hp} здоровья и {hero.damage} урона...
Ты готов начать свое испытание?'''
        bot.send_photo(message.chat.id, img, caption=text, reply_markup=keyboard)

    elif message.text == 'Путешествие':
        event = random.randint(1,2)
        if event == 1:
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = 'Путешествие'
            btn2 = 'Меню'
            keyboard.add(btn1, btn2)
            img = open('./photo/next.jpg', 'rb')
            text = 'Ты изучаешь этот новый для тебя мир, никого не встречаешь. Продолжим?'
            bot.send_photo(message.chat.id, img, caption=text, reply_markup=keyboard)
        elif event == 2:
            enemy = Enemy.create_enemy()
            img = open('./photo/enemies.jpg', 'rb')
            text = f'''Ты видишь {enemy.name}, у которого {enemy.hp} жизней и {enemy.damage} урона.
Что ты предпочтешь, отстаться незаметным или вступить в бой?'''
            bot.send_photo(message.chat.id, img, caption=text)
            combat()

    elif message.text == 'Остаться незамеченным':
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = 'Путешествие'
        btn2 = 'Меню'
        keyboard.add(btn1, btn2)
        img = open('./photo/gone_away.jpg', 'rb')
        text = 'Ты выбрал жизнь, что может быть ценнее.. Идем дальше?'
        bot.send_photo(message.chat.id, img, caption=text, reply_markup=keyboard)

    elif message.text == 'Вступить в бой':
        enemy.hp -= hero.damage
        if enemy.hp <= 0:
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = 'Путешествие'
            btn2 = 'Меню'
            keyboard.add(btn1, btn2)
            img = open('./photo/win.jpg', 'rb')
            text = f'Ты нанес сокрушительный удар {hero.name}. Враг повержен! У тебя осталось {hero.hp} здоровья.'
            bot.send_photo(message.chat.id, img, caption=text, reply_markup=keyboard)
        else:
            hero.hp -= enemy.damage
            if hero.hp <= 0:
                keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = 'Меню'
                keyboard.add(btn1)
                img = open('./photo/damage.jpg', 'rb')
                text = f'''Ты нанес хороший удар, равный {hero.damage} урона.
Но враг нанес {enemy.damage} урона, чем убил тебя... Путь окончен..'''
                bot.send_photo(message.chat.id, img, caption=text, reply_markup=keyboard)
            else:
                img = open('./photo/attack.jpg', 'rb')
                text = f'''В атаку.. Ты нанес {hero.damage} урона, в связи с чем у {enemy.name} осталось {enemy.hp} здоровья.
у тебя осталось {hero.hp} здоровья.'''
                bot.send_photo(message.chat.id, img, caption=text)
                combat()

    elif message.text == 'Меню':
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = "/start"
        keyboard.add(btn1)
        bot.send_message(message.chat.id, text='Хочешь ли ты начать с начала?', reply_markup=keyboard)


bot.polling(none_stop=True)
