from tkinter import *
from tkinter import messagebox
score=0
def finalScore():
    messagebox.showinfo('final score',message=f'Your final score is {score}/3')
def answer():
    global score
    val=x.get()
    if(val==2):
        messagebox.showinfo('Result',message='Correct answer')
        score+=1
    else:
        messagebox.showerror('Result',message='Wrong answer')
        
def next():
    window.destroy()
    open_question2()
        
def open_question2():
    
    win2=Tk()
    win2.title("Quiz game")
    win2.geometry('400x500')
    x2=IntVar()
    def answer2():
        global score
        val=x2.get()
        if(val==3):
            messagebox.showinfo('Result',message='Correct answer')
            score+=1
        else:
            messagebox.showerror('Result',message='Wrong answer')
    def next2():
        win2.destroy()
        open_question3()
           
    fram1 = Frame(win2)
    fram2 = Frame(win2)
    fram3 = Frame(win2)
    fram4 = Frame(win2)

    label1 = Label(fram1, text='Who developed Python?')
    rd1 = Radiobutton(fram2, text='James Gosling', variable=x2, value=1)
    rd2 = Radiobutton(fram2, text='Dennis Ritchie', variable=x2, value=2)
    rd3 = Radiobutton(fram2, text='Guido van Rossum', variable=x2, value=3)
    rd4 = Radiobutton(fram2, text='Bjarne Stroustrup', variable=x2, value=4)

    fram1.pack()
    label1.pack()
    fram2.pack()
    rd1.pack(side=LEFT)
    rd2.pack(side=LEFT)
    rd3.pack(side=LEFT)
    rd4.pack(side=LEFT)

    btn1 = Button(fram3, text='Check Answer', command=answer2)
    btn2 = Button(fram4, text='Next', command=next2)
    fram3.pack()
    fram4.pack()
    btn1.pack()
    btn2.pack()

    win2.mainloop()
    
    
def open_question3():
    win3=Tk()
    win3.title("Quiz game")
    win3.geometry('400x500')
    x3=IntVar()
    def answer3():
        global score
        val=x3.get()
        if(val==3):
            messagebox.showinfo('Result',message='Correct answer')
            score+=1
        else:
            messagebox.showerror('Result',message='Wrong answer')
    def next3():
        win3.destroy()

    fram1 = Frame(win3)
    fram2 = Frame(win3)
    fram3 = Frame(win3)
    fram4 = Frame(win3)

    label1 = Label(fram1, text='Python is .... Language')
    rd1 = Radiobutton(fram2, text='Compiled', variable=x3, value=1)
    rd2 = Radiobutton(fram2, text='Compiled and interpreted', variable=x3, value=2)
    rd3 = Radiobutton(fram2, text='Interpreted', variable=x3, value=3)
    rd4 = Radiobutton(fram2, text='None of Above', variable=x3, value=4)

    fram1.pack()
    label1.pack()
    fram2.pack()
    rd1.pack(side=LEFT)
    rd2.pack(side=LEFT)
    rd3.pack(side=LEFT)
    rd4.pack(side=LEFT)

    btn1 = Button(fram3, text='Check Answer', command=answer3)
    btn2 = Button(fram4, text='Next', command=next3)
    fram3.pack()
    fram4.pack()
    btn1.pack()
    btn2.pack()
    btn3=Button(win3,text='Final score',command=finalScore)
    btn3.pack()

   
    win3.mainloop()
    


if(__name__=='__main__'):
    window=Tk()
    window.title("Quiz game")
    window.geometry('400x500')
    x=IntVar()
    fram1=Frame(window)
    fram2=Frame(window)
    fram3=Frame(window)
    fram4=Frame(window)
    
    
    label1=Label(fram1,text='What is the capital of India?')
    rd1=Radiobutton(fram2,text='Mumbai',variable=x,value=1)
    rd2=Radiobutton(fram2,text='Delhi',variable=x,value=2)
    rd3=Radiobutton(fram2,text='Chennai',variable=x,value=3)
    rd4=Radiobutton(fram2,text='Pune',variable=x,value=4)
    fram1.pack()
    label1.pack()
    fram2.pack()
    rd1.pack(side=LEFT)
    rd2.pack(side=LEFT)
    rd3.pack(side=LEFT)
    rd4.pack(side=LEFT)
    
    btn1=Button(fram3,text='Check Answer',command=answer)
    btn2=Button(fram4,text='Next',command=next)
    fram3.pack()
    fram4.pack()
    btn1.pack()
    btn2.pack()
    
    
    
    
    
    window.mainloop()
    
    
