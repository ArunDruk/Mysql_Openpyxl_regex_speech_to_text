from tkinter import *

root=Tk() # Initializing the window and this is a base window, so naming it as root
root.geometry('300x300') # The dimesion for the window
l1=Label(root, text="Hello Arun")
l1.pack() # This is going to add label to the view

def button_func1():
    print ("You pressed on button 'Click'")

b1=Button(root, text="Click Me",command=button_func1)
b1.pack(side=LEFT) # This is going to add button to the view.

# In the Pack mention the side as LEFT, RIGHT, TOP and BOTTOM to place the position of the button

b2=Button(root, text="Click here",command=button_func1)
b2.pack(side=RIGHT) # This is going to add button to the view.

root.mainloop() # This will make the window to open and it remains open till we close it