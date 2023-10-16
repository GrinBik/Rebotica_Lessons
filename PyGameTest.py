import pygame


# Загрузка всех вложенных возможностей pygame
pygame.init()

# Размеры окна
WIDTH = 500
HEIGHT = 500

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Кол-во FPS
FPS = 60
clock = pygame.time.Clock()

# Установка параметров экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Test')

# Проверка процесса игры
game_run = True

# Центр круга и шаг при перемещении
pos_x = 80
pos_y = 80
step = 15

# Отрисовка
while game_run:
    # Установка FPS
    clock.tick(FPS)

    # Фон экрана
    screen.fill(WHITE)

    # Отрисовка круга
    pygame.draw.circle(screen, BLACK, (pos_x, pos_y), 60)

    # Проверка всех происходящих событий
    for event in pygame.event.get():

        # Если нажат крестик закрытия окна
        if event.type == pygame.QUIT:
            game_run = False

        # Если событие - это нажатие клавиши
        elif event.type == pygame.KEYDOWN:
            # Нажата стрелка "налево"
            if event.key == pygame.K_LEFT:
                pos_x -= step
            # Нажата стрелка "направо"
            elif event.key == pygame.K_RIGHT:
                pos_x += step
            # Нажата стрелка "вверх"
            elif event.key == pygame.K_UP:
                pos_y -= step
            # Нажата стрелка "вниз"
            elif event.key == pygame.K_DOWN:
                pos_y += step

        # Переворот экрана
        pygame.display.flip()

# Закрытие всех открытых ранее возможностей pygame
pygame.quit()
