import tkinter as tk
window = tk.Tk()

entryIn1 = tk.Entry(window)
entryIn1.grid(row=0, column=0)
entryOut2 = tk.Entry(window)
entryOut2.grid(row=0, column=1)


def eventKey(eventKey):
    if eventKey.char.isdigit():
        entryOut2.delete(0, tk.END)
        entryOut2.insert(0,entryIn1.get())
    else:
        entryOut2.delete(0, tk.END)
        entryOut2.insert(0, 'Pleas enter number')

window.bind('<Key>', eventKey)
window.mainloop()


