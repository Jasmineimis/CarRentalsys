import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image


root= Tk()

def nextPage():
    root.destroy()
    import page1

paneMASTER=Frame(root, width=600, height=500, bg='aliceblue')
paneMASTER.pack()
paneMASTER.propagate(0)

panePIC= Frame(paneMASTER,bg='white', width=600, height=250)
panePIC.pack()
path="/Users/Asmi/Documents/car rental/car pics/toyota fortuner.jpeg"
render = ImageTk.PhotoImage(Image.open(path))
img = tk.Label(panePIC,image = render)
img.pack()

Label(paneMASTER,text='CAR  RENTAL  SERVICE',font=('Walkway',45),bg='aliceblue',fg='black').pack()

Button=tk=Button(paneMASTER, text='START YOUR JOURNEY', font=('Amatic',15),
                 width=20, height=2, relief=GROOVE, bg='teal',command=nextPage)
Button.pack()
pane1=Frame(paneMASTER, width=200, height=100, bg='aliceblue')
pane1.pack(side=LEFT)
pane1.propagate(0)
Label(pane1, text='NO \n ADDITIONAL \n CHARGES',font=('Amatic',14),bg='midnightblue',fg='aliceblue',
      relief=RAISED, height=5).pack()
pane2=Frame(paneMASTER, width=200, height=100, bg='aliceblue')
pane2.pack(side=LEFT)
pane2.propagate(0)
Label(pane2, text='GO \n ANYWHERE',font=('Amatic',14), bg='midnightblue',fg='aliceblue',
      relief=RAISED, height=5).pack(anchor=CENTER)
pane3=Frame(paneMASTER, width=200, height=100, bg='aliceblue')
pane3.pack(side=LEFT)
pane3.propagate(0)
Label(pane3, text='DAMAGE \n INSURANCE',font=('Amatic',14), bg='midnightblue',fg='aliceblue',
      relief=RAISED, height=5).pack()
