from tkinter import *
from tkinter import messagebox
def calc():
    num1=int(text1.get())
    num2=int(text2.get())
    op=x.get()
    if(op==1):
        sum=num1+num2
        oplabel.config(text='Addition:'+str(sum))
    elif(op==2):
        sub=num1-num2
        oplabel.config(text='Subtraction:'+str(sub))
    elif(op==3):
        mult=num1*num2
        oplabel.config(text='Multiplication:'+str(mult))
    elif(op==4):
        div=num1/num2
        oplabel.config(text='Division:'+str(div))
    else:
        messagebox.showerror('Warning',message='Please select correct operator')
        
        
    
    

if(__name__=='__main__'):
    window=Tk()
    window.title("Calculator")
    window.geometry('400x500')
    x=IntVar()
    label1=Label(window,text='Enter number 1:')
    label1.grid(row=1,column=1)
    text1=Entry(window)
    text1.grid(row=1,column=2)
    label2=Label(window,text='Enter number 2:')
    label2.grid(row=2,column=1)
    text2=Entry(window)
    text2.grid(row=2,column=2)
    label3=Label(window,text='Select operator from below:')
    label3.grid(row=3,column=2)
    rd1=Radiobutton(window,text='+',variable=x,value=1)
    rd2=Radiobutton(window,text='-',variable=x,value=2)
    rd3=Radiobutton(window,text='*',variable=x,value=3)
    rd4=Radiobutton(window,text='/',variable=x,value=4)
   
    rd1.grid(row=4,column=1)
    rd2.grid(row=4,column=2)
    rd3.grid(row=4,column=3)
    rd4.grid(row=4,column=4)
    btn=Button(window,text='Answer',command=calc)
    oplabel=Label(window)
    oplabel.grid(row=6,column=2)
    btn.grid(row=5,column=2)
    
    
    window.mainloop()
    