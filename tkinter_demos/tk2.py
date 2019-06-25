import tkinter as tk


def say_hi():
    print("你好")


class APP:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack(side=tk.LEFT, padx=10, pady=10)
        self.hi_there = tk.Button(frame, text='打招呼', fg='blue', bg='black', command=say_hi)
        self.hi_there.pack()


root = tk.Tk()
app = APP(root)

root.mainloop()
