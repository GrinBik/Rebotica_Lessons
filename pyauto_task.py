import pyautogui
from time import sleep


def click():
    while True:
        sleep(2)
        print(pyautogui.position())


# Отрисовка круга
def draw_circle():

    # Выбирается форма рисования "окружность"
    pyautogui.click(x=667, y=117)
    sleep(1)

    # Перемещение курсора в начальное положение
    pyautogui.moveTo(x=78, y=312)
    sleep(1)

    # Отрисовка круга с зажатым "shift"
    pyautogui.keyDown('shift')
    sleep(1)
    pyautogui.dragTo(x=365, y=515)
    sleep(1)
    pyautogui.keyUp('shift')
    sleep(1)

    # Клик мышки в стороне
    pyautogui.click(x=365, y=515)


# Отрисовка квадрата
def draw_square():

    # Выбирается форма рисования "прямоугольник"
    pyautogui.click(x=700, y=121)
    sleep(1)

    # Перемещение курсора в начальное положение
    pyautogui.moveTo(x=78, y=312)
    sleep(1)

    # Отрисовка квадрата с зажатым "shift"
    pyautogui.keyDown('shift')
    sleep(1)
    pyautogui.dragTo(x=365, y=515)
    sleep(1)
    pyautogui.keyUp('shift')
    sleep(1)

    # Клик мышки в стороне
    pyautogui.click(x=365, y=515)


# Отрисовка треугольника
def draw_triangle():

    # Выбирается форма рисования "треугольник"
    pyautogui.click(x=784, y=122)
    sleep(1)

    # Перемещение курсора в начальное положение
    pyautogui.moveTo(x=78, y=312)
    sleep(1)

    # Отрисовка треугольника
    pyautogui.dragTo(x=325, y=515)
    sleep(1)

    # Клик мышки в стороне
    pyautogui.click(x=365, y=515)


# Отрисовка куба
def draw_cube():

    # Выбирается форма рисования "прямоугольник"
    pyautogui.click(x=700, y=121)
    sleep(1)

    # Перемещение курсора в начальное положение
    pyautogui.moveTo(x=66, y=429)
    sleep(1)

    # Отрисовка квадрата с зажатым "shift"
    pyautogui.keyDown('shift')
    sleep(1)
    pyautogui.dragTo(x=168, y=516)
    sleep(1)
    pyautogui.keyUp('shift')
    sleep(1)
    pyautogui.click(x=265, y=516)
    sleep(1)

    # Выбирается форма рисования "линия"
    pyautogui.click(x=615, y=118)
    sleep(1)

    # Перемещение курсора для создания грани
    pyautogui.moveTo(x=264, y=352)
    sleep(1)

    # Отрисовка грани под углом 45
    pyautogui.keyDown('shift')
    sleep(1)
    pyautogui.dragTo(x=327, y=302)
    sleep(1)
    pyautogui.keyUp('shift')
    sleep(1)

    # Перемещение курсора на саму грань и перемещение самой грани
    pyautogui.moveTo(x=292, y=324)
    sleep(1)
    pyautogui.dragTo(x=182, y=401)
    sleep(1)

    # Перемещение курсора для создания грани
    pyautogui.moveTo(x=264, y=352)
    sleep(1)

    # Отрисовка грани под углом 45
    pyautogui.keyDown('shift')
    sleep(1)
    pyautogui.dragTo(x=327, y=302)
    sleep(1)
    pyautogui.keyUp('shift')
    sleep(1)

    # Перемещение курсора на саму грань и перемещение самой грани
    pyautogui.moveTo(x=292, y=324)
    sleep(1)
    pyautogui.dragTo(x=94, y=401)
    sleep(1)

    # Перемещение курсора для создания грани
    pyautogui.moveTo(x=264, y=352)
    sleep(1)

    # Отрисовка грани под углом 45
    pyautogui.keyDown('shift')
    sleep(1)
    pyautogui.dragTo(x=327, y=302)
    sleep(1)
    pyautogui.keyUp('shift')
    sleep(1)

    # Перемещение курсора на саму грань и перемещение самой грани
    pyautogui.moveTo(x=292, y=324)
    sleep(1)
    pyautogui.dragTo(x=182, y=488)
    sleep(1)

    # Клик мышки в стороне
    pyautogui.click(x=615, y=118)
    sleep(1)

    # Отрисовка горизонтальной задней грани
    pyautogui.moveTo(x=122, y=373)
    sleep(1)
    pyautogui.dragTo(x=210, y=373)
    sleep(1)

    # Клик мышки в стороне
    pyautogui.click(x=615, y=118)
    sleep(1)

    # Отрисовка вертикальной задней грани
    pyautogui.moveTo(x=210, y=373)
    sleep(1)
    pyautogui.dragTo(x=210, y= 461)
    sleep(1)

    # Клик мышки в стороне
    pyautogui.click(x=615, y=118)
    sleep(1)


# Вопрос пользователю, что нарисовать
answer = pyautogui.confirm(text='Выберите фигуру', title='Рисование', buttons=["круг", "квадрат", "треугольник", "куб"])
sleep(1)

# Если ничего не выбрано завершение программы
if answer == None:
    exit()

# Запуск Paint
pyautogui.click(x=621, y=1051)
sleep(1)
pyautogui.write('paint')
sleep(1)
pyautogui.press('enter')
sleep(2)

# Рисуем выбранную фигуру
if answer == "круг":
    draw_circle()
elif answer == "квадрат":
    draw_square()
elif answer == "треугольник":
    draw_triangle()
elif answer == "куб":
    draw_cube()
