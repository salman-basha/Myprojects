import tkinter
from tkinter import *
# from PIL import ImageTk, Image
import sqlite3

root = Tk()

root.title("this is my database window")
root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='py1.png'))
root.geometry('400x400')

# Databases

# create a database or connect to one
conn = sqlite3.connect('address of book.db')

# create a cursor
c = conn.cursor()


# create table
c.execute("""CREATE TABLE addresses  (
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zip_code integer
            )""")

# commit changes
conn.commit()

# close connection
conn.close()

root.mainloop()
