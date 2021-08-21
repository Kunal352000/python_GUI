from tkinter import Tk
from tkinter import Entry
t=tk()
t.title("Calculator")
t.geometry("425x280")
t.resizable(0,0)
t.configure(background="black")
e1=Entry(font=("30"),justify="right")
e1.place(x=0,y=0,width=425,height=50)
t.mainloop()
