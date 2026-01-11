from tkinter import *
root = Tk()

width = Label(root,text = 'Width')
height = Label(root,text = 'Height')

width.grid(row = 1,column = 2)
height.grid(row = 2,column = 2)

Widthvalue = StringVar()
Heightvalue = StringVar()

Widthentry = Entry(root,textvariable = Widthvalue)
Heightentry = Entry(root,textvariable =Heightvalue)

Widthentry.grid(row = 1,column=3)
Widthentry.grid(row = 2,column=3)

root.geometry(WidthxHeight')
root.mainloop()

