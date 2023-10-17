import telebot, os
from dotenv import load_dotenv
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)

keyboard = InlineKeyboardMarkup()
btn1 = InlineKeyboardButton("кнопка 1 👌", callback_data="btn1")
btn2 = InlineKeyboardButton("кнопка 2 🤦", callback_data="btn1")
keyboard.add(btn1, btn2)

keyboard2 = ReplyKeyboardMarkup()
btn3 = KeyboardButton('кнопка 3 🧤')
btn4 = KeyboardButton('кнопка 4 ☘️')
keyboard2.add(btn3, btn4)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Привет ))", reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def test(message):
    if message.text == 'test':
        bot.send_message(message.from_user.id, "и снова привет ))", reply_markup=keyboard2)


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text == "привет":
        link = '[ссылку](https://qna.habr.com/q/741309)'
        bot.send_message(message.chat.id, f'это тест того, как можно вставить {link} в сообщении.', parse_mode='Markdown')


bot.polling(none_stop=True)

