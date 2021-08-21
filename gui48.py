from tkinter import Tk
from tkinter import Entry
from tkinter import Button
t=Tk()
t.title("Calculator")
t.geometry("425x280")
t.resizable(0,0)
t.configure(background ="black")
e1=Entry(font=("",30),justify="right")
e1.place(x=0,y=0,width=425,height=50)
b1=Button(text="7",font=("",25),bg="gray",fg="white")
b1.place(x=5,y=55,width=100,height=50)
t.mainloop()
