from tkinter import*

root=Tk()
root.geometry("500x500")
root.resizable(0,0)

un=Label(root,text="Enter Name",font=("Arial",20))
un.grid(row=0,column=0)

e1=Entry(root,font=("Arial",20))
e1.grid(row=0,column=1)


un1=Label(root,text="Enter password",font=("Arial",20))
un1.grid(row=1,column=0)

e2=Entry(root,font=("Arial",20))
e2.grid(row=1,column=1)

b1=Button(root,text="CLICK",font=("Arial",20),fg="blue",bg="black")
b1.grid()

root.mainloop()
        
