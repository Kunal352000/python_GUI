from tkinter import *
t=Tk()
t.geometry("400x400")
t.resizable(0,0)
def login():
    e1=Entry()
    e1.pack()
    e2=Entry()
    e2.pack()
    b2=Button(text="LogIn")
    b2.pack()

b1=Button(text="Click",command=login)
b1.pack()
t.mainloop()
