from tkinter import *

root = Tk()
root.geometry("733x566")
root.title("pycharm")

def myfunc():
    print("mai ek bahaut hi natkhat aur shaitan function hu")

#Use these to create a non dropdown menu
#mymenu = menu(root)
#mymenu.add_command(label="file",command="myfunc)
#mymenu.add_command(label="Exit",command=quit)
#root.config(menu= mymenu)

Mainmenu = Menu(root)
m1 = Menu(Mainmenu,tearoff = 0)
m1.add_command(label = "New project",command = myfunc)
m1.add_command(label = "Save Project",command = myfunc)
m1.add_separator()
m1.add_command(label="Save as ", command = myfunc)
m1.add_command(label="Print", command = myfunc)
root.config(menu=Mainmenu)
Mainmenu.add_cascade(label="file",menu= m1)

m2 = Menu(Mainmenu, tearoff =0)
m2.add_command(label = 'Cut',command = myfunc)
m2.add_command(label = "Copy",command=myfunc)
m2.add_separator()

m2.add_command(label="paste",command = myfunc)
m2.add_command(label ="find",command = myfunc)
root.config(menu=Mainmenu)
Mainmenu.add_cascade (label= "Edit",menu=m2)



root.mainloop()