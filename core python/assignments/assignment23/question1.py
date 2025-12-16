from tkinter import *
from tkinter import messagebox
def login():
    username=text1.get()
    password=text2.get()
    if(username=='admin' and password=='1234'):
        messagebox.showinfo('Login',message='Login successfull')
    else:
        messagebox.showwarning('Warning',message='Invalid credentials')

if(__name__=='__main__'):
    window=Tk()
    window.title("Login system")
    window.geometry('300x400')
    label1=Label(window,text='Enter username:')
    text1=Entry(window)
    text2=Entry(window)
    label2=Label(window,text='Enter password:')
    
    label1.grid(row=1,column=1)
    label2.grid(row=2,column=1)
    text1.grid(row=1,column=2)
    text2.grid(row=2,column=2)
    btn=Button(window,text='Login',command=login)
    btn.grid(row=3,column=2)
    window.mainloop()
    
    