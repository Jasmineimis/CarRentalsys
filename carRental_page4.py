#Final order confirmation
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
from page1 import CNo,date,pickupad,dropoffad
from page2 import name,cost,VIN,seats,fueltype,cartype,tmision,path
from page3 import Name,Phno,Address,License,DOB

root = Tk()

"""print(4,CNo,date,pickupad,dropoffad)
print(4,name,cost,seats,fueltype,cartype,tmision,VIN)
print(4,Name,Phno,Address,License,DOB)"""


paneMASTER=Frame(root,
                 width=520,
                 height=270,
                 bg='aliceblue')
paneMASTER.pack()
paneMASTER.propagate(0)

Label(paneMASTER,
      text='Your Order:',
      font=('Amatic',30),
      bg='aliceblue').pack()

#Order details
paneDETAILS=Frame(paneMASTER,
                  bg='aliceblue',
                  width=290,
                  height=350)
paneDETAILS.pack(side=LEFT)
paneDETAILS.propagate(0)

datep=date
pickup=pickupad
drop=dropoffad

Label(paneDETAILS,
      text=name,
      font=('Amatic',20),
      bg='aliceblue').pack()

Label(paneDETAILS,
      text=(fueltype,'|',tmision),
      font=('Amatic',14),
      bg='aliceblue').pack()

Label(paneDETAILS,
      text=(datep),
      font=('Amatic',12),
      bg='aliceblue').pack()

Label(paneDETAILS,
      text=(pickup),
      font=('Amatic',12),
      bg='aliceblue').pack()

Label(paneDETAILS,
      text=(drop),
      font=('Amatic',12),
      bg='aliceblue').pack()

Label(paneDETAILS,
      text=('Rs.',cost,'only'),
      font=('Amatic',18),
      bg='aliceblue').pack()

Button= tk.Button(paneDETAILS,
                  text='PLACE YOUR ORDER',
                  font=('Amatic',12),
                  width=20,
                  relief=GROOVE,
                  bg='Teal').pack()

#Car image
panePIC=Frame(paneMASTER,
              bg='aliceblue',
              width=400,
              height=350)
panePIC.pack(side=LEFT)
panePIC.propagate(0)
render = ImageTk.PhotoImage(Image.open(path))
img = tk.Label(panePIC,
               image = render)
img.pack()




root.mainloop()

import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",
                     user="root",
                     passwd="asmi",
                     database="comp_project")
cursor=mycon.cursor()
cursor.execute("INSERT INTO Customer(Name,Phno,CAddress,DOB,License) VALUES('{}','{}','{}','{}','{}')".format(Name,Phno,Address,DOB,License))
mycon.commit()
mycon.close()

import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",
                     user="root",
                     passwd="asmi",
                     database="comp_project")
c=mycon.cursor()
c.execute("INSERT INTO Transactions(CNO,Pickup_location,dropoff_location,AmtPaid,VIN,License,Rent_Date) VALUES({},'{}','{}',{},'{}','{}','{}')".format(CNo,pickupad,dropoffad,cost,VIN,License,date))
mycon.commit()
mycon.close()
