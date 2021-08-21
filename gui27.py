from tkinter import*

root=Tk()
root.geometry("600x600")
root.resizable(0,0)

show1=lameda e : root.configure(background="red")
show2=lameda e : root.configure(background="green")
show2=lameda e : root.configure(background="cyan")

b1=Button(root,text="CLICK",font=("Arial",20))
b1.bind("<Button-1>",show1)
b1.bind("<Button-2>",show2)
b1.bind("<Button-3>",show3)
b1.pack()

root.mainloop()
