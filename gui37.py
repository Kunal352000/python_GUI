from tkinter import*

root=Tk()
root.geometry("500x500")
root.resizable(0,0)

root.bind("<a>",lambda e:root.configure(background="red"))
root.bind("<b>",lambda e:root.configure(background="cyan"))
root.bind("<c>",lambda e:root.configure(background="blue"))

root.mainloop()
