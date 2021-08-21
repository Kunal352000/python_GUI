from tkinter import*

root=Tk()
root.geometry("500x500")
root.resizable(0,0)

un=Label(root,text="Enter Name:",font=("Arial",20))
un.grid(row=0,column=0,pady=20,sticky=W)

e1=Entry(root,font=("Arial",20))
e1.grid(row=0,column=1,pady=20)

def show():
    print("JAI SHRI MAHAKAL")

un1=Label(root,text="Enter Password:",font=("Arial",20))
un1.grid(row=1,column=0,pady=20)

e2=Entry(root,show="*",font=("Arial",20))
e2.grid(row=1,column=1,pady=20)

b1=Button(root,text="Login",font=("Arial",22),command=show)
b1.grid(row=2,column=0,columnspan=2)

root.mainloop()
