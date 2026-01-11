from tkinter import *
devagupta_root=Tk()
devagupta_root.geometry("655x333")
f1=Frame(bg="grey",borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,fill="y")

f2=Frame(bg="grey",borderwidth=6,relief=SUNKEN)
f2.pack(side=TOP, fill="x")
l=Label(f1,text="project Tkinter-pycharm")
l.pack(pady=142)

l=Label(f2,text="welcome to sublime text",font="Helvetica 16 bold",fg="red",pady=22)
l.pack()
devagupta_root.mainloop()