


# methode 2 without classe
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk
from tkinter import *


def raise_frame(frame):
    frame.tkraise()


#create window 
window=Tk()
#modify window title
window.title("Home")
#put screen width and height as big as the laptop's screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(str(screen_width)+"x"+str(screen_height))
#put window minimum size 
window.minsize(800,500)
#import an icon
window.iconbitmap("icolog.ico")
#render the window resizable
window.resizable(True,True)

#import image 
bg = ImageTk.PhotoImage(file = "finally.jpg")
canvas1 = Canvas( window, width = screen_width,
                  height = screen_height)
# canvas1.pack(fill = "both", expand = False)
canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")

f1 = Frame(window)
f2 = Frame(window)
f3 = Frame(window)
f4 = Frame(window)

for frame in (f1, f2, f3, f4):
    frame.grid(row=0, column=0, sticky='news')

Button(f1, text='Go to frame 2', command=lambda:raise_frame(f2)).pack()
Label(f1, text='go FRAME 1').pack()

Label(f2, text='FRAME 2').pack()
Button(f2, text='Go to frame 3', command=lambda:raise_frame(f3)).pack()

Label(f3, text='FRAME 3').pack(side='left')
Button(f3, text='Go to frame 4', command=lambda:raise_frame(f4)).pack(side='left')

Label(f4, text='FRAME 4').pack()
Button(f4, text='Goto to frame 1', command=lambda:raise_frame(f1)).pack()

raise_frame(f1)
window.mainloop()

