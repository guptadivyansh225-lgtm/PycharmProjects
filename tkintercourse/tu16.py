from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("355x233")
root.title("Radiobutton tutorial")
def order():
    tmsg.showinfo("order received!",f"We have received your order for{var.get()}.Thanks for ordering")
var = IntVar()
#var.set()
Label(root,text="What would you like to have you sir?",font= "lucida 19 bold",justify= LEFT,padx=14).pack()
radio=Radiobutton(root,text="Dosa",padx=14,variable=var,value=1).pack(anchor="w")
radio=Radiobutton(root,text="Idly",padx=14,variable=var,value=2).pack(anchor="w")
radio=Radiobutton(root,text="paratha",padx=14,variable=var,value=3).pack(anchor="w")
radio=Radiobutton(root,text="Samosa",padx=14,variable=var,value=4).pack(anchor="w")
Button(root,text= "Order Now",command= order).pack()
root.mainloop()