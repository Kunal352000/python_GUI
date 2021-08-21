from tkinter import*
from tkinter import ttk
t=Tk()
t.geometry("425x350")

n=ttk.Notebook()
n.place(x=0,y=0,width=425,height=350)

f1=Frame(bg="cyan")
n.add(f1,text="Insert")
b1=Button(f1,text="My insert Page")
b1.place(x=200,y=100)

f2=Frame(bg="blue")
n.add(f2,text="Search")
b2=Button(f1,text="My search Page")
b2.place(x=200,y=100)

f3=Frame(bg="red")
n.add(f1,text="my show All")
b3=Button(f3,text="My insert Page")
b3.place(x=200,y=100)
