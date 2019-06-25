from tkinter import *


root = Tk()

GIRLS = ["西施", "貂蝉", "王昭君", "杨玉环"]

v = IntVar()

Radiobutton(root, text='One', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='Two', variable=v, value=2).pack(anchor=W)
Radiobutton(root, text='Three', variable=v, value=3).pack(anchor=W)

mainloop()