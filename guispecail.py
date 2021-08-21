from tkinter import *
t=Tk()
t.geometry("425x350")
def login():
    f2=Frame(bg="#091e42")
    f2.place(x=0,y=0,width=425,height=350)

    u=Label(f2,text="LogIn Page",bg="#091e42",fg="white")
    u.place(x=150,y=10)

    u1=Label(f2,text="Enter Name",bg="#091e42",fg="white")
    u1.place(x=100,y=80)
    e1=Entry(f2,font=("",12))
    e1.place(x=200,y=80,width=120)
    
    u2=Label(f2,text="Enter Pass",bg="#091e42",fg="white")
    u2.place(x=100,y=130)
    e2=Entry(f2,font=("",12),show='*')
    e2.place(x=200,y=130,width=120)

    b3=Button(f2,text="LogIn")
    b3.place(x=150,y=200,width=80,height=40)

    b2=Button(f2,text="<-",command=home)
    b2.place(x=2,y=3)

def regis():
    f3=Frame(bg="#091e42")
    f3.place(x=0,y=0,width=425,height=350)

    u=Label(f3,text="Registration Page",bg="#091e42",fg="white")
    u.place(x=150,y=10)

    u1=Label(f3,text="Enter Name",bg="#091e42",fg="white")
    u1.place(x=100,y=80)
    e1=Entry(f3,font=("",12))
    e1.place(x=200,y=80,width=120)

    
    u2=Label(f3,text="Enter Pass",bg="#091e42",fg="white")
    u2.place(x=100,y=130)
    
    e2=Entry(f3,font=("",12),show='*')
    e2.place(x=200,y=130,width=120)

    
    u3=Label(f3,text="Enter C Pass",bg="#091e42",fg="white")
    u3.place(x=100,y=180)
    e3=Entry(f3,font=("",12),show='*')
    e3.place(x=200,y=180,width=120)

    b3=Button(f3,text="Regis")
    b3.place(x=150,y=250,width=80,height=40)

    b2=Button(f3,text="<-",command=home)
    b2.place(x=2,y=3)

def home():
    f1=Frame(bg="#091e42")
    f1.place(x=0,y=0,width=425,height=350)

    b1=Button(f1,text="LogIn",command=login)
    b1.place(x=100,y=50,width=80,height=40)

    
    b2=Button(f1,text="Regis",command=regis)
    b2.place(x=200,y=50,width=80,height=40)

home()
t.mainloop()
