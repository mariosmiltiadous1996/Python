from Tkinter import *
from random import randint

def athr():
    global List1,List2,v1,v2
    List3=[]
    lab=Label(root,text="Array A + Array B")
    lab.pack()

    for i in range(len(List1)):
        List3.append(List1[i]+List2[i])
        z=0
    for i in range(v1):
        frame3=Frame(root)
        frame3.pack()
        for j in range(v2):
            p=List3[z]
            Label(frame3,text=str(p),borderwidth=10).pack(side=RIGHT)
            z=z+1
    return lab,frame3

def diaf():
    global List1,List2,v1,v2
    List3=[]
    lab=Label(root,text="Array A - Array B")
    lab.pack()

    for i in range(len(List1)):
        List3.append(List1[i]-List2[i])
        z=0
    for i in range(v1):
        frame3=Frame(root)
        frame3.pack()
        for j in range(v2):
            p=List3[z]
            Label(frame3,text=str(p),borderwidth=10).pack(side=RIGHT)
            z=z+1

    return lab,frame3


root = Tk()
root.wm_geometry("600x900+20+40")

List1=[]
Label(root,text="Array A").pack()
v1=randint(1,5)
v2=randint(1,5)
#Vazoume tyxaia v1,v2 giati 8elei tyxaies diastaseis
for i in range(v1):
    frame1=Frame(root)
    frame1.pack()
    for j in range(v2):
        p=randint(10,50)
        List1.append(p)
        Label(frame1,text=str(p),borderwidth=10).pack(side=RIGHT)

List2=[]
Label(root,text="Array B").pack()

for i in range(v1):
    frame2=Frame(root)
    frame2.pack()
    for j in range(v2):
        t=randint(10,50)
        List2.append(t)
        Label(frame2,text=str(t),borderwidth=10).pack(side=RIGHT)
Button(root,text="+",command = athr).pack()
Button(root,text="-",command = diaf).pack()

root.update()
Button(root, text="Done", command=root.destroy).pack(side=BOTTOM)
root.update()
root.mainloop()
