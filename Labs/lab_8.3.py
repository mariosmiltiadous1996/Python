class ADialog:
 def __init__(self, parent):
     top = self.top = Toplevel(parent)
     Label(top, text="Value").pack()
     self.e = Entry(top)
     self.e.pack(padx=15)
     Label(top, text="Name").pack()
     self.c=Entry(top)
     self.c.pack(padx=15)
     b = Button(top, text="OK", command=self.ok)
     b.pack(pady=5)
 def ok(self):
     self.x = self.e.get()
     print "value is", self.x
     self.y = self.c.get()
     print "name is",self.y
     self.top.destroy()

 
from Tkinter import *
root = Tk()
root.wm_geometry("400x300+20+40")
Label(root, text = "Hello world!").pack()
root.update()
dial = ADialog(root)
root.wait_window(dial.top)
message=StringVar()
message.set("Complete the form")
Label(root, textvariable=message).pack(padx=30)

message.set("Form completed")
Label(root, text="Got value "+dial.x).pack()
Label(root, text="Got name "+dial.y).pack()

Button(root, text="Done", command=root.destroy).pack()
root.update()
root.mainloop()
