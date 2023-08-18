import turtle


# Создание ручки
pen = turtle.Pen()

# Параметры окна
screen = turtle.Screen()
screen.screensize(500, 500, "white")
screen.title("Рисунки")

# Задаем скорость ручки
pen.speed(150)

# Делаем перо невидимым
pen.hideturtle()

# Рисуем квадрат в верхнем левом углу
pen.up()
pen.goto(-200, 150)
pen.down()
pen.pencolor("green")
pen.pensize(4)
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.left(90)

# Рисуем солнце в верхнем правом углу
pen.up()
pen.goto(200, 100)
pen.down()
pen.pencolor('yellow')
pen.fillcolor('yellow')
pen.begin_fill()
for i in range(36):
    pen.forward(100)
    pen.left(50)
pen.end_fill()

# Рисуем зацикленные круги ("пончик") в нижнем правом углу
pen.up()
pen.goto(250, -150)
pen.down()
pen.pencolor('red')
for i in range(15):
    pen.circle(70)
    pen.left(48)

# Рисуем спираль в нижнем левом углу
pen.up()
pen.goto(-150, -150)
pen.down()
pen.pencolor('blue')
for i in range(100):
    pen.forward(i)
    pen.left(50)

turtle.done()
