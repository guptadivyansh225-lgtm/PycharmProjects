from tkinter import *
def getvals():
    print(f"The value of username is {uservalue.get()}")
    print(f"The value of password is{passvalue.get()}")

devash_root= Tk()
devash_root.geometry("655x333")

user= Label(devash_root,text="Username")
password = Label(devash_root,text="Password")
user.grid()
password.grid(row=1)

#Variable classes in tkinter
#BooleanVar,DoubleVar,IntVar,StringVar

uservalue = StringVar()
passvalue = StringVar()

userentry =Entry(devash_root,textvariable=uservalue)
passentry = Entry(devash_root,textvariable=passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(text="Summit",command=getvals).grid()

devash_root.mainloop()

