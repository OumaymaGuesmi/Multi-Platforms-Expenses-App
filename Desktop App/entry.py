import tkinter as tk
from tkinter import *
from tokenize import Comment
import time 

gui = tk.Tk()
gui.geometry("200x200")

def myFunction(event):
    
    comment = Entry(gui,width=15, font=('Ariel',25),bg='#FFFFFF')
    comment.place(x=0,y=0)
    def destroy():
        b.destroy()
    def myfunction2():
        catLabel = Label(gui,width=15, text=comment.get(),font=('Abel',16),fg='gray',bg='#F8F9FA')
        catLabel.place(x=100, y=0)
        comment.destroy()
        destroy()
    
 



    b = Button(gui, text="Confirm", command=myfunction2)
    b.place(x=0,y=0)



gui.bind('<Return>', myFunction)

gui.mainloop()