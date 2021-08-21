from tkinter import*

root=Tk()
root.geometry("500x500")
root.resizable(0,0)

def show():
    root.configure(background="red")
def show1():
    root.configure(background="blue")
def show2():
    root.comfigure(background="pink")

b1=Button(root,text="CLICK",font=("Arial",20),command=show,show1,show2)
b1.pack()

root.mainloop()
