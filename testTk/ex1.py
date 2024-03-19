import tkinter as tk

window = tk.Tk() # создаем окно
window.title(' Название окна ')

window.geometry('600x300+200+50') # ширина х высота + от левого края + от верхнего края
window.resizable(True,True) # По умолчанию разрешает растягивать по ширине и восоте.
window.minsize(200,200) #  минимальное значение окна
window.maxsize(600,600) # максимальное значение окна  

photo = tk.PhotoImage(file='j2.png')
window.iconphoto(False, photo)
window.mainloop() # запускает окно

