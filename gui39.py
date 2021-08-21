from tkinter import*

root=Tk()
root.geometry("500x600")
root.resizable(0,0)

root.bind("1",lambda e:root.configure(background="blue"))
root.bind("2",lambda e:root.configure(background="pink"))
root.bind("3",lambda e:root.configure(background="black"))

root.mainloop()
