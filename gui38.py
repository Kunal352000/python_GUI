from tkinter import*

root=Tk()
root.geometry("600x500")
root.resizable(0,0)

root.bind("1",lambda e:root.configure(background="blue"))
root.bind("2",lambda e:root.configure(background="cyan"))
root.bind("3",lambda e:root.configure(background="red"))

root.mainloop()
