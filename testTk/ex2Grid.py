import tkinter as tk

window = tk.Tk()
window.title('Окно урока номер 2')
btn1 = tk.Button(window, text='button 1')
btn2 = tk.Button(window, text='button 2')
btn3 = tk.Button(window, text='button 3')
btn4 = tk.Button(window, text='button 4')
btn5 = tk.Button(window, text='я растянута на 3 колонки')
btn6 = tk.Button(window, text='растянута на 4ряда')
btn7 = tk.Button(window, text='button 7')

#  Грид позволяет располагать элементы не в порядке добавления, а в виде таблицы
# Т.е. можно использовать ряды и колонки
btn1.grid(row=0, column=0)  # пустые колонки не считаются
btn2.grid(row=0, column=2)
btn3.grid(row=1, column=1)
btn4.grid(row=2, column=0, stick='we')
btn5.grid(row=3, column=0,
          columnspan=3, # объединяет несколько колонок
          stick='we', # растягивает объединеные колонки указываются запад восток север юг
          )

btn6.grid(row=0, column=3,
          rowspan=4, # объединяет несколько колонок
          stick='ns', # растягивает объединеные колонки указываются запад восток север юг
          )
window.grid_columnconfigure(0, minsize=100) # задает мин размер первой колонки
window.grid_rowconfigure(2,minsize=100) # задает мин размер третей строки
window.geometry('500x500+200+200')
window.minsize(500, 400)

window.mainloop()