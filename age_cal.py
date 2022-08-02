from tkinter import *
import tkinter as tk
import datetime as dt
from datetime import*

win=tk.Tk()
win.geometry("400x400+120+100")
win.title("age calculator")
win.configure(bg="black")

##create labels
tk.Label(win,text="Name",bg="black",fg="cyan",width=10).place(x=20,y=200)
tk.Label(win,text="Year",bg="black",fg="cyan",width=10).place(x=20,y=230)
tk.Label(win,text="Month",bg="black",fg="cyan",width=10).place(x=20,y=260)
tk.Label(win,text="Day",bg="black",fg="cyan",width=10).place(x=20,y=290)

def age_calculator():

        name=StringVar()
        year=IntVar()
        month=IntVar()
        day=IntVar()

        name=e1.get()
        year=int(e2.get())
        month=int(e3.get())
        day=int(e4.get())


           

        y=dt.datetime.now()
        curernt_year=y.year
        current_month=y.month
        current_day=y.day

        delta=date(curernt_year,current_month,current_day)-date(year,month,day)
        age=delta.days//365
            
        print(f"{name} you are {age} years old.")



global e1,e2,e3,e4

e1=Entry(win,width=30)
e1.place(x=100,y=200)
e2=Entry(win,width=30)
e2.place(x=100,y=230)
e3=Entry(win,width=30)
e3.place(x=100,y=260)
e4=Entry(win,width=30)
e4.place(x=100,y=290)





tk.Button(win,text="submit",bg="cyan",fg="black",activebackground="blue",command=age_calculator,width=10).place(x=140,y=330)


win.mainloop()
