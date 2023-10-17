import tkinter, time, speedtest

test = speedtest.Speedtest()
win = tkinter.Tk()
win['bg'] = 'green'
win.title('Скорость загрузки и отдачи')
win.geometry('500x500')
download_speed = round(test.download() / 1000000)
time.sleep(5)
download = tkinter.Label(win, bg='green', text=f'Download = {download_speed}', font=('Arial', 20))
upload_speed = round(test.upload() / 1000000)
time.sleep(5)
upload = tkinter.Label(win, bg='green', text=f'Upload = {upload_speed}', font=('Arial', 20))
download.place(x=10, y=100)
upload.place(x=10, y=300)
win.mainloop()
