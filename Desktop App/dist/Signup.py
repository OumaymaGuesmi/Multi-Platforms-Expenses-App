from ctypes import resize
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import subprocess
#for resizing bg when resizing window
def resizer(e):
    global bg1,resized_bg,new_bg
    bg1=Image.open("Signup.png")
    resized_bg=bg1.resize((e.width,e.height),Image.ANTIALIAS)
    new_bg=ImageTk.PhotoImage(resized_bg)
    canvas1.create_image( 0, 0, image = new_bg, anchor = "nw")



#create and modify window 
window=Tk()
window.title("Sign Up")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(str(screen_width)+"x"+str(screen_height))
window.minsize(800,500)
window.iconbitmap("icolog.ico")
window.resizable(True,True)





#make password input not show
def show():
   p = password.get()
   Label(window, text="Your Password is: " + str(p)).pack()
password = StringVar()
def run_program():
    subprocess.call(["python", "login.py"])


#import image 
bg = ImageTk.PhotoImage(file = "Signup.png")
canvas1 = Canvas( window, width = screen_width,
                 height = screen_height)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")
window.bind('<Configure>',resizer)

#Signup form
#create a frame for the signup form
frame=Frame(window,width=700,height=490,bg='#fff')
frame.place(x=1080,y=346)
#heading
#create label
heading=Label(frame,text='Sign Up',fg='#2C49A0',bg='white',font=("Arial", 50,'bold'))
#place label
heading.place(x=0,y=0)
#username
usernamelbl = Label(frame, text='Username', font=('Ariel',20,"bold"),fg='lightgray',bg='white').place(x=4,y=99)
#get input 
username = Entry(frame,width=50, font=('Ariel',25),bg='#F1F3E6').place(x=8,y=135)
#password
passwordlbl = Label(frame, text='Password', font=('Ariel',20,"bold"),fg='lightgray',bg='white').place(x=4,y=185)
password = Entry(frame,width=50, textvariable=password, show="*" ,font=('Ariel',25),bg='#F1F3E6').place(x=8,y=221)
#confirmpassword
passwordlbl2 = Label(frame, text='Confirm Password', font=('Ariel',20,"bold"),fg='lightgray',bg='white').place(x=4,y=271)
password2 = Entry(frame,width=50, textvariable=password, show="*" ,font=('Ariel',25),bg='#F1F3E6').place(x=8,y=309)





#Signup button
signup= Button(frame,width=20, text='Create Account', font=('Ariel',20),fg='white',bg='#2C49A0',command= run_program).place(x=370,y=390)







window.mainloop() 