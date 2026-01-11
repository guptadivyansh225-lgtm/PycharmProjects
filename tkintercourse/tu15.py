from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("355x233")
root.title("Slider tutorial")
def getdollar():
    print(f"we have credited {myslider2.get()}dollars to your bamk account")
    tmsg.showinfo("Ammount Credited!",f"WE  have credited {myslider2.get()}dollars to your account")

#myslider = Scale(root,from_=0,to=100)
#myslider.pack()
Label(root,text="How many dollar do you want?").pack()
myslider2 = Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=50)
#myslider2.set(34)
myslider2.pack()

Button(root,text= "Get dollars!",pady=10,command=getdollar).pack()


root.mainloop()