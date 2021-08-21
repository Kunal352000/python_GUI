from tkinter import*

root=Tk()
root.geometry("500x500")
root.resizable(0,0)

def show():
    root.configure(background="blue")

b1=Button(root,text="CLICK",font=("Arial",20))
b1.config(command=show)
b1.pack()
