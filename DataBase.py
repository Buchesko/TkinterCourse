from tkinter import *
from PIL import ImageTk, Image
import sqlite3
root = Tk()
root.title('Tkinter 5 Hours Coures')
root.iconbitmap('C:\Python Projects\images\miecze.ico')
root.geometry("400x400")
# DataBase

# create a database or connect to one
conn = sqlite3.connect('address_book.db')
# Create cursor
c = conn.cursor()
# Create table
'''
c.execute("""CREATE TABLE addresses (
        first_name text,
        laste_name text,
        adress text,
        city text,
        state text,
        zipcode integer
        )""")
'''
# Commit changes
conn.commit()

# close connection
conn.close()
root.mainloop()