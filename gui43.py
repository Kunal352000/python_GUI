from tkinter import*

root=Tk()
root.geometry("500x500")
root.resizable(0,0)

b1=Button(root,text="CLICK",font=("Arial=20"))
b1.bind("<Button>",lambda e:root.configure(background="red"))
b1.bind("<ButtonRelease>",lambda e:root.configure(background="black"))

b1.pack()

root.mainloop()
