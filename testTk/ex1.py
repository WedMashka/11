import tkinter as tk

window = tk.Tk() # создаем окно
window.title(' Название окна ')

window.geometry('600x300+200+50') # ширина х высота + от левого края + от верхнего края
window.resizable(True,True) # По умолчанию разрешает растягивать по ширине и восоте.
window.minsize(200,200) #  минимальное значение окна
window.maxsize(600,600) # максимальное значение окна  

photo = tk.PhotoImage(file='j2.png') # прописываем фавикон
window.iconphoto(False, photo) # вставляем фавикон

window.config(bg='#909090')  # установка фона

# виджеты они неоходимы для отображения текстовой информации tk.lable(где располажить виджет, text = 'какой текст отобразить')
# виджет создан но не расположен в окне
lable1 = tk.Label(window, text=' текст виджета',
                  bg='#193300', # фон
                  fg='#909090', # цвет текста
                  font=('Arial', 23, 'italic'), # вид, размер, стиль
                  padx=30, # отступы с краев
                  pady=10, # отступы с верха и низа
                  width=20, # ширина изменяется в колличестве знаков
                  height=5, # высота измеряется в коллличестве  знаков
                  anchor='sw', # позиционирование текста в лейбле значения по первым буквам названия север юг запад восток
                  relief= tk.RAISED, # бордер
                  bd= 4, # толщина бордера
                  justify=tk.CENTER # позиционирование текста

                  )


# кнопки

count = [1]
def sayHellow():
    print('hi')

def addlable():
    count.append(count[len(count)-1] +1)
    lable2 = tk.Label(window, text=f'лейбл номер {count[len(count)-1]}')
    lable2.pack()
    print(f'лейбл номер {count[len(count)-1]}')

btn1 = tk.Button(window, text='Название кнопки', # создали кнопку
                 command=sayHellow, # указывает функцию которая выполнится при нажатии
                 ) #
btn2 = tk.Button(window,text='добавлю лейбл', command=addlable)
btn2.pack()
btn1.pack() # разместили кнопку в окне


lable1.pack() # расположили виджет в окне

window.mainloop() # запускает окно

