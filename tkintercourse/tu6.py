from tkinter import*

devika_root=Tk()
devika_root.geometry("655x333")
frame=Frame(devika_root,borderwidth=6,bg="grey",relief=SUNKEN)
frame.pack(side=LEFT,anchor="nw")
def hello():
    print("hello tkinter Buttons ")

def name():
    print("name is harry")

b1=Button(frame,fg="red",text="print now",command=hello)
b1.pack(side=LEFT,padx=23)

b2=Button(frame,fg="red",text="print now",command=name)
b2.pack(side=LEFT,padx=23)

b3=Button(frame,fg="red",text="print now")
b3.pack(side=LEFT,padx=23)

b4=Button(frame,fg="red",text="print now")
b4.pack(side=LEFT,padx=23)

devika_root.mainloop()