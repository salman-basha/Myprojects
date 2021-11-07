
from tkinter import *

root = Tk()
root.title("Simple Calculator")

root.configure(background="pink")

e = Entry(root, width=40, borderwidth=5, fg="white", bg="black")
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# e.insert(0,"Enter your number:")

def button_click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+ str(number))

def button_clear():
    e.delete(0,END)

def button_allclear():
    e.delete(0,END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "Addition"
    f_num= int(first_number)
    e.delete(0,END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "Addition":
        e.insert(0, f_num + int(second_number))
    if math =="subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))
    if math == "percentage":
        e.insert(0, f_num % int(second_number))


def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_mul():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

def button_percentage():
    first_number = e.get()
    global f_num
    global math
    math = "percentage"
    f_num = int(first_number)
    e.delete(0, END)

# define button

button_1 = Button(root, text='1', padx=45, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=45, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=42, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=45, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=45, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=42, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=45, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=45, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=42, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=45, pady=20, command=lambda: button_click(0))
#Decimal = Button(root, text=".", padx=47, pady=20, command=lambda: button_point)

button_add = Button(root, text="+", padx=40, pady=20, command=button_add)
button_sub = Button(root, text="-", padx=41, pady=20, command=button_sub)
button_mul = Button(root, text="*", padx=41, pady=20, command=button_mul)
button_div = Button(root, text="/", padx=41, pady=20, command=button_div)
button_percent = Button(root, text="%", padx=40, pady=20, command=button_percentage)

button_equal = Button(root, text="=", padx=141, pady=20, command=button_equal)
button_All_clear = Button(root, text="AC", padx=40, pady=20, command=button_allclear)
button_clear = Button(root, text="<x", padx=40, pady=20, command= button_clear)

# put the button on the screen

button_0.grid(row=5, column=0)
#Decimal.grid(row=5, column=1)
button_equal.grid(row=5, column=1, columnspan=4)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_add.grid(row=4, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_sub.grid(row=3, column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_mul.grid(row=2, column=3)

button_All_clear.grid(row=1, column=0)
button_clear.grid(row=1, column=1)
button_percent.grid(row=1, column=2)
button_div.grid(row=1, column=3)


root.mainloop()


#================================================================================================

#                      ANOTHER TYPE

# Python program to create a simple GUI
# calculator using Tkinter

# import everything from tkinter module
from tkinter import *

# globally declare the expression variable
expression = " "

# Function to update expression
# in the text entry box
def press(num):

    # point out the global expression variable
    global expression

    # concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    equation.set(expression)

# Function to evaluate the final expression
def equalpress():

    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.
    # Put that code inside the try block
    # which may generate the error
    try:
        global expression

        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(expression))
        equation.set(total)

        # initialze the expression variable
        # by empty string
        expression = " "

    # if error is generate then handle
    # by the except block
    except:
        equation.set("error")
        expression = " "

# Function to clear the contents
# of text entry box
def clear():
    global expression
    expression = " "
    equation.set(" ")

# Driver code
if __name__ == "__main__":

    # create a GUI window
    gui = Tk()

    # set the background colour of GUI window
    gui.configure(bg="pink")

    # set the title of GUI window
    gui.title("simple calculator")

    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()

    # create the text entry box for
    # showing the expression .
    e = Entry(gui, text=equation, width=40, borderwidth=5, fg="white", bg="black")

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    # create a Buttons and place at a particular
    # location inside the root window .
    # when user press the button, the command or
    # function affiliated to that button is executed .
    button1 = Button(gui, text=' 1 ', fg='black', bg='red',
					command=lambda: press(1), height=1, width=9)
    button1.grid(row=2, column=0)
    button2 = Button(gui, text=' 2 ', fg='black', bg='red',
					command=lambda: press(2), height=1, width=9)
    button2.grid(row=2, column=1)
    button3 = Button(gui, text=' 3 ', fg='black', bg='red',
					command=lambda: press(3), height=1, width=9)
    button3.grid(row=2, column=2)
    button4 = Button(gui, text=' 4 ', fg='black', bg='red',
					command=lambda: press(4), height=1, width=9)
    button4.grid(row=3, column=0)
    button5 = Button(gui, text=' 5 ', fg='black', bg='red',
					command=lambda: press(5), height=1, width=9)
    button5.grid(row=3, column=1)
    button6 = Button(gui, text=' 6 ', fg='black', bg='red',
					command=lambda: press(6), height=1, width=9)
    button6.grid(row=3, column=2)
    button7 = Button(gui, text=' 7 ', fg='black', bg='red',
					command=lambda: press(7), height=1, width=9)
    button7.grid(row=4, column=0)
    button8 = Button(gui, text=' 8 ', fg='black', bg='red',
					command=lambda: press(8), height=1, width=9)
    button8.grid(row=4, column=1)
    button9 = Button(gui, text=' 9 ', fg='black', bg='red',
					command=lambda: press(9), height=1, width=9)
    button9.grid(row=4, column=2)
    button0 = Button(gui, text=' 0 ', fg='black', bg='red',
					command=lambda: press(0), height=1, width=9)
    button0.grid(row=5, column=0)
    plus = Button(gui, text=' + ', fg='black', bg='red',
				command=lambda: press("+"), height=1, width=9)
    plus.grid(row=2, column=3)
    minus = Button(gui, text=' - ', fg='black', bg='red',
				command=lambda: press("-"), height=1, width=9)
    minus.grid(row=3, column=3)
    multiply = Button(gui, text=' * ', fg='black', bg='red',
					command=lambda: press("*"), height=1, width=9)
    multiply.grid(row=4, column=3)
    divide = Button(gui, text=' / ', fg='black', bg='red',
					command=lambda: press("/"), height=1, width=9)
    divide.grid(row=5, column=3)
    percent = Button(gui, text=' % ', fg='black', bg='red',
                    command=lambda: press("%"), height=1, width=9)
    percent.grid(row=6, column=3)
    leftparentheces = Button(gui, text=' ( ', fg='black', bg='red',
				command=lambda : press("("), height=1, width=9)
    leftparentheces.grid(row=5, column=1)
    rightparentheces = Button(gui, text=')', fg='black', bg='red',
				command=lambda : press(")"), height=1, width=9)
    rightparentheces.grid(row=5, column=2)
    equal = Button(gui, text=' = ', fg='black', bg='red',
                   command=equalpress, height=1, width=9)
    equal.grid(row=6, column=2)
    clear = Button(gui, text='Clear', fg='black', bg='red',
                   command=clear, height=1, width=9)
    clear.grid(row=6, column=1)
    Decimal = Button(gui, text='.', fg='black', bg='red',
                     command=lambda: press('.'), height=1, width=9)
    Decimal.grid(row=6, column=0)

    gui.mainloop()

