from tkinter import*

root=Tk()
root.geometry("500x500")
root.resizable(0,0)

show1=lambda e:root.configure(background="green")
show2=lambda e:root.configure(background="red")
show3=lambda e:root.configure(background="blue")

b1=Button(root,text="CLICK",font=("Arial",20))
b1.bind("<Enter>",show1)
b1.bind("<Leave>",show2)

b1.pack()

root.mainloop()
