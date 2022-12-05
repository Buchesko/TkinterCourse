from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('Tkinter 5 Hours Coures')
root.iconbitmap('C:\Python Projects\images\miecze.ico')

# r = IntVar()
# r.set("2")

def clicked(value):
    my_label = Label(root, text=value)
    my_label.pack()


toppings=[
    ("Peperoni","Peperoni"),
    ("Cheese","Cheese"),
    ("Onion","Onion"),
    ]
pizza = StringVar()
pizza.set(" ")

for text, topping in toppings:
    Radiobutton(root,text=text,variable=pizza, value=topping).pack(anchor=W)

# Radiobutton(root,text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root,text="Option 2", variable=r, value=1,command=lambda: clicked(r.get())).pack()

my_label = Label(root,text=pizza.get())
my_label.pack()

my_button = Button(root, text="click me",command=lambda: clicked(pizza.get()))
my_button.pack()
mainloop()