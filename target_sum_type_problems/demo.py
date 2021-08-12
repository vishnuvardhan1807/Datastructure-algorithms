from tkinter import *
root=Tk()
root.title("Jashuva calculator")
e=Entry(root,width=60,fg="black")
e.grid(row=0,column=0,columnspan=30,padx=30,pady=80)

def buttonclick(numbers):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(numbers))
def clear():
    e.delete(0,END)
def buttonadd():
    firstnum=e.get()
    global fnum
    global math
    math="add"
    fnum=int(firstnum)
    e.delete(0,END)
def equal():
    secondnum=e.get()
    e.delete(0,END)
    if math=="add":
        e.insert(0,fnum+int(secondnum))
    if math=="sub":
        e.insert(0,fnum-int(secondnum))
    if math=="mul":
        e.insert(0,fnum*int(secondnum))
    if math=="div":
        e.insert(0,fnum/int(secondnum))
    if math=="pow":
        e.insert(0,fnum**int(secondnum))

def sub():
    firstnum=e.get()
    global fnum
    global math
    math="sub"
    fnum=int(firstnum)
    e.delete(0,END)
    return
def mul():
    firstnum=e.get()
    global fnum
    global math
    math="mul"
    fnum=int(firstnum)
    e.delete(0,END)
    return
def div():
    firstnum=e.get()
    global fnum
    global math
    math="div"
    fnum=int(firstnum)
    e.delete(0,END)
    return
def pow():
    firstnum=e.get()
    global fnum
    global math
    math="pow"
    fnum=int(firstnum)
    e.delete(0,END)
    return


button1=Button(root,text="1",padx=40,pady=20,command=lambda:buttonclick(1))
button2=Button(root,text="2",padx=40,pady=20,command=lambda:buttonclick(2))
button3=Button(root,text="3",padx=40,pady=20,command=lambda:buttonclick(3))
button4=Button(root,text="4",padx=40,pady=20,command=lambda:buttonclick(4))
button5=Button(root,text="5",padx=40,pady=20,command=lambda:buttonclick(5))
button6=Button(root,text="6",padx=40,pady=20,command=lambda:buttonclick(6))
button7=Button(root,text="7",padx=40,pady=20,command=lambda:buttonclick(7))
button8=Button(root,text="8",padx=40,pady=20,command=lambda:buttonclick(8))
button9=Button(root,text="9",padx=40,pady=20,command=lambda:buttonclick(9))
button0=Button(root,text="0",padx=40,pady=20,command=lambda:buttonclick(0))


buttonadd=Button(root,text="+",padx=40,pady=20,command=buttonadd)
buttonsub=Button(root,text="-",padx=40,pady=20,command=sub)
buttonmul=Button(root,text="*",padx=40,pady=20,command=mul)
buttondiv=Button(root,text="/",padx=40,pady=20,command=div)
buttonequl=Button(root,text="=",padx=40,pady=20,command=equal)
buttonclear=Button(root,text="Clr()",padx=40,pady=20,command=clear)
buttonpow=Button(root,text="pow",padx=40,pady=20,command=pow)
buttonquit=Button(root,text="quit",padx=40,pady=20,command=root.quit)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button0.grid(row=4,column=1)
buttonadd.grid(row=4,column=0)
buttonsub.grid(row=4,column=2)
buttonmul.grid(row=5,column=0)
buttondiv.grid(row=5,column=1)
buttonclear.grid(row=1,column=4)
buttonequl.grid(row=5,column=2)
buttonpow.grid(row=2,column=4)
buttonquit.grid(row=3,column=4)

root.mainloop()
