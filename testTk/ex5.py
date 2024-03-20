import tkinter as tk
from tkinter import *
def showInfo(el):
    el.insert(0.0, str1)

window = tk.Tk()
window.geometry('400x400+100+100')
window.title('тест 5')
window.grid_columnconfigure(0, minsize=100)
window.grid_columnconfigure(1, minsize=100)
window.grid_columnconfigure(2, minsize=100)
window.grid_rowconfigure(0, minsize=50)
window.grid_rowconfigure(1, minsize=50)
window.grid_rowconfigure(2, minsize=50)
text = tk.Text(width=25, height=5, bg="darkgreen", fg='white') # позволяет вводить многострочный текст
text.grid(row=1, column=1)
str1 = 'text for out'
btn = tk.Button(window, text='button 1', command= lambda : showInfo(text))
btn.grid(row=0, column=1)
window.mainloop()