from tkinter import *


def callback():
    var.set("吹吧你，我才不信呢")


root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set("您所下载的影片含有未成年人限制内容，\n请满18周岁再点击")
textLabel = Label(root, textvariable=var, justify=LEFT, padx=10)
textLabel.pack(side=LEFT)

photo = PhotoImage(file='18.gif')

imgLabel = Label(frame1, image=photo)
imgLabel.pack(side=RIGHT)

theButton = Button(frame2, text="我已满18周岁", command=callback)
theButton.pack()

frame1.pack(padx=10, pady=10)
frame2.pack(padx=10, pady=10)

mainloop()