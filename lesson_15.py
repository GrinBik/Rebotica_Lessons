import tkinter


# Перемещение фонаря-рентгена с помощью клавиш
def light_move(event):
    if event.keysym == 'Up':
        canvas.move(light, 0, -5)
    elif event.keysym == 'Down':
        canvas.move(light, 0, 5)
    elif event.keysym == 'Left':
        canvas.move(light, -5, 0)
    elif event.keysym == 'Right':
        canvas.move(light, 5, 0)


# Создание стартового окна, названия, фона
window = tkinter.Tk()
window.title('Посчитай мячи')

# Создание холста
canvas = tkinter.Canvas(window, bg='aqua', width=800, height=700)
canvas.pack()

# Создание фонаря-рентгена
light = canvas.create_oval(20, 20, 120, 120, fill='gold')

# Рисуем корзину
canvas.create_line(550, 530, 550, 690, fill='aqua')
for i in range(8):
    canvas.create_line(550, 550 + (i * 20), 750, 550 + (i * 20), fill='aqua')
canvas.create_line(750, 690, 750, 530, fill='aqua')

# Рисуем мячи в корзине
for j in range(8):
    for i in range(10):
        canvas.create_oval(550 + (i * 20), 530 + (j * 20),
                           570 + (i * 20), 550 + (j * 20),
                           fill='aqua', outline='aqua')

# Привязка нажатия клавиш к перемещению фонаря-рентгена
canvas.bind_all('<Up>', light_move)
canvas.bind_all('<Down>', light_move)
canvas.bind_all('<Left>', light_move)
canvas.bind_all('<Right>', light_move)

window.mainloop()
