from tkinter import *


def finish(win):
    win.destroy()  # ручное закрытие окна и всего приложения
    print("Закрытие приложения")


def tets():
    root = Tk()
    root.geometry("250x200")
    root.title("Hello METANIT.COM")
    root.protocol("WM_DELETE_WINDOW", lambda win = root : finish(root))

    root.mainloop()
def cr():
    win1 = Tk()
    win1.title('win2')
    win1.geometry('300x300+500+200')
    but2 = Text(win1)
    but2.place(x=30, y=50)
    win1.protocol("WM_DELETE_WINDOW", lambda win3=win1: finish(win3))
    win1.mainloop()

win = Tk()
win.geometry('300x300+200+200')
win.title('win1')
but1 = Button(win, text='create new', command=cr)
but1.place(x = 30, y = 50)
win.mainloop()

