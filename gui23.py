from tkinter import*

root=Tk()
root.geometry("600x600")
root.resizable(0,0)

def show():
    root.configure(background="cyan")

b1=Button(root,text="CLICK",font=("Arial",20),command=show)
b1.pack()

root.mainloop
