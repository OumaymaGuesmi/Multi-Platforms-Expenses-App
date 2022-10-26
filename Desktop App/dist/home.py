from ctypes import resize
from msilib.schema import Font
from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import ImageTk, Image
import subprocess
#a class for resizing background image when resizing window
def resizer(e):
    global bg1,resized_bg,new_bg
    bg1=Image.open("home1.png") #open background image
    resized_bg=bg1.resize((e.width,e.height),Image.ANTIALIAS) #fct for recizing image
    new_bg=ImageTk.PhotoImage(resized_bg) #put the image in a variable
    canvas1.create_image( 0, 0, image = new_bg, anchor = "nw") #put the image in a canva 


    



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
bg = ImageTk.PhotoImage(file = "home1.png")
canvas1 = Canvas( window, width = screen_width,
                 height = screen_height)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")
window.bind('<Configure>',resizer)


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

#path
path= Label(window,width=10, text="", font=('Abel',24),fg='#2C49A0',bg='#F8F9FA')
path.place(x=680,y=137)

#image button icon
#Import the image using PhotoImage function
clickk_btn= PhotoImage(file='circle.png')

#Let us create a dummy button and pass the image
button= Button(window, image=clickk_btn,bg='#F8F9FA',borderwidth=0,activebackground='#F8F9FA')
button.place(x=1710,y=25)

#icon input
ico_label= Label(window,width=2, text="Ni", font=('Abel',15,'bold'),fg='white',bg='#2C49A0',border=1)
ico_label.place(x=1725,y=35)


#username input
use_label=Label(window,width=13, text="Ninja_Unicorn", font=('Poppins',14),bg='#F8F9FA',fg='#2C49A0')
use_label.place(x=1550,y=35)


#Let us create a label for button event
img_label= Label(image=click_btn)
window_height = 230
window_width = 500
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))



def popup_bonus():
    
    def click(event):
        enterAmount.configure(state=NORMAL)
        enterAmount.delete(0, END)
        enterAmount.unbind('<Button-1>', clicked)

    def click1(event):
        comment.configure(state=NORMAL)
        comment.delete(0, END)
        comment.unbind('<Button-1>', clicked1)
        
    def changeData():
        k=int(totalAmountLabel.cget("text")[0:len(totalAmountLabel.cget("text"))-1])+int(enterAmount.get())
        totalAmountLabel.config(text=str(k)+'$')
        win.destroy()

    win = Toplevel()
    win.wm_title("Add New Value")
    win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    win.configure(bg='white')


    b = ttk.Button(win, text="Confirm", command=changeData)
    b.place(x=210,y=190)

    enterAmount = Entry(win,width=15, font=('Ariel',25),bg='#FFFFFF')
    enterAmount.place(x=110,y=40)
    enterAmount.insert(0,"Enter Amount")
    clicked = enterAmount.bind('<Button-1>', click)


    comment = Entry(win,width=15, font=('Ariel',25),bg='#FFFFFF')
    comment.place(x=110,y=110)
    comment.insert(0,"Comment Optional")
    clicked1 = comment.bind('<Button-1>', click1)

    win.wm_attributes('-toolwindow', 'True')
 

#added Value button
addedValue= Button(window,width=8, text='Add Value', font=('Ariel',20),fg='white',bg='#2C49A0',command=popup_bonus).place(x=660,y=440)



totalAmountLabel=Label(window,width=15, text=str(0)+'$', font=('Ariel',20,"bold"),fg='green',bg='#F8F9FA')
totalAmountLabel.place(x=860,y=455)


catName=Label(window,width=15, text='Pocket Money', font=('Abel',16),fg='gray',bg='#F8F9FA')
catName.place(x=390,y=450)
window.mainloop() 