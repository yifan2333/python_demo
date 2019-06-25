from tkinter import *


root = Tk()
photo = PhotoImage(file='bg.gif')
theLabel = Label(root, text="吴一凡哈哈哈", justify=LEFT, image=photo, compound=CENTER, font=("华康少女字体", 20), fg='white')
theLabel.pack()

mainloop()