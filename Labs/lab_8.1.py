from Tkinter import *
def keimeno():
    Label(root, text='ante geia').pack()
root = Tk()
root.wm_geometry("400x300+20+40")
Label(root, text = "Hello world!").pack()
Button(root, text="Done", command=root.destroy).pack()
Button(root, text='the_best', command=keimeno).pack()
root.update()
root.mainloop()
