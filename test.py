from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
root = Tk()
root.title('Tkinter 5 Hours Coures')
root.iconbitmap('C:\Python Projects\images\miecze.ico')
class Habits:

    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.pack()

        self.myButton = Button(master, text="Click me", command=self.clicker)
        self.myButton.pack()

    def clicker(self):
        print("look at you... You click a button")


e = Habits(root)
root.mainloop()