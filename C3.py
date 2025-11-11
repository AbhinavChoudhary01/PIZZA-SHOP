from tkinter import *
x=Tk()
x.geometry("600x600")
x.title("PIZZA CORNER")
r11=StringVar()
a1=IntVar()
a2=IntVar()
a3=IntVar()
a4=IntVar()
a5=IntVar()
amt=IntVar()
g=IntVar()
na=IntVar()
b1=IntVar()
b2=IntVar()
b3=IntVar()
def amount():
    extra=0
    if b1.get()==1:
        extra=extra+20
    if b2.get()==1:
        extra=extra+20
    if b3.get()==1:
        extra=extra+20    
    y=r11.get()

    if y=="PAN":
        z=450
    elif y=="REG":
        z=300
    r=z+extra
    a1.set(r)
    Q=a2.get()
    amt=Q*r
    g=amt*0.05
    na=amt+g
    a3.set(amt)
    a4.set(g)
    a5.set(na)

l1=Label(text="PIZZA CORNER")
l1.grid(row=1,column=2)

l2=Label(text="PIZZA TYPE:-")
l2.grid(row=1,column=5)
r1=Radiobutton(text="PAN",variable=r11,value="PAN")
r2=Radiobutton(text="REGULAR",variable=r11,value="REG")
r1.grid(row=1,column=6)
r2.grid(row=1,column=7)

l3=Label(text="RATE")
l3.grid(row=1,column=1)
e1=Entry(textvariable=a1)
e1.grid(row=1,column=2)

l4=Label(text="QUANTITY")
l4.grid(row=2,column=1)
e2=Entry(textvariable=a2)
e2.grid(row=2,column=2)

l5=Label(text="AMOUNT")
l5.grid(row=3,column=1)
e3=Entry(textvariable=a3)
e3.grid(row=3,column=2)

l6=Label(text="GST @5%")
l6.grid(row=4,column=1)
e4=Entry(textvariable=a4)
e4.grid(row=4,column=2)

l7=Label(text="NET AMOUNT")
l7.grid(row=5,column=1)
e5=Entry(textvariable=a5)
e5.grid(row=5,column=2)


l8=Label(text="TOPPINGS:-  EXTRA COST = 20 ruppes")
l8.grid(row=2,column=6)

c1=Checkbutton(text="cheese",variable=b1)
c1.grid(row=3,column=5)

c2=Checkbutton(text="capsicum",variable=b2)
c2.grid(row=3,column=6)

c3=Checkbutton(text="corn",variable=b3)
c3.grid(row=3,column=7)

b=Button(text="OK",command=amount)
b.grid(row=13,column=6)


x.mainloop()