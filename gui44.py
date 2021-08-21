from tkinter import*

root=Tk()
root.geometry("600x600")
root.resizable(0,0)

b1=Button(root,text="CLICK",font=("Arial",30))
b1.pack()

def show(e):
    root.configure(background="red")

def show1(e):
    root.configure(background="cyan")

b1.bind("<Button>",show)
b1.bind("<ButtonRelease>",show1)

root.mainloop()
