from ctypes import resize
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import subprocess

#a class for resizing background image when resizing window
def resizer(e):
    global bg1,resized_bg,new_bg
    bg1=Image.open("firstpage.png") #open background image
    resized_bg=bg1.resize((e.width,e.height),Image.ANTIALIAS) #fct for recizing image
    new_bg=ImageTk.PhotoImage(resized_bg) #put the image in a variable
    canvas1.create_image( 0, 0, image = new_bg, anchor = "nw") #put the image in a canva 
    


#run signup script class
def run_program():
    subprocess.call(["python", "Signup.py"])


#create window 
window=Tk()
#modify window title
window.title("Sign Up")
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
bg = ImageTk.PhotoImage(file = "firstpage.png")
canvas1 = Canvas( window, width = screen_width,
                 height = screen_height)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")
window.bind('<Configure>',resizer)

#Signup button
signup= Button(window,width=20, text='Sign Up', font=('Ariel',20),fg='white',bg='#2C49A0',command= run_program).place(x=1150,y=600)

window.mainloop() 