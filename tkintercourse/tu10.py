from tkinter import *
def harry(event):
    print(f"You clicked on the button at {event.x},{event.y}")


geta_root = Tk()
geta_root.title("Events in Tkinter")
geta_root.geometry("644x234")

widget = Button(geta_root,text = 'Click me please')
widget.pack()

widget.bind('<Button-1>', harry)
widget.bind('<Button-1>', harry)
geta_root.mainloop()
