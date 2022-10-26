from ast import Break
from ctypes import resize
from msilib.schema import Font
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import ImageTk, Image
import subprocess 
#a class for resizing background image when resizing window  
def resizer(e):
    global bg1,resized_bg,new_bg
    bg1=Image.open("home1.png") #open background image
    resized_bg=bg1.resize((e.width,e.height),Image.Resampling.LANCZOS) #fct for recizing image
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


#popup on add value
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
        d=int(plsValue.cget("text")[0:len(plsValue.cget("text"))-1])+int(enterAmount.get())
        plsValue.config(text=str(d)+'$')
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
 
window_height1 = 330
window_width1 = 600
x_cordinate1 = int((screen_width/2) - (window_width/2))
y_cordinate1 = int((screen_height/2) - (window_height/2))
#popup new category
lbllst = []
butlst = []
vallst = []
def popup_bonus1():
    def click2(event):
        categoryName.configure(state=NORMAL)
        categoryName.delete(0, END)
        categoryName.unbind('<Button-1>', clicked2)

    def click3(event):
        description.configure(state=NORMAL)
        description.delete(0, END)
        description.unbind('<Button-1>', clicked3)
    

    def addCategory():
        window_height = 230
        window_width = 500
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))


        #popup on add value
        def popup_bonuscat():
            
            def click(event):
                enterAmount.configure(state=NORMAL)
                enterAmount.delete(0, END)
                enterAmount.unbind('<Button-1>', clicked)

            def click1(event):
                comment.configure(state=NORMAL)
                comment.delete(0, END)
                comment.unbind('<Button-1>', clicked1)
        

            def changeData():
                k=int(amountCat.cget("text")[0:len(amountCat.cget("text"))-1])+int(enterAmount.get())
                d=int(plsValue.cget("text")[0:len(plsValue.cget("text"))-1])+int(enterAmount.get())
                amountCat.config(text=str(k)+'$')
                plsValue.config(text=str(d)+'$')
                
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

        catLabel = Label(window,width=15, text=categoryName.get(),font=('Abel',16),fg='gray',bg='#F8F9FA')
        catLabel.place(relx=0.2, rely=0.5*(len(butlst)+1))
        catButton= Button(window,width=8, text='Add Value', font=('Ariel',20),fg='white',bg='#2C49A0',command=popup_bonuscat)
        catButton.place(relx=0.344, rely=0.5*(len(butlst)+1))
        if (moneyType.get()=='Income'):
            amountCat= Label(window,width=15, text=str(0)+'$', font=('Ariel',20,"bold"),fg='green',bg='#F8F9FA')
            amountCat.place(relx=0.447, rely=0.5*(len(vallst)+1))
        else:
            amountCat= Label(window,width=15, text=str(0)+'$', font=('Ariel',20,"bold"),fg='red',bg='#F8F9FA')
            amountCat.place(relx=0.447, rely=0.5*(len(vallst)+1))
        lbllst.append(catLabel)
        butlst.append(catButton)
        vallst.append(amountCat)
        win1.destroy()

    win1 = Toplevel()
    win1.wm_title("Add New Category")
    win1.geometry("{}x{}+{}+{}".format(window_width1, window_height1, x_cordinate1, y_cordinate1))

    win1.configure(bg='white')

    b1 = ttk.Button(win1, text="Confirm", command=addCategory)
    b1.place(x=270,y=290)

    moneyType = ttk.Combobox(win1, width=19, font=('Ariel',25),
                            values=[
                                    "Income", 
                                    "Outcome"])
    moneyType.insert(0,"enter type")
    moneyType.place(x=120,y=40)

    categoryName = Entry(win1,width=20, font=('Ariel',25),bg='#FFFFFF')
    categoryName.place(x=120,y=120)
    categoryName.insert(0,"Category Name")
    clicked2 = categoryName.bind('<Button-1>', click2)


    description = Entry(win1,width=20, font=('Ariel',25),bg='#FFFFFF')
    description.place(x=120,y=200)
    description.insert(0,"Description Optional")
    clicked3 = description.bind('<Button-1>', click3)

    

    win1.wm_attributes('-toolwindow', 'True')



#added Value button
addedValue= Button(window,width=8, text='Add Value', font=('Ariel',20),fg='white',bg='#2C49A0',command=popup_bonus).place(x=660,y=440)



totalAmountLabel=Label(window,width=15, text=str(0)+'$', font=('Ariel',20,"bold"),fg='green',bg='#F8F9FA')
totalAmountLabel.place(x=860,y=455)

# add categorybutton 
addedCategory= tk.Button(window,width=14, text='Add Category', font=('Ariel',20),fg='white',bg='#2C49A0',command=popup_bonus1).place(x=1660,y=920)

catName=Label(window,width=15, text='Pocket Money', font=('Abel',16),fg='gray',bg='#F8F9FA')
catName.place(x=390,y=450)


# + sign
plsValue=Label(window,width=8, text='0'+'$', font=('Abel',16),fg='white',bg='#492CA0')
plsValue.place(x=1000,y=263)

# - sign
mnsValue=Label(window,width=8, text='0'+'$', font=('Abel',16),fg='white',bg='#2C83A0')
mnsValue.place(x=1560,y=263)

window.mainloop() 