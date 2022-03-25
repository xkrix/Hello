from tkinter import *

win = Tk()
win.geometry("350x250")
win.title("first program")


def printt():
    print("Hello")


label1 = Label(win, text="Name")
label1.grid(row=0, column=0)

textbox = Entry(win)
textbox.grid(row=0, column=1)

b1 = Button(win, text='Submit', command=printt)
b1.grid(row=2, column=1)

win.mainloop()