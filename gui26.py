from tkinter import*

root=Tk()
root.geometry("600x500")
root.resizable(0,0)

def show(e):
    root.configure(background="blue")

def show2(e):
    root.configure(background="black")

def show3(e):
    root.configure(background="cyan")

b1=Button(root,text="CLICK",font=("Arial",20))
b1.bind("<Button-1>",show)#left
b1.bind("<Button-2>",show2)#wheel
b1.bind("<Button-3>",show3)#right
b1.pack()

root.mainloop()
