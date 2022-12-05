from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Tkinter 5 Hours Coures')
root.iconbitmap('C:\Python Projects\images\miecze.ico')
root.geometry("400x400")
# Drop Down Boxes
def show():
    my_label = Label(root, text=var.get()).pack()

options = ["Monday",
           "Tuesday",
           "Wednesday",
           "Thursday",
            "Friday"
           ]

var = StringVar()
var.set("Monday")
drop = OptionMenu(root,var,*options)
drop.pack()
my_button = Button(root, text="Show Selection", command=show).pack()

mainloop()