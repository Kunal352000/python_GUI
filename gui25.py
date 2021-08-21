from tkinter import*

root=Tk()
root.geometry("600x600")
root.resizable(0,0)

def show(e):
    root.configure(background="pink")

b1=Button(root,text="CLICK",font=("Arial",20))
b1.bind("<Button>",show)
b1.pack()

root.mainloop()
