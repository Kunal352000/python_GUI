from tkinter import*

root=Tk()
root.geometry("500x600")
root.resizable(0,0)

root.bind("<Alt-Up>",lambda e:root.configure(background="pink"))
root.bind("<Alt-Down>",lambda e:root.configure(background="blue"))
root.bind("<Alt-Left>",lambda e:root.configure(background="black"))
root.bind("<Alt-Right>",lambda e:root.configure(background="cyan"))
