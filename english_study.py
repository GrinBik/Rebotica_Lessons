import csv, tkinter, random
from translate import Translator

def next():
    if eng_word:
        lbl['text'] = random.choice(WORDS)
    else:
        word = random.choice(WORDS)
        if word in list(words_dict.keys()):
            lbl['text'] = words_dict[word]
        else:
            lbl['text'] = translator.translate(word)
            words_dict.update({word : lbl['text']})
    lbl.place(x=300, y=200)
    lbl1['text'] = ''
    lbl1.place(x=300, y=300)

def translate():
    global eng_word
    if eng_word:
        if lbl['text'] in list(words_dict.keys()):
            lbl1['text'] = words_dict[lbl['text']]
            lbl1.place(x=300, y=300)
        else:
            lbl1['text'] = translator.translate(lbl['text'])
            lbl1.place(x=300, y=300)
            words_dict.update({lbl['text'] : lbl1['text']})
    else:
        if lbl['text'] in list(words_dict.values()):
            for key, value in words_dict.items():
                if lbl['text'] == value:
                    lbl1['text'] = key
                    lbl1.place(x=300, y=300)
        else:
            lbl1['text'] = translator.translate(lbl['text'])
            lbl1.place(x=300, y=300)
            words_dict.update({lbl1['text'] : lbl['text']})

def save():
    with open('eng_words.txt', 'w', encoding="utf-8") as file:
        for key, value in words_dict.items():
            file.write(f'{key}:{value}\n')

def change():
    global eng_word
    if eng_word:
        eng_word = False
        lbl_lang = tkinter.Label(win, bg='yellow', text='Russian', font=('Arial', 20))
        lbl_lang.place(x=20, y=100)
    else:
        eng_word = True
        lbl_lang = tkinter.Label(win, bg='yellow', text='English', font=('Arial', 20))
        lbl_lang.place(x=20, y=100)

win = tkinter.Tk()
win.geometry('650x500')
win['bg'] = 'grey'

eng_word = True

translator = Translator(from_lang='en', to_lang='ru')

WORDS = []

words_dict = dict()

with open('C:/Users/grego/Documents/English/1000_words.csv') as csv_file:
    data = csv.reader(csv_file, delimiter = ' ', quotechar='|')
    for line in data:
        for elem in line:
            word = elem.strip(',')
            WORDS.append(word)

with open('eng_words.txt', 'r', encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        key, value = (line.strip('\n')).split(':')
        words_dict.update({key : value})

lbl_lang = tkinter.Label(win, bg='yellow', text='English', font=('Arial', 20))
lbl_lang.place(x=20, y=100)

lbl = tkinter.Label(win, bg='grey', text=random.choice(WORDS), font=('Arial', 20))
lbl.place(x=300, y=200)

lbl1 = tkinter.Label(win, bg='grey', text='', font=('Arial', 20))
lbl1.place(x=300, y=300)

btn_next = tkinter.Button(win, bg='brown', text='Далее', font=('Arial', 15), command=next)
btn_next.place(x=20, y=400)

btn_translate = tkinter.Button(win, bg='brown', text='Перевод', font=('Arial', 15), command=translate)
btn_translate.place(x=200, y=400)

btn_save = tkinter.Button(win, bg='brown', text='Сохранить', font=('Arial', 15), command=save)
btn_save.place(x=400, y=400)

btn_change_lang = tkinter.Button(win, bg='brown', text='Сменить язык', font=('Arial', 15), command=change)
btn_change_lang.place(x=20, y=300)

win.mainloop()
