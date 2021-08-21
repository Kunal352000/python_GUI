from tkinter import*

root=Tk()
root.geometry("700x700")
root.resizable(0,0)

root.bind("<F1>",lambda e:root.configure(background="red"))
root.bind("<F2>",lambda e:root.configure(background="cyan"))
root.bind("<F3>",lambda e:root>configure(background="blue"))

root.mainloop()
