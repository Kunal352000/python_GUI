from tkinter import*

root=Tk()
root.geometry("500x500")
root.resizable(0,0)

def show():
    print("MAHAKAL")

b1=Button(root,text="CLICK",font=("Arial",20),command=show)
b1.pack()

root.mainloop()
