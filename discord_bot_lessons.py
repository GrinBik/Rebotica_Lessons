# Модуль для периодической проверки БД
import asyncio
# Модуль для создания записи текущего времени в БД
import datetime
# Модуль для чтения файла с запрещенными словами
import json
# Модуль для загрузки переменных окружения
import os
# БД
import sqlite3
# Модуль для анализа сообщений пользователя
import string

# Модуль для создания бота Discord
import discord
# Создание команд в Discord
from discord.ext import commands
# Проверка прав пользователя на совершения действия
from discord.ext.commands import has_permissions
# Загрузка переменных окружения
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# COMMON_CHANNEL_ID = int(os.getenv('COMMON_CHANNEL_ID'))

# Временное множество для хранения запрещенных слов
temp_censorship = {'мат'}

# Задаем префикс боту и права
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Переменная для хранения информации о том - регулярная ли проверка БД или нет
CHECK_DB = False


# Реакция бота на запуск:
# Бот подтверждает, что запущен
# Соединение с базой данных
@bot.event
async def on_ready():
    global db, cursor
    print("Бот запущен")
    db = sqlite3.connect('DiscordDB.db')
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users(
                        user_id INT,
                        warnings INT,
                        blocked INT,
                        block_date TEXT
                    )''')
    db.commit()
    if db:
        print('DataBase connected .... OK')


# Команда закрытия базы данных
@bot.command()
@has_permissions(administrator=True)
async def db_stop(ctx):
    db.close()
    print('DataBase disconnected .... OK')


# Тестовая команда
@bot.command()
async def test(ctx):
    await ctx.send(f"Здравствуйте!\nЭто тест!\nТак работает реакция на команды..")


# Бот отправляет в ответ слово, которое идет после команды
@bot.command()
async def second_word(ctx, arg=None):
    if arg is None:
        await ctx.send('Если бы после команды было какое-либо слово, я бы его написал...')
    else:
        await ctx.send(f'Ваше слово - {arg} - которое было после команды')


# Бот отправляет в ответ текст целиком, который идет после команды
@bot.command()
async def send_text(ctx, *, arg=None):
    if arg is None:
        await ctx.send('Если бы после команды было что-нибудь, я бы это написал...')
    else:
        await ctx.send(f'Текст - {arg} - который был после команды')


# Обращение к написавшему команду
@bot.command()
async def send_to_author(ctx, arg=None):
    author = ctx.message.author
    if arg is None:
        await ctx.send(f"{author}, Здравствуйте!")
    else:
        await ctx.send(f"{author.mention}, Здравствуйте!")


# Вывод всех команд
@bot.command()
async def commands(ctx, arg=None):
    author = ctx.message.author
    if arg is None:
        await ctx.send(f"{author.mention}, для вывода всех команд наберите '!commands все'")
    elif arg == "все":
        await ctx.send(f""""
{author.mention}, список существующих команд:
* !db_stop - Команда закрытия базы данных
* !test - Тестовая команда
* !second_word <любое слово> - Бот отправляет в ответ слово, которое идет после команды
* !send_text <любой текст> - Бот отправляет в ответ текст целиком, который идет после команды
* !send_to_author - Обращение к написавшему команду
* !commands все - Вывод всех команд
* !clear_db - Очистка базы данных
* !my_status - Статус текущего пользователя, какие у него права на текущий момент
* !user_status <user> - Статус конкретного пользователя (user), какие у него права на текущий момент
* !write_to_myself - Отправка ЛС пользователю, который написал данную команду
* !write_to_user <useer> - Отправка ЛС пользователю (user)
* !set_mute <user> - При наличии прав, вы можете изменить права пользователю user
* !set_unmute <user> - При наличии прав, вы можете изменить права пользователю user
* !delete_chat <кол-во сообщений к удалению> - Удаление любого кол-ва сообщений в чате
* !admin_delete_chat <кол-во сообщений к удалению> - Удаление сообщений в чате при условии, что у вас есть права
* !default_delete_chat - Удаление заданного кол-ва сообщений в чате 
""")


# Обработка всех сообщений пользователя
@bot.event
async def on_message(message):
    # БД переходит в режим постоянной проверки через определенное время
    global CHECK_DB

    # Если в сообщении пользователя присутствует текст "как дела, бот?", бот ответит ХОРОШО
    if "как дела, бот?" in message.content.lower():
        await message.channel.send('хорошо ))')

    # Проверка на цензуру
    # Читаем все слова из сообщения
    text = {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.content.split(' ')}

    # Проверяем, есть ли пересечение с запрещенными словами
    bad_words = text.intersection(set(json.load(open('censorship.json'))))
    # Если запрещенное слово найдено
    if bad_words != set():
        # Запоминаем id пользователя
        number = message.author.id
        # Проверяем были ли предупреждения
        warnings_count = cursor.execute('''SELECT warnings FROM users
                                            WHERE user_id == ?''', (number,)).fetchone()
        # Если предупреждений не было или не было записей, то создаем
        if warnings_count is None:
            cur_date = str(datetime.datetime.now())
            cursor.execute(f"INSERT INTO users VALUES ({number}, 1, 0, '{cur_date}')")
            db.commit()
            await message.channel.send(f'{message.author.mention}, Ваше ПЕРВОЕ предупреждение за цензуру!')
        # Если предупреждение было, то увеличиваем счетчик
        else:
            cursor.execute(f"UPDATE users SET warnings = warnings + 1 WHERE user_id = {number}")
            warnings_count = warnings_count[0] + 1
            # Записываем все изменения в базе данных
            db.commit()
            # Предупреждаем пользователя
            await message.channel.send(f'{message.author.mention}, Ваше {warnings_count}-е предупреждение за цензуру!')
            # Проверка на кол-во предупреждений
            if warnings_count >= 3:
                # Блокировка пользователя на несколько дней, сменив его 'права'
                cur_date = str(datetime.datetime.now())
                cursor.execute(f"UPDATE users SET blocked = 1, block_date = '{cur_date}' WHERE user_id = {number}")
                # Записываем все изменения в базе данных
                db.commit()
                # Меняем права пользователю
                # Уточняем пользователя
                blocked_member = message.guild.get_member(number)
                # Доступные права
                mute = discord.utils.get(message.guild.roles, name='Mute')
                talk = discord.utils.get(message.guild.roles, name='Talk')
                # Меняем права
                await blocked_member.add_roles(mute)
                await blocked_member.remove_roles(talk)
                # Сообщаем о смене прав пользователю
                await message.channel.send('Вы заблокированы на n-ое время...')

                # Запуск постоянной проверки БД
                if not CHECK_DB:
                    CHECK_DB = True
                    await check_db(message, number, blocked_member)

        # Удаляем сообщение, содержащее запрещенное слово
        await message.delete()

    # Передаем управление дальше
    await bot.process_commands(message)


# Проверка базы данных на предмет изменения прав пользователям
async def check_db(message, user_id, member):
    # Проверяем всю БД
    data = cursor.execute("SELECT * FROM users").fetchall()
    # Проверяем каждую запись
    for line in data:
        # Если нашелся заблокированный пользователь, то проверяем не вышло ли время блокировки
        if line[2] == 1:
            # Текущее время
            cur_date = datetime.datetime.now()
            # Сколько времени прошло с момента блокировки
            time_difference = cur_date - datetime.datetime.strptime(line[3], '%Y-%m-%d %H:%M:%S.%f')
            # if time_difference.days > 3:
            # Если время блокировки достигло ограничений, меняем права пользователю
            if time_difference.seconds > 15:
                # Меняем запись в БД, обнуляем счетчик предупреждений запрещенных слов
                cursor.execute(
                    f"UPDATE users SET warnings = 0, blocked = 0, block_date = '{cur_date}' WHERE user_id = {user_id}")
                db.commit()
                # Какие права доступны
                mute = discord.utils.get(message.guild.roles, name='Mute')
                talk = discord.utils.get(message.guild.roles, name='Talk')
                # Меняем права
                await member.remove_roles(mute)
                await member.add_roles(talk)
                # Сообщаем пользователю о смене прав
                await member.send(f'Вы разблокированы!')
    # Постоянная проверка БД
    await asyncio.sleep(5)
    await check_db(message, user_id, member)


# Очистка всех полей в таблице базы данных
@bot.command()
@has_permissions(administrator=True)
async def clear_db(ctx):
    cursor.execute("DELETE FROM users")
    db.commit()
    await ctx.send(f'{ctx.message.author}, база данных очищена!')


# Статус текущего пользователя, какие у него права на текущий момент
@bot.command()
async def my_status(ctx):
    user_id = ctx.message.author.id
    warnings = cursor.execute(f'SELECT warnings FROM users WHERE user_id = {user_id}').fetchone()
    if warnings is None:
        await ctx.send(f'{ctx.message.author.mention}, у вас нет предупреждений, вы молодец!')
    else:
        await ctx.send(f'{ctx.message.author}, у вас {warnings[0]} предупреждений!')


# Статус конкретного пользователя, какие у него права на текущий момент
@bot.command()
async def user_status(ctx, member: discord.Member):
    warnings = cursor.execute(f'SELECT warnings FROM users WHERE user_id = {member.id}').fetchone()
    if warnings is None:
        await ctx.send(f'{ctx.message.author.mention}, у вас нет предупреждений, вы молодец!')
    else:
        await ctx.send(f'{ctx.message.author.mention}, у вас {warnings[0]} предупреждений!')


# Отправка ЛС пользователю, который написал данную команду
@bot.command()
async def write_to_myself(ctx):
    await ctx.author.send("Hello word!")


# Отправка ЛС пользователю, которого вы указали
@bot.command()
async def write_to_user(ctx, member: discord.Member):
    await member.send(f"{member.name}, привет от {ctx.author.name}")


# При наличии прав, вы можете изменить права пользователю
@bot.command()
@has_permissions(manage_messages=True)
async def set_mute(ctx, member: discord.Member):
    mute = discord.utils.get(member.guild.roles, name='Mute')
    talk = discord.utils.get(member.guild.roles, name='Talk')
    await member.add_roles(mute)
    await member.remove_roles(talk)
    await ctx.send(f'{member.mention}, бан в виде потери речи')
    await member.send(f'Вы заблокированы на сервере {ctx.guild.name} для разговора')


# При наличии прав, вы можете изменить права пользователю
@bot.command()
@has_permissions(manage_messages=True)
async def set_unmute(ctx, member: discord.Member):
    mute = discord.utils.get(member.guild.roles, name='Mute')
    talk = discord.utils.get(member.guild.roles, name='Talk')
    await member.add_roles(talk)
    await member.remove_roles(mute)
    await ctx.send(f'{member.mention}, вы снова в сердце сервера!')
    await member.send(f'Вы разблокированы для разговора!')


# Удаление любого кол-ва сообщений в чате
@bot.command()
async def delete_chat(ctx, amount=1):
    if ctx.message.author.guild_permissions.administrator:
        await ctx.channel.purge(limit=amount)


# Удаление любого кол-ва сообщений в чате при условии, что у вас есть необходимые права
@bot.command()
@has_permissions(administrator=True)
async def admin_delete_chat(ctx, amount=1):
    await ctx.channel.purge(limit=amount)


# Удаление заданного кол-ва сообщений в чате равного limit
@bot.command()
async def default_delete_chat(ctx):
    await ctx.channel.purge(limit=5)
    await ctx.send(f'{ctx.message.author}, привет )))')


# Приветствие пользователя в ЛС при присоединении к серверу
@bot.event
async def on_member_join(member):
    # Приветствие пользователя в общем чате при присоединении к серверу
    for channel in bot.get_guild(member.guild.id).channels:
        if channel.name == 'основной':
            await bot.get_channel(channel.id).send(f'{member.name}, приветствуем тебя на канале!')

    await member.send("Добро пожаловать на наш сервер!")
    user_id = member.id
    check = cursor.execute(f'SELECT check FROM users WHERE user_id = {user_id}').fetchone()
    if check is None:
        cur_date = str(datetime.datetime.now())
        cursor.execute(f"INSERT INTO users VALUES ({user_id}, 0, 0, '{cur_date}')")
        talk = discord.utils.get(member.guild.roles, name='Talk')
        await member.add_roles(talk)
    elif check[2] == 0:
        talk = discord.utils.get(member.guild.roles, name='Talk')
        await member.add_roles(talk)
    elif check[2] == 1:
        mute = discord.utils.get(member.guild.roles, name='Mute')
        await member.add_roles(mute)


# Прощание с пользователем в общем чате при удалении с сервера
@bot.event
async def on_member_remove(member):
    for channel in bot.get_guild(member.guild.id).channels:
        if channel.name == 'основной':
            await bot.get_channel(channel.id).send(f'{member.name}, будем ждать твоего возвращения!')

bot.run(TOKEN)
