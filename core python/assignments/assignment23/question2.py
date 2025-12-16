from tkinter import *
from tkinter import ttk

rates={
    "USD": 1,
    "INR": 83.2,
    "EUR":0.92,
    "GBP":0.78,
    "JPY":151.5
  
   }
def convert():
    try:
        amt=float(text1.get())
        from_cur=combo_from.get()
        to_cur=combo_to.get()
        
        if from_cur not in rates or to_cur not in rates:
            result.config(text='invalid currency code!')
            return
        usd=amt/rates[from_cur]
        converted=usd*rates[to_cur]
        result.config(text=f"converted amount:{converted: .2f} {to_cur}")
        
    except ValueError:
        result.config(text="enter valid amount")

if(__name__=="__main__"):
    window=Tk()
    window.geometry('300x400')
    f1=Frame(window)
    label1=Label(f1,text="Enter Amount:")
    text1=Entry(f1)
    f1.pack(pady=10)
    label1.pack()
    text1.pack()
      
    f2=Frame(window)
    label2=Label(f2,text="From currency:")
    text2=Entry(f2)
    
    f2.pack(pady=10)
    label2.pack()
    text2.pack()
    combo_from=ttk.Combobox(f2,values=list(rates.keys()),state='readonly')
    combo_from.current(0)
    combo_from.pack()
    f3=Frame(window)
    label3=Label(f3,text="To currency:")
    text3=Entry(f3)
    
    f3.pack(pady=10)
    label3.pack()
    text3.pack()
    combo_to=ttk.Combobox(f3,values=list(rates.keys()),state='readonly')
    combo_to.current(1)
    combo_to.pack()
    
    f4=Frame(window)
    btn=Button(f4,text='convert',command=convert)
    f4.pack(pady=10)
    btn.pack()
    
    result=Label(window,text="")
    result.pack(pady=20)
    



    window.mainloop()


