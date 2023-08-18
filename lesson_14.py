import tkinter


# Появление рисунка при нажатии кнопки
def create_picture():
    canvas.pack()
    picture_button.destroy()

# Создание стартового окна, названия, фона
window = tkinter.Tk()
window.geometry('800x700')
window.title('Рисунок')
window['bg'] = 'aqua'

# Создание кнопки по нажатию которой будет появляться рисунок
picture_button =  tkinter.Button(window, bg='gold', text='нажми меня :-)', font=('Arial', 10), command=create_picture)
picture_button.place(width=300, height=40, x=250, y=0)

# Создание холста
canvas = tkinter.Canvas(window, bg='aqua', width=800, height=700)

# Рисуем сердце
canvas.create_polygon(100, 300,
                      100, 250,
                      150, 200,
                      200, 200,
                      250, 250,
                      300, 200,
                      350, 200,
                      400, 250,
                      400, 300,
                      250, 450,
                      fill='red', outline='sandybrown', width=5, activefill='tomato')

# Рисуем смайлик
canvas.create_oval(600,500, 780, 680, fill='yellow', outline='gold', width=3, activefill='lime')

# Рисуем глаза смайлика
canvas.create_oval(640,520, 690, 560, fill='darkcyan', outline='yellow', width=3, activefill='yellow')
canvas.create_oval(705,520, 755, 560, fill='darkcyan', outline='yellow', width=3, activefill='yellow')

# Рисуем нос
canvas.create_oval(690, 560, 710, 580, fill='red', outline='yellow', width=3, activefill='lime')

# Рисуем рот
canvas.create_oval(685,600, 715, 650, fill='skyblue', outline='yellow', width=3, activefill='gold')

window.mainloop()
