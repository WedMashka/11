import tkinter as tk
from random import randint

window = tk.Tk()
window.geometry('500x400+400+100')
window.title('Test Entry')
entry = tk.Entry(window,
                 relief=tk.RAISED,
                 bd=4) #создали  поле для ввода
entry.grid(row=0, column=1) # установили его в окне
entryResult = tk.Entry(window)
entryResult.grid(row=2, column=2)

listNAme=['Jonah']
def showName():
    entryResult.delete(0, tk.END)
    val = entry.get()# используется для получения значения поля энтри
    if val:
        entryResult.insert(0, f'you enter name is {val}')
        listNAme.append(val)
    else:
        entryResult.insert(0, f'you dont write name')
    entry.delete(0,'end') # Удаляет содержимое энтри, первый элемент начиная с какого символа, второй по какой

def showRandomName():
    entryResult.delete(0, tk.END)
    indexRand = randint(0, len(listNAme)-1)
    entryResult.insert(0, f'random name is {listNAme[indexRand]}')
    entry.delete(0, 'end')

tk.Label(window, text='name').grid(row=0,column=0)
tk.Button(window,text='выведу введеное имя',command=showName).grid(row=1,column=1)
tk.Button(window,text='выведу рандомное имя',command=showRandomName).grid(row=1,column=2)
window.grid_columnconfigure(0, minsize=200)
window.grid_columnconfigure(1, minsize=100)
window.grid_rowconfigure(0, minsize=50)
window.grid_rowconfigure(1, minsize=50)

tk.mainloop()