from tkinter import*

root=Tk()
root.geometry("500x600")
root.resizable(0,0)

root.bind("<Control-Up>",lambda e:root.configure(background="red"))
root.bind("<Control-Down>",lambda e:root.configure(background="blue"))
root.bind("<Control-Left>",lambda e:root.configure(background="cyan"))
root.bind("<Control-Right>",lambda e:root.configure(background="black"))

root.mainloop()
