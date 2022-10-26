from ctypes import resize
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import subprocess
#for resizing bg when resizing window
def resizer(e):
    global bg1,resized_bg,new_bg
    bg1=Image.open("logg.png")
    resized_bg=bg1.resize((e.width,e.height),Image.ANTIALIAS)
    new_bg=ImageTk.PhotoImage(resized_bg)
    canvas1.create_image( 0, 0, image = new_bg, anchor = "nw")
def run_program():
    subprocess.call(["python", "setupProfile.py"])


#create and modify window 
window=Tk()
window.title("Login")
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
#import image 
bg = ImageTk.PhotoImage(file = "logg.png")
canvas1 = Canvas( window, width = screen_width,
                 height = screen_height)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")
window.bind('<Configure>',resizer)

#login form
frame=Frame(window,width=700,height=390,bg='#fff')
frame.place(x=1080,y=346)
#heading
heading=Label(frame,text='Login',fg='#2C49A0',bg='white',font=("Arial", 50,'bold'))
heading.place(x=0,y=5)
#username
usernamelbl = Label(frame, text='Username', font=('Ariel',20,"bold"),fg='lightgray',bg='white').place(x=4,y=99)
username = Entry(frame,width=50, font=('Ariel',25),bg='#F1F3E6').place(x=8,y=135)
#password
passwordlbl = Label(frame, text='Password', font=('Ariel',20,"bold"),fg='lightgray',bg='white').place(x=4,y=185)
password = Entry(frame,width=50, textvariable=password, show="*" ,font=('Ariel',25),bg='#F1F3E6').place(x=8,y=221)
#Login button
login= Button(frame,width=20, text='Login', font=('Ariel',20),fg='white',bg='#2C49A0',command=run_program).place(x=370,y=320)

window.mainloop() 