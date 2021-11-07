import tkinter
from tkinter import *
# from PIL import ImageTk, Image
import sqlite3

root = Tk()

root.title("this is my database window")
root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='py1.png'))
root.geometry('500x500')

global editor
global f_name_editor
global l_name_editor
global address_editor
global city_editor
global state_editor
global zipcode_editor

# Databases

# create a database or connect to one
conn = sqlite3.connect('address of book.db')

# create a cursor
c = conn.cursor()
# create table
'''
c.execute("""CREATE TABLE addresses  (
           first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zip_code integer
            )""")
'''
# create a update function:
def update():
    global conn, c

    # create a database or connect to one
    conn = sqlite3.connect('address of book.db')
    # create a cursor
    c = conn.cursor()

    record_id = delete_box.get()

    c.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zip_code = :zipcode 
        
        WHERE oid = :oid""",
              {
               'first': f_name_editor.get(),
               'last': l_name_editor.get(),
               'address': address_editor.get(),
               'city': city_editor.get(),
               'state': state_editor.get(),
               'zipcode': zipcode_editor.get(),
               'oid': record_id
               })

    # commit changes
    conn.commit()

    # close connection
    conn.close()

    editor.destroy()

# create a edit function:
def edit():
    global editor
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor
    global conn, c
    global f_name_label
    global l_name_label
    global address_label
    global city_label
    global state_label
    global zipcode_label
    global edit_button
    editor = Tk()
    editor.title("this is editor window")
    editor.iconbitmap("C:\\Users\\ADMIN\\PycharmProjects\\pythonlearning\\GUI\\p1.ico")
    editor.geometry('500x500')

    # create a database or connect to one
    conn = sqlite3.connect('address of book.db')

    # create a cursor
    c = conn.cursor()

    record_id = delete_box.get()
    # Query the database:
    c.execute("SELECT *,oid FROM addresses WHERE oid =" + record_id)
    records = c.fetchall()

# create text boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

# create text box label
    f_name_label = Label(editor, text='First name')
    f_name_label.grid(row=0, column=0, padx=20, pady=(10, 0))
    l_name_label = Label(editor, text='Last name')
    l_name_label.grid(row=1, column=0)
    address_label = Label(editor, text='Address')
    address_label.grid(row=2, column=0)
    city_label = Label(editor, text='City')
    city_label.grid(row=3, column=0)
    state_label = Label(editor, text='State')
    state_label.grid(row=4, column=0)
    zipcode_label = Label(editor, text='Zipcode')
    zipcode_label.grid(row=5, column=0)

    # loop through results:
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    # create save button:
    edit_button = Button(editor, text='Save Record ', command=update)
    edit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)


# create a delete function for database
def delete():
    global conn, c
    # create a database or connect to one
    conn = sqlite3.connect('address of book.db')

    # create a cursor
    c = conn.cursor()

    # delete the Record:
    c.execute("DELETE from addresses WHERE oid= "+delete_box.get())

    # commit changes
    conn.commit()

    # close connection
    conn.close()


# create a submit function for database
def submit():
    global conn, c
    # create a database or connect to one
    conn = sqlite3.connect('address of book.db')

# create a cursor
    c = conn.cursor()


# insert into tables
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {'f_name': f_name.get(),
               'l_name': l_name.get(),
               'address': address.get(),
               'city': city.get(),
               'state': state.get(),
               'zipcode': zipcode.get()})

# commit changes
    conn.commit()

    # close connection
    conn.close()

    # clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)
# create query function:
def query():
    global conn, c
    # create a database or connect to one
    conn = sqlite3.connect('address of book.db')

    # create a cursor
    c = conn.cursor()

    # Query the  database:
    c.execute("SELECT *,oid FROM addresses")
    records = c.fetchall()
    # print(records)

    # Loop through results
    print_records = ''
    for record in records:
        print_records += str(record) + " \t" + str(record[6])+"\n"
# print_records += str(record[0])+ " " + str(record[1]) + "\n"
# print_records += str(record[0]) + " " + str(record[1]) + " " + " \t"+ " \t" + " \t" + str(record[6]).strip()+ "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    # commit changes
    conn.commit()

    # close connection
    conn.close()


# create text box:
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1)

# create text box label
f_name_label = Label(root, text='First name')
f_name_label.grid(row=0, column=0, padx=20, pady=(10, 0))
l_name_label = Label(root, text='Last name')
l_name_label.grid(row=1, column=0)
address_label = Label(root, text='Address')
address_label.grid(row=2, column=0)
city_label = Label(root, text='City')
city_label.grid(row=3, column=0)
state_label = Label(root, text='State')
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text='Zipcode')
zipcode_label.grid(row=5, column=0)
delete_box_label = Label(root, text="Select ID")
delete_box_label.grid(row=9, column=0)

# create submit button
sub_button = Button(root, text='Add a Record to Database', command=submit)
sub_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=70)

# create a query button:
query_button = Button(root, text='Show Records', command=query)
query_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# create a delete button:
delete_button = Button(root, text='Delete Record ', command=delete)
delete_button.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# create update button:
edit_button = Button(root, text='Edit Record ', command=edit)
edit_button.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# commit changes
conn.commit()

# close connection
conn.close()

root.mainloop()
