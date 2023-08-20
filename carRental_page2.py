#Pg 2 pt 1
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image

root=Tk()
def nextPage():
    root.destroy()
    import page3

def prevPage():
    root.destroy()
    import page2
    
paneFILTER = Frame(root,bg="aliceblue")
paneFILTER.grid(row=1,column=0)
    
L=Label(paneFILTER,
      text='FILTERS',
      font=('Amatic',18),
      bg='aliceblue',
      fg='black')
L.grid(row=0,column=0)

#Free Kms
w = Label(paneFILTER,
          text='Km package:',
          font=('Amatic',15),
          bg="aliceblue",
          fg="midnightblue")
w.grid(row=0,
       column=0,
       sticky=W)
a = tk.IntVar()
a.set(1)
RadBut = Radiobutton(paneFILTER,
                     text='12',
                     variable=a,
                     value=1,
                     relief=GROOVE,
                     width=12,
                     height=2,
                     bg='lightsteelblue',
                     activebackground='darkturquoise',
                     fg='black')
RadBut.grid(row=1,
            column=0,
            sticky=W)
RadBut = Radiobutton(paneFILTER,
                     text='192',
                     variable=a,
                     value=2,
                     relief=GROOVE,
                     width=12,
                     height=2,
                     bg='lightsteelblue',
                     activebackground='darkturquoise',
                     fg='black')
RadBut.grid(row=1,
            column=1,
            sticky=W)
RadBut = Radiobutton(paneFILTER,
                     text='320',
                     variable=a,
                     value=3,
                     relief=GROOVE,
                     width=12,
                     height=2,
                     bg='lightsteelblue',
                     activebackground='darkturquoise',
                     fg='black')
RadBut.grid(row=1,
            column=2,
            sticky=W)




#Seats
w = Label(paneFILTER,
          text='Seats:',
          font=('Amatic',15),
          bg='aliceblue',
          fg='midnightblue')
w.grid(row=2,
       column=0,
       sticky=W)
b=tk.IntVar()
b.set(1)
RadBut = Radiobutton(paneFILTER,
                     text='7',
                     variable=b,
                     value=1,
                     relief=GROOVE,
                     width=12,
                     height=2,
                     bg='lightsteelblue',
                     activebackground='darkturquoise',
                     fg='black')
RadBut.grid(row=3,
            column=0,
            sticky=W)
RadBut = Radiobutton(paneFILTER,
                     text='4',
                     variable=b,
                     value=2,
                     relief=GROOVE,
                     width=12,
                     height=2,
                     bg='lightsteelblue',
                     activebackground='darkturquoise',
                     fg='black')
RadBut.grid(row=3,
            column=1,
            sticky=W)
RadBut = Radiobutton(paneFILTER,
                     text='5',
                     variable=b,
                     value=3,
                     relief=GROOVE,
                     width=12,
                     height=2,
                     bg='lightsteelblue',
                     activebackground='darkturquoise',
                     fg='black')
RadBut.grid(row=3,
            column=2,
            sticky=W)




#Car type
w = Label(paneFILTER,
          text='Car Type:',
          font=('Amatic',15),
          bg='aliceblue',
          fg='midnightblue')
w.grid(row=4,
       column=0,
       sticky=W)
c=tk.IntVar()
c.set(1)
RadBut = Radiobutton(paneFILTER,
                     text='SUV',
                     variable=c,
                     value=1,
                     relief=GROOVE,
                     width=12,
                     height=2,
                     bg='lightsteelblue',
                     activebackground='darkturquoise',
                     fg='black')
RadBut.grid(row=5,
            column=0,
            sticky=W)
RadBut = Radiobutton(paneFILTER,
                     text='Hatchback',
                     variable=c,
                     value=2,
                     relief=GROOVE,
                     width=12,
                     height=2,
                     bg='lightsteelblue',
                     activebackground='darkturquoise',
                     fg='black')
RadBut.grid(row=5,
            column=1,
            sticky=W)
RadBut = Radiobutton(paneFILTER,
                     text='Sedan',
                     variable=c,
                     value=3,
                     relief=GROOVE,
                     width=12,
                     height=2,
                     bg='lightsteelblue',
                     activebackground='darkturquoise',
                     fg='black')
RadBut.grid(row=5,
            column=2,
            sticky=W)




#Transmission
w = Label(paneFILTER,
          text='Transmission:',
          font=('Amatic',15),
          bg='aliceblue',
          fg='midnightblue')
w.grid(row=6,
       column=0,
       sticky=W)
d=tk.IntVar()
d.set(1)
RadBut = Radiobutton(paneFILTER,
                     text='Manual',
                     variable=d,
                     value=1,
                     relief=GROOVE,
                     width=12,
                     height=2,
                     bg='lightsteelblue',
                     activebackground='darkturquoise',
                     fg='black')
RadBut.grid(row=7,
            column=0,
            sticky=W)
RadBut = Radiobutton(paneFILTER,
                     text='Automatic',
                     variable=d,
                     value=2,
                     relief=GROOVE,
                     width=12,
                     height=2,
                     bg='lightsteelblue',
                     activebackground='darkturquoise',
                     fg='black')
RadBut.grid(row=7,
            column=1,
            sticky=W)




#Delivery
w = Label(paneFILTER,
          text='Delivery:',
          font=('Amatic',15),
          bg='aliceblue',
          fg='midnightblue')
w.grid(row=8,
       column=0,
       sticky=W)
e=tk.IntVar()
e.set(1)
RadBut = Radiobutton(paneFILTER,
                     text='Home Delivery',
                     variable=e,
                     value=1,
                     relief=GROOVE,
                     width=12,
                     height=2,
                     bg='lightsteelblue',
                     activebackground='darkturquoise',
                     fg='black')
RadBut.grid(row=9,
            column=0,
            sticky=W)
RadBut = Radiobutton(paneFILTER,
                     text='Airport',
                     variable=e,
                     value=2,
                     relief=GROOVE,
                     width=12,
                     height=2,
                     bg='lightsteelblue',
                     activebackground='darkturquoise',
                     fg='black')
RadBut.grid(row=9,
            column=1,
            sticky=W)




#Fuel Type
w = Label(paneFILTER,
          text='Fuel Type:',
          font=('Amatic',15),
          bg='aliceblue',
          fg='midnightblue')
w.grid(row=10,
       column=0,
       sticky=W)
f=tk.IntVar()
f.set(1)
RadBut = Radiobutton(paneFILTER,
                     text='Petrol',
                     variable=f,
                     value=1,
                     relief=GROOVE,
                     width=12,
                     height=2,
                     bg='lightsteelblue',
                     activebackground='darkturquoise',
                     fg='black')
RadBut.grid(row=11,
            column=0,
            sticky=W)
RadBut = Radiobutton(paneFILTER,
                     text='Diesel',
                     variable=f,
                     value=2,
                     relief=GROOVE,
                     width=12,
                     height=2,
                     bg='lightsteelblue',
                     activebackground='darkturquoise',
                     fg='black')
RadBut.grid(row=11,
            column=1,
            sticky=W)



    

#Brand
w = Label(paneFILTER,
          text='Brand:',
          font=('Amatic',15),
          bg='aliceblue',
          fg='midnightblue')
w.grid(row=12,
       column=0,
       sticky=W)
g=tk.IntVar()
g.set(6)
RadBut = Radiobutton(paneFILTER,
                     text='Hyundai',
                     variable=g,
                     value=1,
                     relief=GROOVE,
                     width=12,
                     height=2,
                     bg='lightsteelblue',
                     activebackground='darkturquoise',
                     fg='black')
RadBut.grid(row=13,
            column=0,
            sticky=W)
RadBut = Radiobutton(paneFILTER,
                     text='Honda',
                     variable=g,
                     value=2,
                     relief=GROOVE,
                     width=12,
                     height=2,
                     bg='lightsteelblue',
                     activebackground='darkturquoise',
                     fg='black')
RadBut.grid(row=13,column=1,sticky=W)
RadBut = Radiobutton(paneFILTER,
                     text='Maruti',
                     variable=g,
                     value=3,
                     relief=GROOVE,
                     width=12,
                     height=2,
                     bg='lightsteelblue',
                     activebackground='darkturquoise',
                     fg='black')
RadBut.grid(row=13,column=2,sticky=W)
RadBut = Radiobutton(paneFILTER,text='Mahindra',variable=g,value=4,relief=GROOVE,width=12,
                     height=2,bg='lightsteelblue',activebackground='darkturquoise',
                     fg='black')
RadBut.grid(row=14,column=0,sticky=W)
RadBut = Radiobutton(paneFILTER,text='Tata',variable=g,value=5,relief=GROOVE,width=12,
                     height=2,bg='lightsteelblue',activebackground='darkturquoise',
                     fg='black')
RadBut.grid(row=14,column=1,sticky=W)
RadBut = Radiobutton(paneFILTER,text='Toyota',variable=g,value=6,relief=GROOVE,width=12,
                     height=2,bg='lightsteelblue',activebackground='darkturquoise',
                     fg='black')
RadBut.grid(row=14,column=2,sticky=W)



#nextpage button    
Button= tk.Button(paneFILTER,
                  text='SEARCH',
                  font=('Amatic',12),
                  width=10,
                  relief=GROOVE,
                  bg='Teal',
                  command=root.destroy)
Button.grid(row=19,
            column=1)

root.mainloop()

#Getting values from radio buttons    
A=a.get()
if A==1:
    kms=12
elif A==2:
    kms=192
elif A==3:
    kms=320

B=b.get()
if B==1:
    seats=7
elif B==2:
    seats=4
elif B==3:
    seats=5

C=c.get()
if C==1:
    cartype="SUV"
elif C==2:
    cartype="Hatchback"
elif C==3:
    cartype="Sedan"

D=d.get()
if D==1:
    tmision="Manual"
elif D==2:
    tmision="Automatic"

E=e.get()
if E==1:
    delivery="Home Delivery"
elif E==2:
    delivery="Airport"

F=f.get()
if F==1:
    fueltype="Petrol"
elif F==2:
    fueltype="Diesel"

G=g.get()
if G==1:
    brand="Hyundai"
elif G==2:
    brand="Honda"
elif G==3:
    brand="Maruti"
elif G==4:
    brand="Mahindra"
elif G==5:
    brand="Tata"
elif G==6:
    brand="Toyota"


"""print(2,kms,seats,cartype,tmision,delivery,fueltype,brand)"""

import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",
                     user="root",
                     passwd="asmi",
                     database="comp_project")
c=mycon.cursor()
st="SELECT Model,Price,PIC,VIN FROM cars WHERE Seats={} AND Body_Type='{}' AND Tmision='{}' AND Fuel_Type='{}' AND Brand='{}'".format(seats,cartype,tmision,fueltype,brand)
c.execute(st)
data=c.fetchone()

#Sorry no cars available
if data is None:
    root=Tk()
    panemsg= Frame(root,
                   bg='aliceblue')
    panemsg.grid(row=0,
                 column=0)

    button= tk.Button(panemsg,
                      text='OK',
                      font=('Amatic',15),
                      width=15,
                      relief=GROOVE,
                      bg='Teal',
                      command=prevPage)
    button.grid(row=1,column=0)
    Label(panemsg,
          text=("SORRY NO CARS AVAILABLE"),
          font=('Amatic',30),
          bg='aliceblue').grid(row=0,column=0)

    root.mainloop()

global name
name=data[0]

price=data[1]
global cost
cost=price*kms
global path
path=data[2]
global VIN
VIN=data[3]
mycon.commit()
mycon.close()


#Pg 2 pt 2
import tkinter as tk
from tkinter import*
from PIL import ImageTk,Image

root=Tk()

#Displaying available cars
panePIC= Frame(root)
panePIC.grid(row=0,column=1)
render = ImageTk.PhotoImage(Image.open(path))
img = tk.Label(panePIC,image = render)
img.grid(row=0,column=0)


pane1= Frame(panePIC,bg="aliceblue")
pane1.grid(row=0,column=1)
Label(pane1,
      text=(name),
      font=('Amatic',18),
      bg="aliceblue").grid(row=0,column=0)
Label(pane1,
      text=cartype,
      width=10,
      font=('Amatic',14),
      bg="aliceblue").grid(row=1,column=0,sticky=W)
Label(pane1,
      text=tmision,
      width=10,
      font=('Amatic',14),
      bg="aliceblue").grid(row=1,column=1,sticky=W)
Label(pane1,
      text=fueltype,
      width=10,
      font=('Amatic',14),
      bg="aliceblue").grid(row=2,column=0,sticky=W)
Label(pane1,
      text=('Seats:',seats),
      width=10,
      font=('Amatic',14),
      bg="aliceblue").grid(row=2,column=1,sticky=W)
Label(pane1,
      text=('Rs:',cost),
      font=('Amatic',14),
      bg="aliceblue").grid(row=3,column=0)

Button= tk.Button(panePIC,
                  text='BOOK NOW',
                  font=('Amatic',12),
                  width=10,
                  relief=GROOVE,
                  bg='Teal',
                  command=nextPage)
Button.grid(row=1,column=1)

button= tk.Button(panePIC,
                  text='BACK',
                  font=('Amatic',12),
                  width=10,
                  relief=GROOVE,
                  bg='Teal',
                  command=prevPage)
button.grid(row=1,column=0)

root.mainloop()
