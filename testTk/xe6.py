import tkinter as TK


def startWin():
    print(1)
    win = TK.Tk()
    win.title('test close')
    win.geometry('300x200+100+200')
    lable1 = TK.Label(win, text='examle', background='green')
    lable1.place(x=50, y=20)
    print(2)
    kk = win.title()
    print(kk)
    win.mainloop()
    print(3)

startWin()

