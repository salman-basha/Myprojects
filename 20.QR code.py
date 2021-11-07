from tkinter import*
from tkinter import messagebox
import pyqrcode
import os

window = Tk()
window.title("QR Code Generator")

# code generation
def generation():
    if len(subject.get()) != 0:
        global myQr
        myQr = pyqrcode.create(subject.get())
        qrImage = myQr.xbm(scale=6)
        global photo
        photo = BitmapImage(data=qrImage)
    else:
        messagebox.showinfo("Error!", "Please Enter The Subject")
    try:
        showcode()
    except:
        pass
# code showing:
def showcode():
    global photo
    notificationLabel.config(image=photo)
    subLabel.config(text='Showing QRCode for: ' + subject.get())
def save():
    # folder to save all the codes
    dir = path1 = os.getcwd() + "\\QR Codes"
    # create a folder is it doesn't exist
    if not os.path.exists(dir):
        os.makedirs(dir)
    try:
        if len(name.get()) != 0:
            qrImage = myQr.png(os.path.join(dir, name.get() + ".png"), scale=6)
        else:
            messagebox.showinfo("Error", "File name can not be empty!")
    except:
        messagebox.showinfo("Error!", "Please generate the code first")


label1 = Label(window, text="Enter The Subject", font=("helvetica ", 20))
label1.grid(row=0, column=0, sticky=N + S + E + W)

label2 = Label(window, text="Enter The File Name", font=("helvetica ", 20))
label2.grid(row=1, column=0, sticky=N + S + E + W)

subject = StringVar()
subject_entry = Entry(window, textvariable=subject, font=("helvetica ", 20))
subject_entry.grid(row=0, column=0, sticky=N + S + E + W)

name = StringVar()
name_entry = Entry(window, textvariable=name, font=("helvetica ", 20))
name_entry.grid(row=1, column=0, sticky=N + S + E + W)

create_button = Button(window, text="Create QR Code", font=("helvetica ", 20),
                       width=15, command=generation)
create_button.grid(row=0, column=3, sticky=N + S + E + W)

notificationLabel = Label(window)
notificationLabel.grid(row=2, column=1, sticky=N + S + E + W)

subLabel = Label(window, text="")
subLabel.grid(row=3, column=1, sticky=N + S + E + W)

showButton = Button(window, text="Save as PNG", font=("helvetica", 12),
                    width=15, command=save)
showButton.grid(row=1, column=3, sticky=N + S + E + W)
# Making responsive layout:
totalRows = 3
totalCols = 3
for row in range(totalRows + 1):
    window.grid_rowconfigure(row, weight=1)
for col in range(totalCols + 1):
    window.grid_rowconfigure(col, weight=1)
# looping the gui
window.mainloop()
