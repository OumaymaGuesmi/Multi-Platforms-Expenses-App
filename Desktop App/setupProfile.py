from ast import Break
from asyncio.windows_events import NULL
from cProfile import label
from ctypes import resize
from tkinter import *
from tkinter import ttk
from tokenize import String
from PIL import ImageTk, Image
from tkinter import messagebox
#for resizing bg when resizing window
def resizer(e):
    global bg1,resized_bg,new_bg
    bg1=Image.open("setupprofile.png")
    resized_bg=bg1.resize((e.width,e.height),Image.Resampling.LANCZOS)
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







#import image 
bg = ImageTk.PhotoImage(file = "setupprofile.png")
canvas1 = Canvas( window, width = screen_width,
                 height = screen_height)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")
window.bind('<Configure>',resizer)


def show():
   p = password.get()
   Label(window, text="Your Password is: " + str(p)).pack()

password = StringVar()


#username
username = Entry(window,width=17,border=1, font=('Abel',15),bg='#F8F9FA')
username.place(x=550,y=680)
#password
password = Entry(window,width=17,border=1, textvariable=password, show="*" ,font=('Abel',15),bg='#F8F9FA')
password.place(x=550,y=740)
#confirmpassword
password2 = Entry(window,width=17,border=1, textvariable=password, show="*" ,font=('Abel',15),bg='#F8F9FA')
password2.place(x=550,y=800)

#turn the password input into *
def turn(s):
    r=""
    for i in range (len(s)):
        r += "*"
    return r


#a class to change data all over the page when the system gets an input when updating password and username
def change_data():
    #manage all errors when getting an input
    if (len(username.get())==0):
        if (len(password.get())==0):
            if (len(password2.get())==0):
                messagebox.showerror('Input Error', 'Username,password and cofirm password fields are empty')
                Break
            else:
                messagebox.showerror('Input Error', 'Username and password fields are empty')
                Break  
        else:
            messagebox.showerror('Input Error', 'Username is empty')
            Break
    elif (len(password.get())==0):
        messagebox.showerror('Input Error', 'Password is empty')
        Break
    elif (len(password2.get())==0):
        messagebox.showerror('Input Error', 'Confirm password is empty')
        Break
    else:
        #get input from password and username and chheck if password and confirm password match
        if (password.get()==password2.get()):
            user.config(text=username.get())
            pas.config(text=turn(password.get()))
            ico_label.config(text=username.get()[0:2])
            use_label.config(text=username.get())
            clear_text()
        else:
            messagebox.showerror('Input Error', 'Passwords do not match')
            Break

#a class to clear fields after saving or when canceling            
def clear_text():
   username.delete(0, END) #clear entry field
   password.delete(0, END)
   password2.delete(0, END)


#labels for showing the existing user and password
#user label 
user= Label(window,width=25, text="Ninja_Unicorn", font=('Abel',15),fg='lightgray',bg='#F8F9FA',border=1)
user.place(x=370,y=400)
#password label
pas= Label(window,width=25, text="*****", font=('Abel',15),fg='lightgray',bg='#F8F9FA',border=1)
pas.place(x=932,y=400)
#while clicking on dashboard button change the path
def dash_butt():
    path.config(text=button.cget('text'))
#image button dashboard
#Import the image using PhotoImage function
click_btn= PhotoImage(file='Dash.png')

#Let us create a label for button event
img_label= Label(image=click_btn)

#Let us create a dummy button and pass the image
button= Button(window, image=click_btn,bg='#2C49A0',activebackground='#2C49A0',borderwidth=0,text='Dashboard',command=dash_butt)
button.place(x=65,y=190)

#while clicking on home button change the path
def home_butt():
    path.config(text=button1.cget('text'))
#image button Home
#Import the image using PhotoImage function
click_btn1= PhotoImage(file='home.png')

#Let us create a label for button event
img_label1= Label(image=click_btn1)

#Let us create a dummy button and pass the image
button1= Button(window, image=click_btn1,bg='#2C49A0',activebackground='#2C49A0',borderwidth=0,text='',command=home_butt)
button1.place(x=65,y=290)
#while clicking on history button change path
def hist_butt():
    path.config(text=button2.cget('text'))
#image button History
#Import the image using PhotoImage function
click_btn2= PhotoImage(file='hist.png')

#Let us create a label for button event
img_label2= Label(image=click_btn1)

#Let us create a dummy button and pass the image
button2= Button(window, image=click_btn2,bg='#2C49A0',activebackground='#2C49A0',borderwidth=0,text='History',command=hist_butt)
button2.place(x=60,y=380)

#while clicking on setup profile button change path
def set_butt():
    path.config(text=button3.cget('text'))
#image button Setup
#Import the image using PhotoImage function

click_btn3= PhotoImage(file='set.png')

#Let us create a label for button event
img_label3= Label(image=click_btn3)

#Let us create a dummy button and pass the image
button3= Button(window, image=click_btn3,bg='#2C49A0',activebackground='#2C49A0',borderwidth=0,text='Setup Profile',command=set_butt)
button3.place(x=69,y=490)
#while clicling on logout button change path
def log_butt():
    path.config(text=button4.cget('text'))
#image button Logout
#Import the image using PhotoImage function

click_btn4= PhotoImage(file='out.png')

#Let us create a label for button event
img_label4= Label(image=click_btn4)

#Let us create a dummy button and pass the image
button4= Button(window, image=click_btn4,bg='#2C49A0',activebackground='#2C49A0',borderwidth=0,text='Logout',command=log_butt)
button4.place(x=74,y=580)

#image button icon
#Import the image using PhotoImage function
clickk_btn= PhotoImage(file='circle.png')

#Let us create a label for button event
img_label= Label(image=click_btn)

#Let us create a dummy button and pass the image
button= Button(window, image=clickk_btn,bg='#F8F9FA',borderwidth=0,activebackground='#F8F9FA')
button.place(x=1710,y=25)


#icon input
ico_label= Label(window,width=2, text="Ni", font=('Abel',15,'bold'),fg='white',bg='#2C49A0',border=1)
ico_label.place(x=1725,y=35)

#username input
use_label=Label(window,width=13, text="Ninja_Unicorn", font=('Poppins',14),bg='#F8F9FA',fg='#2C49A0')
use_label.place(x=1550,y=35)



#buttons
save= Button(window,width=8, text='Save', font=('Abel',15),fg='white',bg='#2C49A0',command=change_data,).place(x=1500,y=850)
cancel= Button(window,width=8, text='Cancel', font=('Abel',15),fg='#000000',bg='#E9EAEB',command=clear_text).place(x=1380,y=850)


    

#path
path= Label(window,width=10, text="Setup Profile", font=('Abel',24),fg='#2C49A0',bg='#F8F9FA')
path.place(x=680,y=137)


#mainloop
window.mainloop() 


