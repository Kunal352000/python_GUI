from tkinter import*
from tkinter import ttk
t=Tk()
t.geometry("425x350")

n=ttk.Notebook()
n.place(x=0,y=0,width=425,height=350)

f1=Frame(bg="cyan")
n.add(f1,text="Insert")


f2=Frame(bg="blue")
n.add(f2,text="Search")


f3=Frame(bg="red")
n.add(f3,text="ShowAll")

t.mainloop()
