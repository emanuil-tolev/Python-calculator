# This is an exercise for me to see what I can do with my Python
# skills. I am going to try to create a fully functioning calculator.

# Various Imports
import Tkinter
from Tkinter import *

# Defining the functions the calculator has: addition, subtraction,
# multiplication, division.

def addition():
    pass

def subtraction():
    pass

def multiplication():
    pass

def division():
    pass

# Creating the window

top = Tk()

# Creating the input. In this case we want the input to come from
# buttons. I will try with Tkinter first.

B1 = Tkinter.Button(top, text='1', height=1, width=1)
B1.grid(row='0', column='0')
B2 = Tkinter.Button(top, text='2', height=1, width=1)
B2.grid(row='0', column='1')
B3 = Tkinter.Button(top, text='3', height=1, width=1)
B3.grid(row='0', column='2')
B4 = Tkinter.Button(top, text='4', height=1, width=1)
B4.grid(row='1', column='0')
B5 = Tkinter.Button(top, text='5', height=1, width=1)
B5.grid(row='1', column='1')
B6 = Tkinter.Button(top, text='6', height=1, width=1)
B6.grid(row='1', column='2')
B7 = Tkinter.Button(top, text='7', height=1, width=1)
B7.grid(row='2', column='0')
B8 = Tkinter.Button(top, text='8', height=1, width=1)
B8.grid(row='2', column='1')
B9 = Tkinter.Button(top, text='9', height=1, width=1)
B9.grid(row='2', column='2')
B0 = Tkinter.Button(top, text='0', height=1, width=1)
B0.grid(row='3', column='1')

# Now the buttons for the mathematical operations.

B10 = Tkinter.Button(top, text='*', height=1, width=1)
B10.grid(row='0', column='3')
B11 = Tkinter.Button(top, text='/', height=1, width=1)
B11.grid(row='1', column='3')
B12 = Tkinter.Button(top, text='-', height=1, width=1)
B12.grid(row='2', column='3')
B13 = Tkinter.Button(top, text='+', height=1, width=1)
B13.grid(row='3', column='3')
B14 = Tkinter.Button(top, text='=', height=1, width=1)
B14.grid(row='3', column='2')
B15 = Tkinter.Button(top, text='.', height=1, width=1)
B15.grid(row='3', column='0')

top.mainloop()





