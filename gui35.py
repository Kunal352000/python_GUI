from tkinter import*

root=Tk()
root.geometry("700x700")
root.resizable(0,0)

root.bind("<Key-a>",lambda e:root.configure(background="cyan"))
root.bind("<Key-b>",lambda e:root.configure(background="blue"))
root.bind("<Key-c>",lambda e:root.configure(background="pink"))


root.mainloop()
