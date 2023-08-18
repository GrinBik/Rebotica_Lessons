import random
import tkinter


# Реакция на нажатие "правильной" кнопки
def correct_btn_func():
    correct_button.configure(bg=random.choice(colors))
    message['text'] = 'правильно :-)'

# Реакция на нажатие "неправильной" кнопки
def wrong_btn_func():
    wrong_button_1.configure(bg=random.choice(colors))
    wrong_button_2.configure(bg=random.choice(colors))
    wrong_button_3.configure(bg=random.choice(colors))
    message['text'] = 'неправильно ;)'


# Создание стартового окна, названия, фона
window = tkinter.Tk()
window.geometry('800x700')
window.title('Обманки')
window['bg'] = 'aqua'

# Создание списка цветов
colors = ['silver', 'tan', 'moccasin', 'olivedrab', 'seagreen',
          'darkcyan', 'slategray', 'mediumpurple', 'plum',
          'lightgray', 'coral', 'peachpuff', 'olive', 'skyblue']

# Создание 4-х кнопок
correct_button = tkinter.Button(window, bg='gold', text='нажми меня', font=('Arial', 10), command=correct_btn_func)
correct_button.place(width=200, height=40, x=0, y=660)
wrong_button_1 = tkinter.Button(window, bg='gold', text='нажми меня', font=('Arial', 10), command=wrong_btn_func)
wrong_button_1.place(width=200, height=40, x=600, y=0)
wrong_button_2 = tkinter.Button(window, bg='gold', text='нажми меня', font=('Arial', 10), command=wrong_btn_func)
wrong_button_2.place(width=200, height=40, x=0, y=0)
wrong_button_3 = tkinter.Button(window, bg='gold', text='нажми меня', font=('Arial', 10), command=wrong_btn_func)
wrong_button_3.place(width=200, height=40, x=600, y=660)

# Создание переменной для надписи на экране
message = tkinter.Label(window, bg='aqua', text='', font=('Arial', 30))
message.place(x=225, y=275, width=350, height=150)

window.mainloop()
