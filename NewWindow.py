from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title('Tkinter 5 Hours Coures')
root.iconbitmap('C:\Python Projects\images\miecze.ico')

def open():
    global my_image
    top = Toplevel()
    top.title('Tkinter 5 Hours Coures, TopLevel')
    top.iconbitmap('C:\Python Projects\images\miecze.ico')
    label = Label(top, text="HelloWorld").pack()
    my_image = ImageTk.PhotoImage(Image.open("Obrazy/Picture1.jpg"))
    my_label = Label(top, image=my_image, height=600, width=500).pack()
    btn2 = Button(top,text="Close window", command=top.destroy).pack()



btn= Button(root, text="Open second Window", command=open).pack()






mainloop()