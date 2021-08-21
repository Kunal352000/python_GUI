from tkinter import*

root=Tk()
root.geometry("600x600")
root.resizable(0,0)

show1=lameda a:root.configure(background="blue")
show2=lameda a:root.configure(background="cyan")
show3=lameda a:root.configure(backgroubd="black")

b1=Button(root,text="CLICK",font=("Arial",20))
b1.bind("<Double-1>",show1)
b1.bind("<Double-2>",show2)
b1.bind("<Double-3>",show3)
b1.pack()

root.mainloop()


























