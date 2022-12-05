from tkinter import *
from PIL import ImageTk,Image

# try:
#     import Tkinter as tk
# except:
#     import tkinter as tk
#
# import time
# class Clock():
#     def __init__(self):
#         self.frame1 = tk.Tk()
#         self.label = tk.Label(text="", font=('Helvetica', 48), fg='red')
#         self.label.pack()
#         self.update_clock()
#         self.frame1.mainloop()
#
#     def update_clock(self):
#         now = time.strftime("%H:%M:%S")
#         self.label.configure(text=now)
#         self.frame1.after(1000, self.update_clock)

root = Tk()
root.title('Tkinter 5 Hours Coures')
root.iconbitmap('C:\Python Projects\images\miecze.ico')


# Creating frame obdject
frame1 = LabelFrame(root, text="This is my Frame .. ", padx=5,pady=5)
frame1.pack(padx=10,pady=10)
frame2 = LabelFrame(root, text="Dzisiaj jest", padx=5,pady=5)
frame2.pack(padx=10,pady=10)
frame3 = LabelFrame(root, text="This is my Frame .. ", padx=5,pady=5)
frame2.pack(padx=10,pady=10)
# Pack and grid can be both used with the frame
my_img1 = ImageTk.PhotoImage(Image.open('Obrazy/2.jpg'))

b1 = Button(frame1,text="Habits",padx=40, pady=20)
b2= Button(frame1,text="Budget",padx=40, pady=20)
b3= Button(frame1,text="Dieta",padx=40, pady=20)
b4= Button(frame1,text="Workouts",padx=40, pady=20)
b5= Button(frame1,text="Password",padx=40, pady=20)

my_label = Label(frame2,text="Dzisiaj jest: ")
my_label.grid(row=0, column=0, columnspan=3)
# b6 = Button(frame2,text="Habits",padx=59, pady=20)
# b7= Button(frame2,text="Budget",padx=59, pady=20)
# b8= Button(frame2,text="Dieta",padx=59, pady=20)
# b9= Button(frame2,text="Workouts",padx=50, pady=20)
# b10= Button(frame2,text="Password",padx=55, pady=20)

# label1 = Label(frame2,text="Czas"+ {Clock()})
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0,column=3)
b4.grid(row=1,column=0)
b5.grid(row=1,column=1)

# b6.grid(row=0, column=0)
# b7.grid(row=0, column=1)
# b8.grid(row=0,column=3)
# b9.grid(row=1,column=0)
# b10.grid(row=1,column=1)
# label1.grid(row=3,column=0)
root.mainloop()