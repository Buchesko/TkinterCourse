from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Tkinter 5 Hours Coures')
root.iconbitmap('C:\Python Projects\images\miecze.ico')
root.geometry("400x400")

def show():
    myLabel = Label(root,text=var.get()).pack()

var = StringVar()

c = Checkbutton(root, text="Check this box", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()

my_button = Button(root, text="Show Selection", command=show)
my_button.pack()

mainloop()