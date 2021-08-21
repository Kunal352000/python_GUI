from tkinter import*

root=Tk()
root.geometry("600x600")
root.resizable(0,0)

root.bind("<Shift-Up>",lambda e:root.configure(background="blue"))
root.bind("<Shift-Down>",lambda e:root.configure(background="black"))
root.bind("<Shift-Left>",lambda e:root.configure(background="cyan"))
root.bind("<Shift-Right>",lambda e:root.configure(background="red"))

