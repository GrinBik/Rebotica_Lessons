import pygame as py
import random as rnd


def grid():

    # Вертикальные линии
    py.draw.line(screen, GREEN, (stepX, 0), (stepX, height), thick)
    py.draw.line(screen, GREEN, (2 * stepX, 0), (2 * stepX, height), thick)

    # Горизонтальные линии
    py.draw.line(screen, GREEN, (0, stepY), (width, stepY), thick)
    py.draw.line(screen, GREEN, (0, 2 * stepY), (width, 2 * stepY), thick)


# Отрисовка "крестиков"
def draw_x():
    for i in range(3):
        for j in range(3):
            if field[i][j] == 'x':
                py.draw.line(screen, BRIGHT_TURQUOISE, (j * stepX, i * stepY),
                                                (j * stepX + stepX, i * stepY + stepY), thick)
                py.draw.line(screen, BRIGHT_TURQUOISE, (j * stepX + stepX, i * stepY),
                                                (j * stepX, i * stepY + stepY), thick)


# Отрисовка "ноликов"
def draw_0():
    half_x = int(stepX / 2)
    half_y = int(stepY / 2)
    for i in range(3):
        for j in range(3):
            if field[i][j] == "0":
                py.draw.circle(screen, BLUE, (j * stepX + half_x, i * stepY + half_y), min(half_x, half_y), thick)


# Проверка существования победной линии
def winner(symbol):

    # Здесь будет храниться победная линия
    global winner_line

    # Проверка на победу горизонтальных линий
    for line in field:
        if line.count(symbol) == 3:
            winner_line = [[0, field.index(line)],
                           [1, field.index(line)],
                           [2, field.index(line)]]
            return True

    # Проверка на победу вертикальных линий
    for column in range(3):
        if field[0][column] == field[1][column] == field[2][column] == symbol:
            winner_line = [[column, 0], [column, 1], [column, 2]]
            return True

    # Проверка на победу горизонтали (с лева на право)
    if field[0][0] == field[1][1] == field[2][2] == symbol:
        winner_line = [[0, 0], [1, 1], [2, 2]]
        return True

    # Проверка на победу горизонтали (с права на лево)
    if field[0][2] == field[1][1] == field[2][0] == symbol:
        winner_line = [[0, 2], [1, 1], [2, 0]]
        return True

    # Если дошли до сюда, то победная линия не найдена
    return False


# Вывод надписи на экран
def write_on_screen(text):

    # Вывод победителя
    font = py.font.Font(None, 70)
    message = font.render(text, True, WHITE)
    place = message.get_rect(center=(width / 2, height / 2))
    screen.blit(message, place)

    # Вывод надписи о перезагрузке
    font = py.font.Font(None, 40)
    message = font.render("Нажмите 'R' для перезапуска.", True, WHITE)
    place = message.get_rect(center=(width / 2, height - 100))
    screen.blit(message, place)


# Инициализируем движок pygame
py.init()

# Размеры игрового окна
width = 600
height = 750

# Ширина и высота каждой ячейки поля
stepX = int(width / 3)
stepY = int(height / 3)

# Толщина рисуемых линий линий
thick = 5

# Цвета, используемые в игре
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BRIGHT_TURQUOISE = (0,255,204)

# FPS
fps = 90
clock = py.time.Clock()

# Хранилище значений ячеек игрового поля
field = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

# Победная линия
winner_line = [[], [], []]

# Есть ли пустые ячейки
is_empty_cells = 9

# Процесс игры и конец раунда
game_run = True
game_over = False

# Создаем экран по заданным размерам
screen = py.display.set_mode((width,height))

# Название игрового окна
py.display.set_caption("Крестики - Нолики")

# Отрисовка
while game_run:

    # FPS
    clock.tick(fps)

    # Фон экрана
    screen.fill(BLACK)

    # Отрисовка победной линии
    if game_over:
        py.draw.rect(screen, RED, (winner_line[0][0] * 200, winner_line[0][1] * stepY, stepX, stepY))
        py.draw.rect(screen, RED, (winner_line[1][0] * 200, winner_line[1][1] * stepY, stepX, stepY))
        py.draw.rect(screen, RED, (winner_line[2][0] * 200, winner_line[2][1] * stepY, stepX, stepY))

    # Отрисовка сетки
    grid()

    # Отрисовка "крестиков"
    draw_x()

    # Отрисовка "ноликов"
    draw_0()

    # Поиск победителя
    player_x = winner('x')
    player_0 = winner('0')

    # Вывод соответствующей надписи, если есть победитель
    if player_x:
        game_over = True
        write_on_screen("Победа крестиков!!!")
    elif player_0:
        game_over = True
        write_on_screen("Победа ноликов!!!")
    elif is_empty_cells == 0:
        game_over = True
        write_on_screen("НИЧЬЯ!!!")

    # Анализ событий
    for event in py.event.get():

        # Если нажат крестик в правом верхнем углу, то игра прекращается
        if event.type == py.QUIT:
            game_run = False

        # Пользователь "кликает" в ячейке
        elif event.type == py.MOUSEBUTTONDOWN and not game_over:

            # Узнаем координаты "клика"
            pos = py.mouse.get_pos()

            # Если ячейка пуста, то ставим "крестик"
            if field[pos[1] // stepY][pos[0] // stepX] == '':
                field[pos[1] // stepY][pos[0] // stepX] = 'x'

                # Кол-во свободных ячеек уменьшается на 1
                is_empty_cells -= 1

                # Ход противника
                if is_empty_cells > 1:

                    # Выбор случайной ячейки компьютером
                    x, y = rnd .randint(0, 2), rnd.randint(0, 2)

                    # Поиск свободной ячейки, random мог выбрать занятую ячейку
                    while field[x][y] != '':
                        # Выбор случайной ячейки компьютером
                        x, y = rnd.randint(0, 2), rnd.randint(0, 2)

                    # Ход компьютера
                    field[x][y] = '0'

                    # Кол-во свободных ячеек уменьшается на 1
                    is_empty_cells -= 1

        # Перезапуск игры
        elif event.type == py.KEYDOWN:
            if event.key == py.K_r and game_over:
                field = [['', '', ''],
                         ['', '', ''],
                         ['', '', '']]
                game_over = False
                is_empty_cells = 9

    # Разворот экрана к пользователю
    py.display.flip()

# Конец игры
py.quit()
