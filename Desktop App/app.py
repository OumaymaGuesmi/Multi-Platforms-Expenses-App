from ast import Break
from ctypes import resize
from msilib.schema import Font
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import ImageTk, Image
import subprocess 
from tkinter import *
import firstPage as f1
import login as f3
import signupp as f2


def raise_frame(frame):
    frame.tkraise()

root = Tk()

f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)


for frame in (f1, f2, f3):
    frame.grid(row=0, column=0, sticky='news')

Button(f1, text='Go to frame 2', command=lambda:raise_frame(f2)).pack()
Label(f1, text='FRAME 1').pack()

Label(f2, text='FRAME 2').pack()
Button(f2, text='Go to frame 3', command=lambda:raise_frame(f3)).pack()

Label(f3, text='FRAME 1').pack(side='left')
Button(f3, text='Go to frame 1', command=lambda:raise_frame(f1)).pack()



raise_frame(f1)
root.mainloop()