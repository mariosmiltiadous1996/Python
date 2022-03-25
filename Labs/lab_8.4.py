class ADialog:
 def __init__(self, parent):
     top = self.top = Toplevel(parent)
     Label(top, text="Row Value").pack()
     self.e = Entry(top)
     self.e.pack(padx=15)
     Label(top, text="Column Value").pack()
     self.c=Entry(top)
     self.c.pack(padx=15)
     b = Button(top, text="OK", command=self.ok)
     b.pack(pady=5)
 def ok(self):
     self.x = self.e.get()
     self.y = self.c.get()
     self.top.destroy()
 
from Tkinter import *
from random import *
root = Tk()
root.wm_geometry("400x300+20+40")

root.update()
dial = ADialog(root)
root.wait_window(dial.top)


for x in range(int(dial.x)):
    for y in range(int(dial.y)):
        b=randint(0,123)
        lab=Label(root, text=b,borderwidth=10)
        lab.grid(row=x,column=y)

root.update()
root.mainloop()
