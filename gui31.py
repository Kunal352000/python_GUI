from tkinter import*

root=Tk()
root.geometry("500x500")
root.resizable(0,0)

b1=Button(root,text="CLICK",font=("Arial",20))
b1.bind("<Enter>",lambda e:root.configure(background="red"))
b1.bind("<Leave>",lambda e:root.configure(background="pink"))

b1.pack()
root.mainloop()
