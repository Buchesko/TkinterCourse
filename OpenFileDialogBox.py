from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
root = Tk()
root.title('Tkinter 5 Hours Coures')
root.iconbitmap('C:\Python Projects\images\miecze.ico')
def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="C:\Python Projects\TkinterCourse 5h\Obrazy", title="Select File", filetypes=(("jpg",".jpg"),("all files", "*.*")))
    my_label = Label(root,text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()


my_btn = Button(root, text="Open File", command=open).pack()
root.mainloop()