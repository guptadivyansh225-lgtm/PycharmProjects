from tkinter import*


class GUI(Tk):
    def __init__(self): #jaha par root hua karta tha VAHA Par ab self hota hai
        super().__init__()
        self.geometry("744x377")

    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self,textvar=self.var,relief=SUNKEN,anchor='w')
        self.statusbar.pack(side=BOTTOM,fill=X)
    def click(self):
        print("Button clicked")
    def createbuttom(self,inptext):
        Button(text=inptext,command=self.click).pack()

if __name__ == '__main__':
    window = GUI()
    window.status()
    window.createbuttom("Click me")
    window.mainloop()#jo yaha par root hua karta tha vo ab yaha par window ho gaya