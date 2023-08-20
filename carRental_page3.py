#Customer information entry
import tkinter as tk
from tkinter import *

root=Tk()
root.geometry("500x310")


def nextPage():
    dd=W1.get()
    mm=W2.get()
    yy=W3.get()
    global DOB
    DOB=dd+"/"+mm+"/"+yy
    global Name
    Name=T1.get("1.0","end-1c")
    global Address
    Address=T2.get("1.0","end-1c")
    global Phno
    Phno=T3.get("1.0","end-1c")
    global License
    License=T5.get("1.0","end-1c")
    root.destroy()
    import page4


pane0=Frame(root,
            bg='aliceblue')
pane0.pack()
Label(pane0,
      text="Customer Info:",
      font=('Amatic',30),
      bg='aliceblue',
      width=500,
      anchor=N).pack(side=TOP)


#Name
pane1= Frame(root,
             bg='aliceblue')
pane1.pack()
Label(pane1,
      text=' Name (as per driver\'s license):',
      font=('Amatic',18),
      bg='aliceblue',
      width=21,
      height=2,anchor=W).pack(side=LEFT)
T1=Text(pane1,
        height=2,
        width=35,
        bg='lightsteelblue')
T1.pack(side=LEFT)


#Address
pane2 = Frame(root,
              bg='aliceblue')
pane2.pack()
Label(pane2,
      text=' Address:',
      font=('Amatic',18),
      bg='aliceblue',
      width=21,
      height=2,
      anchor=W).pack(side=LEFT)
T2 = Text(pane2,
          height=2,
          width=35,
          bg='lightsteelblue')
T2.pack(side=LEFT)

#Phone number
pane3 = Frame(root,
              bg='aliceblue')
pane3.pack()
Label(pane3,
      text=' Phone number:',
      font=('Amatic',18),
      bg='aliceblue',
      width=21,
      height=2,
      anchor=W).pack(side=LEFT)
T3=Text(pane3,
        height=2,
        width=35,
        bg='lightsteelblue')
T3.pack(side=LEFT)


#Date of Birth
pane4 = Frame(root,
              bg='aliceblue')
pane4.pack()
Label(pane4,
      text='Date of Birth:',
      font=('Amatic',18),
      bg='aliceblue',
      width=21,
      height=2,
      anchor=W).pack(side=LEFT)

W1=tk.StringVar()
W1 = Spinbox(pane4,
             from_ = '1',
             to = '31',
             width=5)
W1.pack(side=LEFT)

W2=tk.StringVar()
W2 = Spinbox(pane4,
             from_ = '1',
             to = '12',
             width=5)
W2.pack(side=LEFT)

W3=tk.StringVar()
W3 = Spinbox(pane4,
             from_ = '1975',
             to = '2006',width=7)
W3.pack(side=LEFT)


#License no.
pane5 = Frame(root,
              bg='aliceblue')
pane5.pack()
Label(pane5,
      text=' License No:',
      font=('Amatic',18),
      bg='aliceblue',
      width=21,
      height=2,
      anchor=W).pack(side=LEFT)
T5=Text(pane5,
        height=2,
        width=35,
        bg='lightsteelblue')
T5.pack(side=LEFT)



pane6=Frame(root,
            bg='aliceblue')
pane6.pack()
button=tk.Button(pane6,
                 text='CONTINUE',
                 font=('Amatic',15),
                 width=8,
                 relief=GROOVE,
                 bg='Teal',
                 command=nextPage)
button.pack(anchor=S)



root.mainloop()

"""print(3,Name,Address,Phno,DOB,License)"""
