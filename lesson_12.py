import turtle


# Создание ручки
pen = turtle.Pen()

# Параметры окна
screen = turtle.Screen()
screen.screensize(500, 500, "black")
screen.title("Ракушка")

# Задаем скорость ручки
pen.speed(150)

# Делаем перо невидимым
pen.hideturtle()

# Рисуем ракушку
pen.up()
pen.goto(-70, -70)
pen.down()
pen.pencolor('white')
for i in range(85):
    pen.circle(i * 2.7)
    pen.left(4)

turtle.done()
