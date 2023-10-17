import random
import pygame
from os import path

# Инициализация встроенных инструментов font и mixer
pygame.font.init()
pygame.mixer.init()


# Создание еды для змейки
def create_food():
    global food_x, food_y, food_img, food, food_rect
    food_x = random.randrange(0, screen_width - snake_block)
    food_y = random.randrange(0, screen_height - snake_block)
    food = pygame.transform.scale(food_img, (2 * snake_block, 2 * snake_block))
    food.set_colorkey(WHITE)
    food_rect = food.get_rect(x=food_x, y=food_y)


# Функция проверки поедания еды змейкой
def sneak_eat_food(sneak_place_x, sneak_place_y, food_cor_x, food_cor_y):
    if food_cor_x - snake_block <= sneak_place_x <= food_cor_x + snake_block:
        if food_cor_y - snake_block <= sneak_place_y <= food_cor_y + snake_block:
            # Возвращается True, если змейка съела еду
            return True
    else:
        return False


# Вывод текста на игровое поле
def screen_message():
    font = pygame.font.Font(None, 70)
    message = font.render('Вы проиграли!', True, RED)
    place = message.get_rect(center=(screen_width / 2, screen_height / 2 - 100))
    screen.blit(message, place)
    font = pygame.font.Font(None, 70)
    message = font.render(f'Ваш счет составил {score}.', True, RED)
    place = message.get_rect(center=(screen_width / 2, screen_height / 2))
    screen.blit(message, place)
    font = pygame.font.Font(None, 40)
    restart_message = font.render("Нажмите 'R' для перезапуска.", True, RED)
    restart_place = restart_message.get_rect(center=(screen_width / 2, screen_height - 100))
    screen.blit(restart_message, restart_place)


def snake_draw(i, snake_body):
    snake_img = snake_head_img[i]
    snake_head = pygame.transform.scale(snake_img, (snake_block, snake_block))
    snake_head.set_colorkey(WHITE)
    snake_head_rect = snake_head.get_rect(x=snake_body[-1][0], y=snake_body[-1][1])
    screen.blit(snake_head, snake_head_rect)


# Размеры игрового окна
screen_width = 600
screen_height = 750

# Название игрового окна
pygame.display.set_caption("Змейка")

# Создаем экран по заданным размерам
screen = pygame.display.set_mode((screen_width, screen_height))

# Цвета, используемые в игре
GREEN = (0, 102, 51)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BRIGHT_TURQUOISE = (0, 255, 204)

# Параметры FPS и объект clock для реализации
FPS = 60
clock = pygame.time.Clock()

# Контроль процесса и остановки игры
game_run = True

# Сама змейка представляет собой список
snake_body = []

# Координаты появления змейки
x_start = screen_width / 2
y_start = screen_height / 2

# Шаг змейки и размер каждой ячейки змейки
snake_step = 4
snake_block = 20

# В этих переменных обозначается на сколько переместилась змейка по XY
x_sneak_step = 0
y_sneak_step = 0

# Первоначальная длина змейки
sneak_length = 1

# Местоположение еды для змейки
food_x = 0
food_y = 0

# Счет - сколько еды удалось съесть
score = 0

# Проверка game over
game_over = False

# Директория музыки
music_dir = path.join(path.dirname(__file__), 'music')

# Директория изображений
img_dir = path.join(path.dirname(__file__), 'photo')

# Установка фоновой картинки
bg_img = pygame.image.load(path.join(img_dir, 'snake_fon.jpg')).convert()
bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height))
bg_img_rect = bg_img.get_rect()

# Установка фото еды
food_img = pygame.image.load(path.join(img_dir, 'snake_apple.jpg')).convert()
food = ''
food_rect = ''

# Создание случайного местоположения еды для змейки
create_food()

# Включаем музыку для фона
pygame.mixer.music.load(path.join(music_dir, 'snake_fon.mp3'))
pygame.mixer.music.play()
# Установка громкости
pygame.mixer.music.set_volume(0.5)

# Подключение звука для события поедания еды
eating_music = pygame.mixer.Sound(path.join(music_dir, 'snake_eat.ogg'))
# Установка громкости
eating_music.set_volume(0.5)

# Подключение звука для события столкновения со стеной
wall_music = pygame.mixer.Sound(path.join(music_dir, 'snake_wall.wav'))
# Установка громкости
wall_music.set_volume(0.5)

# Картинки головы в 4-е стороны
snake_head_img = [pygame.image.load(path.join(img_dir, "snake_head_up.jpg")).convert(),
                  pygame.image.load(path.join(img_dir, "snake_head_down.jpg")).convert(),
                  pygame.image.load(path.join(img_dir, "snake_head_left.jpg")).convert(),
                  pygame.image.load(path.join(img_dir, "snake_head_right.jpg")).convert()]

snake_body_img = [pygame.image.load(path.join(img_dir, "snake_body_up_down.jpg")).convert(),
                  pygame.image.load(path.join(img_dir, "snake_body_left_right.jpg")).convert()]

# Переменная для контроля правильности отрисовки головы
snake_head_control = 0

# Запуск игры
while game_run:
    # Задаем фон экрана
    screen.fill(GREEN)

    # Установка фоновой картинки
    screen.blit(bg_img, bg_img_rect)

    # Отрисовка игры согласно заданному FPS
    clock.tick(FPS)

    if game_over:

        screen_message()

    elif not game_over:
        # Отрисовка еды для змейки
        # pygame.draw.rect(screen, BLUE, [food_x, food_y, snake_block, snake_block])
        screen.blit(food, food_rect)

        # Добавление нового местоположения головы змейки в тело змейки
        snake_head = [x_start, y_start]
        snake_body.append(snake_head)

        # Контроль на то - голова добавилась из-за еды или перемещения
        # Если из-за перемещения, то удаляем старую голову (самый хвост)
        if len(snake_body) > sneak_length:
            del snake_body[0]

        # snake_draw(snake_head_control, snake_body)
        # Отрисовка змейки, начиная с ее головы
        for elem_body in snake_body[:-1]:
            # pygame.draw.rect(screen, BRIGHT_TURQUOISE, [elem_body[0], elem_body[1], snake_block, snake_block])
            if snake_head_control == 0 or snake_head_control == 1:
                body_img = snake_body_img[0]
            else:
                body_img = snake_body_img[1]
            body = pygame.transform.scale(body_img, (snake_block, snake_block))
            body.set_colorkey(WHITE)
            body_rect = body.get_rect(x=snake_body[-1][0], y=snake_body[-1][1])
            screen.blit(body, (elem_body[0], elem_body[1]))

        snake_draw(snake_head_control, snake_body)

        # Проверяем событие - куда направили змейку
        for event in pygame.event.get():
            # Если нажат крестик в правом верхнем углу, то игра прекращается
            if event.type == pygame.QUIT:
                game_run = False
            # Управление змейкой
            elif event.type == pygame.KEYDOWN:
                # Змейка перемещается налево
                if event.key == pygame.K_LEFT:
                    x_sneak_step = -snake_step
                    y_sneak_step = 0
                    snake_head_control = 2
                # Змейка перемещается направо
                elif event.key == pygame.K_RIGHT:
                    x_sneak_step = snake_step
                    y_sneak_step = 0
                    snake_head_control = 3
                # Змейка перемещается вверх
                elif event.key == pygame.K_UP:
                    x_sneak_step = 0
                    y_sneak_step = -snake_step
                    snake_head_control = 0
                # Змейка перемещается вниз
                elif event.key == pygame.K_DOWN:
                    x_sneak_step = 0
                    y_sneak_step = snake_step
                    snake_head_control = 1

        # Сохраняется новое местоположение змейки
        x_start += x_sneak_step
        y_start += y_sneak_step

        # Проверка не наткнулась ли голова на свое тело
        for elem_body in snake_body[:-1]:
            # Если голова наткнулась на тело, то игра завершается
            if elem_body == snake_head:
                game_over = True

        # Если змейка съедает еду, то создается новая еда и длина змейки увеличивается на 1
        if sneak_eat_food(x_start, y_start, food_x, food_y):
            create_food()
            score += 1
            sneak_length += 2
            eating_music.play()

        # Если голова змейки столкнулась с границей игрового поля, то конец игры
        if x_start >= screen_width or y_start >= screen_height or x_start <= 0 or y_start <= 0:
            wall_music.play()
            game_over = True

    # Проверка на событие закрытия игрового окна
    for event in pygame.event.get():
        # Если нажат крестик в правом верхнем углу, то игра прекращается
        if event.type == pygame.QUIT:
            game_run = False
        # Проверка на перезагрузку игры при проигрыше
        elif event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_r:
                x_start = screen_width / 2
                y_start = screen_height / 2
                x_sneak_step = 0
                y_sneak_step = 0
                sneak_length = 1
                snake_body = []
                create_food()
                score = 0
                game_over = False

    # Разворот экрана к пользователю
    pygame.display.update()
    pygame.display.flip()

# Конец игры
pygame.quit()
