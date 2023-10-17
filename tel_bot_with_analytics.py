from telebot import TeleBot
import os
import random as rnd
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('TOKEN2')
bot = TeleBot(TOKEN)

hp = 0
damage = 0
enemies = ['орк', 'Саруман', 'Саурон']
users = set()
total_messages = 0
total_users = 0

enemy = []


def create_enemy():
    name = rnd.choice(enemies)
    hp = rnd.randint(1, 100)
    damage = rnd.randint(1, 100)
    return [name, hp, damage]


def analytics(func: callable):
    def analytics_wrapper(message):
        global users, total_messages, total_users
        total_messages += 1
        if message.chat.id not in users:
            users.add(message.chat.id)
            total_users += 1
        print('Total messages:', total_messages,
              'Total users:', total_users)
        return func(message)
    return analytics_wrapper


@bot.message_handler(commands=['start'])
@analytics
def starting(message):
    text = "Приветствую тебя путник! Назови себя.."
    img = open('hello.jpg', 'rb')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = 'хоббит'
    btn2 = 'эльф'
    btn3 = 'друид'
    keyboard.add(btn1, btn2, btn3)
    bot.send_photo(message.chat.id, img, caption = text, reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
@analytics
def answer(message):
    global hp, damage, enemy
    def combat():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = 'Вступить в бой'
        btn2 = 'Остаться незамеченным'
        btn3 = 'Меню'
        keyboard.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text= 'Твой выбор?', reply_markup=keyboard)
    if message.text == 'хоббит':
        hp += 75
        damage += 35
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = 'Путешествие'
        btn2 = 'Меню'
        keyboard.add(btn1, btn2)
        img = open('start_quest.jpg', 'rb')
        text = f'''Значит ты {message.text}.. Рад встретить тебя, давно я не видел таких как ты.
Ты должен знать, что у тебя {hp} здоровья и {damage} урона...
Ты готов начать свое испытание?'''
        bot.send_photo(message.chat.id, img, caption=text, reply_markup=keyboard)
    elif message.text == 'эльф':
        hp += 90
        damage += 55
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = 'Путешествие'
        btn2 = 'Меню'
        keyboard.add(btn1, btn2)
        img = open('start_quest.jpg', 'rb')
        text = f'''Значит ты {message.text}.. Рад встретить тебя, давно я не видел таких как ты.
    Ты должен знать, что у тебя {hp} здоровья и {damage} урона...
    Ты готов начать свое испытание?'''
        bot.send_photo(message.chat.id, img, caption=text, reply_markup=keyboard)
    elif message.text == 'друид':
        hp += 100
        damage += 45
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = 'Путешествие'
        btn2 = 'Меню'
        keyboard.add(btn1, btn2)
        img = open('start_quest.jpg', 'rb')
        text = f'''Значит ты {message.text}.. Рад встретить тебя, давно я не видел таких как ты.
    Ты должен знать, что у тебя {hp} здоровья и {damage} урона...
    Ты готов начать свое испытание?'''
        bot.send_photo(message.chat.id, img, caption=text, reply_markup=keyboard)
    elif message.text == 'Путешествие':
        event = rnd.randint(1,2)
        if event == 1:
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = 'Путешествие'
            btn2 = 'Меню'
            keyboard.add(btn1, btn2)
            img = open('next.jpg', 'rb')
            text = 'Ты изучаешь этот новый для тебя мир, никого не встречаешь. Продолжим?'
            bot.send_photo(message.chat.id, img, caption=text, reply_markup=keyboard)
        elif event == 2:
            enemy = create_enemy()
            img = open('enemies.jpg', 'rb')
            text = f'''Ты видишь {enemy[0]}, у которого {enemy[1]} жизней и {enemy[2]} урона.
Что ты предпочтешь, отстаться незаметным или вступить в бой?'''
            bot.send_photo(message.chat.id, img, caption=text)
            combat()
    elif message.text == 'Остаться незамеченным':
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = 'Путешествие'
        btn2 = 'Меню'
        keyboard.add(btn1, btn2)
        img = open('gone_away.jpg', 'rb')
        text = 'Ты выбрал жизнь, что может быть ценнее.. Идем дальше?'
        bot.send_photo(message.chat.id, img, caption=text, reply_markup=keyboard)
    elif message.text == 'Вступить в бой':
        enemy[1] -= damage
        if enemy[1] <= 0:
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = 'Путешествие'
            btn2 = 'Меню'
            keyboard.add(btn1, btn2)
            img = open('win.jpg', 'rb')
            text = f'Ты нанес сокрушительный удар {hero.name}. Враг повержен! У тебя осталось {hero.hp} здоровья.'
            bot.send_photo(message.chat.id, img, caption=text, reply_markup=keyboard)
        else:
            hp -= enemy[2]
            if hp <= 0:
                keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = 'Меню'
                keyboard.add(btn1)
                img = open('damage.jpg', 'rb')
                text = f'''Ты нанес хороший удар, равный {damage} урона.
Но враг нанес {enemy[2]} урона, чем убил тебя... Путь окончен..'''
                bot.send_photo(message.chat.id, img, caption=text, reply_markup=keyboard)
            else:
                img = open('attack.jpg', 'rb')
                text = f'''В атаку.. Ты нанес {damage} урона, в связи с чем у {enemy[0]} осталось {enemy[1]} здоровья.
у тебя осталось {hp} здоровья.'''
                bot.send_photo(message.chat.id, img, caption=text)
                combat()
    if message.text == 'Меню':
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = "/start"
        keyboard.add(btn1)
        bot.send_message(message.chat.id, text='Хочешь ли ты начать с начала?', reply_markup=keyboard)

bot.polling(none_stop=True)