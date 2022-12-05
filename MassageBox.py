from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox


root = Tk()
root.title('Tkinter 5 Hours Coures')
root.iconbitmap('C:\Python Projects\images\miecze.ico')
e = Entry(root,width=35,borderwidth=5).pack()
# showinfo, showwarning, showerror, askquestion,askokcancel, askyesno
def popup():
    response = messagebox.showwarning("This is my popup", "hello world")
    Label(root,text=response).pack()
    # if response == 1:
    #     Label(root,text="You click Yes").pack()
    # else:
    #     Label(root,text="You Clicked NO").pack()

Button(root,text="popup", command=popup).pack()

mainloop()