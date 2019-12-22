from tkinter import *
from tkinter.font import Font
from functools import partial

import sqlite3
import random
m=Tk()
m.geometry('1920x1080')
m.title('THE GRAVE')
photo=PhotoImage(file="dark.jpeg")
label=Label(m,image=photo)

label1=Label(m,text='THE GRAVE',font=('times',70,'bold')).place(x=550,y=50)
label2=Label(m,text='COMMANDER WE ARE IN A TROUBLE!!',font=('times',20,'bold')).place(x=80,y=250)
label3=Label(m,text='COMMANDER IN YOUR ABSENCE THE SKELETON KING KIDNAPPED OUR PRINCESS..',font=('times',20,'bold')).place(x=80,y=280)
label4=Label(m,text='WELCOME TO THE GAME THE GRAVE COMMANDER!!.',font=('times',20,'bold')).place(x=80,y=310)
label5=Label(m,text='WELCOME TO THE GAME THE GRAVE COMMANDER!!.',font=('times',20,'bold')).place(x=80,y=340)
#screen.blit(background_image,[0,0])
def buttonclick():
    n=Tk()
    n.geometry('1920x1080')
    n.title('RULES')
    label1=Label(n,text='RULES',font=('times',70,'bold')).place(x=550,y=50)
    label1=Label(n,text='There are 3 levels in the game mode namely 1-Mislers 2-Jumblers 3-Mixers',font=('times',20,'bold')).place(x=80,y=250)
    label1=Label(n,text='There are 3 levels in the game mode namely 1-Mislers 2-Jumblers 3-Mixers',font=('times',20,'bold')).place(x=80,y=280)
    label1=Label(n,text='There are 3 levels in the game mode namely 1-Mislers 2-Jumblers 3-Mixers',font=('times',20,'bold')).place(x=80,y=310)
    label1=Label(n,text='There are 3 levels in the game mode namely 1-Mislers 2-Jumblers 3-Mixers',font=('times',20,'bold')).place(x=80,y=340)
    label1=Label(n,text='There are 3 levels in the game mode namely 1-Mislers 2-Jumblers 3-Mixers',font=('times',20,'bold')).place(x=80,y=370)
    label1=Label(n,text='There are 3 levels in the game mode namely 1-Mislers 2-Jumblers 3-Mixers',font=('times',20,'bold')).place(x=80,y=400)
button=Button(m,text='RULES',width=25,command=buttonclick).place(x=80,y=400)
    
def Mode1():
    k=Tk()
    k.geometry('1920x1080')
    e1=StringVar()
    e1=Entry(k)
    e1.place(x=400,y=250)
    e2=StringVar()
    e2=Entry(k)
    e2.place(x=400,y=350)
    e3=StringVar()
    e3=Entry(k)
    e3.place(x=400,y=450)
    e4=StringVar()
    e4=Entry(k)
    e4.place(x=400,y=550)
    e5=StringVar()
    e5=Entry(k)
    e5.place(x=400,y=650)
    label=Label(k,text='THE MISLERS',font=('times',70,'bold')).place(x=550,y=50)
    le=["EARTH","SWORD","APPLE","SCARY","BIRTH","DEATH","CASTLE","LIGHT","MONGER","PLACE"]
    lm=["TREES","ARMOUR","RAINBOW","FRUIT","WATER","VOWEL","PLASTIC","MINER","EASY","HAMMER"]
    lh=["AUTOMOBILES","EDUCATION","EVACUATION","GRAVEYARD","LECTURES","BIRTHDAY","CROSSROAD","PRESSURE","INSTAGRAM"]
    qe=["..RTH","SW.RD",".PPL.","SC.RY","B.RTH","D..TH","C.STL.","L.GHT","M.NG.R","PL.C."]
    qm=["TR..S",".RM..R","R..NB.W","FR..T","W.T.R","V.W.L","PL.ST.C","M.N.R","..SY","H.MM.R"]
    qh=["..T.M.B.L.S",".D.C.T..N",".V.C..T..N","GR.V.Y.RD","L.CT.R.S","B.RTHD.Y","CR.SSR..D","PR.SS.R.",".NST.GR.M"]
    label=Label(k,text='Fill the correct vowel a,e,i,o,u',font=('times',20,'bold')).place(x=80,y=200)
    label=Label(k,text=random.choice(qe),font=('times',20,'bold')).place(x=80,y=250)
    label=Label(k,text=random.choice(qe),font=('times',20,'bold')).place(x=80,y=350)
    label=Label(k,text=random.choice(qm),font=('times',20,'bold')).place(x=80,y=450)
    label=Label(k,text=random.choice(qm),font=('times',20,'bold')).place(x=80,y=550)
    label=Label(k,text=random.choice(qh),font=('times',20,'bold')).place(x=80,y=650)
    pt=partial(Level1,e1,e2,e3,e4,e5,le,lm,lh)
    button=Button(k,text='SUBMIT',width=50,command=pt).place(x=600,y=700)   
def Level1(e1,e2,e3,e4,e5,le,lm,lh):
    
    sol1=e1.get()
    sol2=e2.get()
    sol3=e3.get()
    sol4=e4.get()
    sol5=e5.get()
    c=0
    if(sol1 in le):
        c+=1
    if(sol2 in le):
        c+=1
    if(sol3 in lm):
        c+=1
    if(sol4 in lm):
        c+=1
    if(sol5 in lh):
        c+=1
    if(c==5):
        s=Tk()
def Mode2():
    a=Tk()
def buttonclick2():
    x=Tk()
    x.geometry('1920x1080')
    x.title('PLAY')
    label1=Label(x,text='It consists of two game modes',font=('times',20,'bold')).place(x=80,y=250)
    button=Button(x,text='MODE1',width=50,command=Mode1).place(x=80,y=430)
    
    button=Button(x,text='MODE2',width=50,command=Mode2).place(x=600,y=430)
button=Button(m,text='PLAY',width=25,command=buttonclick2).place(x=80,y=430)
m.mainloop()
