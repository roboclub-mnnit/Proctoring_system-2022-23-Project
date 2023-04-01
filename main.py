# App File
import time
from Client import GUI as gui
from Detection import data
from tkinter import *
import pdf_generator

gui.window()

win = Tk()

win.minsize(width =1200,height = 600)

canvas2 = Canvas(win,bg='gray82',width=500,height=100)
canvas2.place(x=20,y=20)

lbl1 = Label(canvas2,text = 'Name:')
lbl1.place(x=10,y=10)
lbl2 = Label(canvas2,text = data.name)
lbl2.place(x=40,y=10)

lbl1 = Label(canvas2,text = 'Roll No.:')
lbl1.place(x=10,y=40)
lbl2 = Label(canvas2,text = data.roll)
lbl2.place(x=80,y=40)

canvas3 =Canvas(win,bg='gray82',width=1160,height=440)
canvas3.place(x=20,y=140)


canvas11 =Canvas(canvas3,bg='gray25',width=170,height=50)
canvas11.place(x=20,y=20)

canvas12 =Canvas(canvas3,bg='gray25',width=170,height=50)
canvas12.place(x=20,y=90)

canvas13 =Canvas(canvas3,bg='gray25',width=170,height=50)
canvas13.place(x=20,y=160)

canvas14 =Canvas(canvas3,bg='gray25',width=170,height=50)
canvas14.place(x=20,y=230)

canvas15 =Canvas(canvas3,bg='gray25',width=170,height=50)
canvas15.place(x=20,y=300)

canvas16 =Canvas(canvas3,bg='gray25',width=170,height=50)
canvas16.place(x=20,y=370)

canvas17 =Canvas(canvas3,bg='gray25',width=170,height=50)
canvas17.place(x=210,y=20)

canvas18 =Canvas(canvas3,bg='gray25',width=930,height=50)
canvas18.place(x=210,y= 90)

canvas19 =Canvas(canvas3,bg='gray25',width=930,height=50)
canvas19.place(x=210,y= 160)






if(data.up != 0):
    lbl1 = Label(canvas11,text = 'Suspicious Head Movement \n Up')
    lbl1.place(x=10,y=10)

if(data.Left != 0):
    lbl2 = Label(canvas12,text = 'Suspicious Head Movement \n Left')
    lbl2.place(x=10,y=10)

if(data.Right != 0):
    lbl3 = Label(canvas13,text = 'Suspicious Head Movement \n Right')
    lbl3.place(x=10,y=10)

if(data.down != 0):
    lbl4 = Label(canvas14,text = 'Suspicious Head Movement \n Down')
    lbl4.place(x=10,y=10)

if(data.usermiss != 0):
    lbl5 = Label(canvas15,text = 'User Missing\n')
    lbl5.place(x=10,y=10)

if(data.multi4 != 0):
    lbl6 = Label(canvas16,text = 'Multiple Face\n Detected')
    lbl6.place(x=10,y=10)

if(data.switch != 0):
    lbl7 = Label(canvas17,text = 'Browser Tab \n Switch')
    lbl7.place(x=10,y=10)

if(data.softwares != []):
     lbl8 = Label(canvas18,text = data.softwares)
     lbl8.place(x=10,y=10)

if(data.URL != []):
     lbl9 = Label(canvas19,text = data.URL)
     lbl9.place(x=10,y=10)


pdf_generator.pdf_gen()
print(data.URL)
print(data.softwares)

print(data.res.keys())






win.mainloop()

