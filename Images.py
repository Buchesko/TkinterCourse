from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap('C:\Python Projects\images\miecze.ico')


my_img1 = ImageTk.PhotoImage(Image.open('Obrazy/2.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('Obrazy/3.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('Obrazy/4.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('Obrazy/Picture1.jpg'))
# Creating list with items
image_list = (my_img1,my_img2,my_img3,my_img4)
# Status Bar
status = Label(root,text="Image 1 of "+str(len(image_list)), bd=1,relief=SUNKEN, anchor=E)
# Label
my_label = Label(image=my_img1,height=600,width=500)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1],height=600,width=500)
    button_forward = Button(root,text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root,text="<<", command=lambda: back(image_number-1))

    if image_number == len(image_list):
        button_forward=Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    #         Update status bar
    status = Label(root, text="Image" + str(image_number) +"of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)



def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1], height=600, width=500)
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back=Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    # Update status bar
    status = Label(root, text="Image" + str(image_number) +"of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


button_back = Button(root, text="<<",command=back, state = DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda:forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)
status.grid(row=2, column=0, columnspan=3,sticky=W+E)
root.mainloop()

# from tkinter import *
# # from PIL import ImageTk,Image
# # root = Tk()
# # root.title('Learn To Code at Codemy.com')
# # root.iconbitmap('C:\Python Projects\images\miecze.ico')
# #
# #
# # my_img = ImageTk.PhotoImage(Image.open('Obrazy/Picture1.jpg'))
# # my_label = Label(image=my_img)
# # my_label.pack()
# # button_quit = Button(root, text="Exit Program", command=root.quit)
# # button_quit.pack()
# # root.mainloop()