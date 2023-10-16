import telebot, os, random
from telebot.types import ReplyKeyboardMarkup
from dotenv import load_dotenv


def create_enemy():
    name = random.choice(enemies)
    hp = random.randint(1, 100)
    damage = random.randint(1, 100)
    return [name, hp, damage]


load_dotenv()
TOKEN = os.getenv('TELEGRAM_RPG_TOKEN')
bot = telebot.TeleBot(TOKEN)

enemies = ['орк', 'Саруман', 'Саурон']
heroes = ['хоббит', 'эльф', 'друид']

HP = 0
DAMAGE = 0
NAME = 'name'
ENEMY = 'enemy'


@bot.message_handler(commands=['start'])
def starting(message):
    text = "Приветствую тебя путник! Назови себя.."
    img = open('./photo/hello.jpg', 'rb')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = 'хоббит'
    btn2 = 'эльф'
    btn3 = 'друид'
    keyboard.add(btn1, btn2, btn3)
    bot.send_photo(message.chat.id, img, caption = text, reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def answer(message):
    global ENEMY, HP, DAMAGE, NAME
    def combat():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = 'Вступить в бой'
        btn2 = 'Остаться незамеченным'
        btn3 = 'Меню'
        keyboard.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text='Твой выбор?', reply_markup=keyboard)
    if message.text == 'хоббит':
        HP = 75
        DAMAGE = 35
        NAME = message.text
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = 'Путешествие'
        btn2 = 'Меню'
        keyboard.add(btn1, btn2)
        img = open('./photo/start_quest.jpg', 'rb')
        text = f'''Значит ты хоббит.. Рад встретить тебя, давно я не видел таких как ты.
Ты должен знать, что у тебя {HP} здоровья и {DAMAGE} урона...
Ты готов начать свое испытание?'''
        bot.send_photo(message.chat.id, img, caption=text, reply_markup=keyboard)
    elif message.text == 'эльф':
            HP = 90
            DAMAGE = 55
            NAME = message.text
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = 'Путешествие'
            btn2 = 'Меню'
            keyboard.add(btn1, btn2)
            img = open('./photo/start_quest.jpg', 'rb')
            text = f'''Значит ты эльф.. Рад встретить тебя, давно я не видел таких как ты.
        Ты должен знать, что у тебя {HP} здоровья и {DAMAGE} урона...
        Ты готов начать свое испытание?'''
            bot.send_photo(message.chat.id, img, caption=text, reply_markup=keyboard)
    elif message.text == 'друид':
            HP = 100
            DAMAGE = 45
            NAME = message.text
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = 'Путешествие'
            btn2 = 'Меню'
            keyboard.add(btn1, btn2)
            img = open('./photo/start_quest.jpg', 'rb')
            text = f'''Значит ты друид.. Рад встретить тебя, давно я не видел таких как ты.
        Ты должен знать, что у тебя {HP} здоровья и {DAMAGE} урона...
        Ты готов начать свое испытание?'''
            bot.send_photo(message.chat.id, img, caption=text, reply_markup=keyboard)
    elif message.text == 'Путешествие':
        event = random.randint(1, 2)
        if event == 1:
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = 'Путешествие'
            btn2 = 'Меню'
            keyboard.add(btn1, btn2)
            img = open('./photo/next.jpg', 'rb')
            text = 'Ты изучаешь этот новый для тебя мир, никого не встречаешь. Продолжим?'
            bot.send_photo(message.chat.id, img, caption=text, reply_markup=keyboard)
        elif event == 2:
            ENEMY = create_enemy()
            img = open('./photo/enemies.jpg', 'rb')
            text = f'''Ты видишь {ENEMY[0]}, у которого {ENEMY[1]} жизней и {ENEMY[2]} урона.
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
        ENEMY[1] -= DAMAGE
        if ENEMY[1] <= 0:
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = 'Путешествие'
            btn2 = 'Меню'
            keyboard.add(btn1, btn2)
            img = open('./photo/win.jpg', 'rb')
            text = f'Ты нанес сокрушительный удар {NAME}. Враг повержен! У тебя осталось {HP} здоровья.'
            bot.send_photo(message.chat.id, img, caption=text, reply_markup=keyboard)
        else:
            HP -= ENEMY[2]
            if HP <= 0:
                keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = 'Меню'
                keyboard.add(btn1)
                img = open('./photo/damage.jpg', 'rb')
                text = f'''Ты нанес хороший удар, равный {DAMAGE} урона.
Но враг нанес {ENEMY[2]} урона, чем убил тебя... Путь окончен..'''
                bot.send_photo(message.chat.id, img, caption=text, reply_markup=keyboard)
            else:
                img = open('./photo/attack.jpg', 'rb')
                text = f'''В атаку.. Ты нанес {DAMAGE} урона, в связи с чем у {ENEMY[0]} осталось {ENEMY[1]} здоровья.
у тебя осталось {HP} здоровья.'''
                bot.send_photo(message.chat.id, img, caption=text)
                combat()
    elif message.text == 'Меню':
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = "/start"
        keyboard.add(btn1)
        bot.send_message(message.chat.id, text='Хочешь ли ты начать с начала?', reply_markup=keyboard)


bot.polling(none_stop=True)
