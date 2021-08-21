from tkinter import*

root=Tk()
root.geometry("500x500")
root.resizable(0,0)

root.bind("<Enter>",lambda e:root.configure(background="pink"))
root.bind("<Leave>",lambda e:root.configure(background="cyan"))

root.mainloop()
