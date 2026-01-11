from tkinter import *
root = Tk()
root.geometry("655x444")
root.title("CodeWithHarry - Title of my GUI")
#root.wm_iconbitmap("1.ico")#widget of icon entry
root.configure(background="Red")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(f"{width}x{height}")
Button (text= "close",command = root.destroy).pack()

root.mainloop()