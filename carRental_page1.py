import tkinter as tk

from tkinter import *

root = Tk()


def nextPage():
    dd=w1.get()
    mm=w2.get()
    yy=w3.get()
    global date
    date=dd+"/"+mm+"/"+yy
    global pickupad
    pickupad=T1.get("1.0","end-1c")
    global dropoffad
    dropoffad=T2.get("1.0","end-1c")
    root.destroy()
    import page2


import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",
                     user="root",
                     passwd="asmi",
                     database="comp_project")
c=mycon.cursor()
st="select CNo from Transactions ORDER BY CNo DESC LIMIT 1"
c.execute(st)
Data=c.fetchone()
CNo=Data[0]
mycon.commit()
mycon.close()
CNo=CNo+1


paneMASTER=Frame(root,
                 width=500,
                 height=265,
                 bg='aliceblue')
paneMASTER.pack()
paneMASTER.propagate(0)

Label(paneMASTER,
      text='Booking Details:',
      font=('Walkway',45),
      bg='aliceblue',
      fg='black').pack()

#Travelling from
A= tk.StringVar(paneMASTER)
A.set('Travelling from:')
cities=['Bangalore','Mumbai','Delhi','Kolkata','Chennai']
OptionMenu(paneMASTER,A,*cities).pack()


#Trip details
B= tk.StringVar(paneMASTER)
B.set('Trip details:')
OptionMenu(paneMASTER,B,*['Round trip','One way trip']).pack()



pane1 = Frame(paneMASTER,
              bg='aliceblue')
pane1.pack(anchor=W,
           fill=BOTH)

#DD MM YYYY
Label(pane1,
      text='DD:',
      width=10,
      bg='aliceblue').pack(side=LEFT,fill=BOTH)
Label(pane1,
      text='MM:',
      width=10,
      bg='aliceblue').pack(side=LEFT,fill=BOTH)
Label(pane1,
      text='YYYY:',
      width=14,
      bg='aliceblue').pack(side=LEFT,fill=BOTH)


pane2 = Frame(paneMASTER,
              width=34,
              bg='aliceblue')
pane2.pack(anchor=W,
           fill = BOTH)

#DD MM YYYY Spinboxes
w1=tk.StringVar()
w1 =Spinbox(pane2,
            from_ = '1',
            to = '31',
            width=10)
w1.pack(side=LEFT,fill=BOTH)

w2=tk.StringVar()
w2 =Spinbox(pane2,
            from_ = '1',
            to = '12',
            width=10)
w2.pack(side=LEFT,fill=BOTH)

w3=tk.StringVar()
w3 =Spinbox(pane2,
            from_ = '2022',
            to = '2030',
            width=14)
w3.pack(side=LEFT,fill=BOTH)



#Pick up
pane3 = Frame(paneMASTER,
              bg="aliceblue")
pane3.pack()

Label(pane3,
      text=' Pick up:',
      font=('amatic',14),
      width=7,
      anchor=W,
      bd=4,
      bg='aliceblue',
      relief=RAISED).pack(side=LEFT)

T1 = Text(pane3,
          height=2,
          width=30,
          bg='lightsteelblue')
T1.pack(side=LEFT)


#Drop
pane4 = Frame(paneMASTER,
              bg="aliceblue")
pane4.pack()


Label(pane4,
      text=' Drop:',
      font=('amatic',14),
      width=7,
      anchor=W,
      bd=4,
      bg='aliceblue',
      relief=RAISED).pack(side=LEFT)

T2 = Text(pane4,
          height=2,
          width=30,
          bg='lightsteelblue')
T2.pack(side=LEFT)



button = tk.Button(paneMASTER,
                   text='FIND CARS',
                   font=('amatic',14),
                   width=25,
                   relief=GROOVE,
                   bg='lightsteelblue',
                   command=nextPage)

button.pack(side=BOTTOM)


root.mainloop()

#Getting values
"""
tfrom=A.get()
print(1,tfrom)

tdetail=B.get()
print(1,tdetail)

print(date)
print(1,pickupad)
print(1,dropoffad)
print(1,CNo)
"""
