from tkinter import *
from PIL import Image,ImageTk
divyanshgupta_root=Tk()
divyanshgupta_root.geometry("1255x944")
#photo= PhotoImage(file=".venv/photo.jpg")
#for jpg images
image=Image.open(".venv/photo.jpg")
photo=ImageTk.PhotoImage(image)


dev_label =Label (image=photo)
dev_label.pack()

divyanshgupta_root.mainloop()
