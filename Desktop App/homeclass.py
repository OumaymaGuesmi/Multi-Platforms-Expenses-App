from cProfile import label
from cgitb import text
from email.utils import collapse_rfc2231_value
from logging import root
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk
import backopeartion as up


#create Window 
Window=Tk()

#modify Window title
Window.title("Home")
#put screen width and height as big as the laptop's screen
screen_width = Window.winfo_screenwidth()
screen_height = Window.winfo_screenheight()
Window.geometry(str(screen_width)+"x"+str(screen_height))
#put Window minimum size 
Window.minsize(800,500)
#import an icon
Window.iconbitmap("icolog.ico")
#render the Window resizable
Window.resizable(True,True)





bg = ImageTk.PhotoImage(file = "finally.jpg")
bg2 = ImageTk.PhotoImage(file = "finally.jpg")
bg3 = ImageTk.PhotoImage(file = "finally.jpg")
bg4 = ImageTk.PhotoImage(file = "finally.jpg")
bg5 = ImageTk.PhotoImage(file = "finally.jpg")

image_list=[bg,bg2,bg3,bg4,bg5]
status=Label(Window,text="Pages 1 of " + str(len(image_list)),bd=1,relief=SUNKEN)
canvas1 = Canvas( Window, width = screen_width,
                 height = screen_height)
canvas1.pack(fill = "both", expand = False)
canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")
# my_label=Label(image=bg)
# my_label.grid()

def forword(image_number):
    global my_label
    global button_forword
    global button_back
    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])
    button_forword=Button(Window,text=">>",command=lambda:forword(image_number+1))
    button_back=Button(Window,text="<<",command=lambda:back(image_number-1))
    if image_number==5:
        button_forword=Button(Window,text=">>",state=DISABLED)
    my_label.grid()
    button_back.place(x=1000,y=970)
    button_forword.place(x=1200,y=970)
    status=Label(Window,text="Pages "+ str(image_number) + "of " + str(len(image_list)),bd=1,relief=SUNKEN)
    status.grid(row=0,column=0,columnspan=3)
def back(image_number):
    global my_label
    global button_forword
    global button_back

    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])
    button_forword=Button(Window,text=">>",command=lambda:forword(image_number+1))
    button_back=Button(Window,text="<<",command=lambda:back(image_number-1))
    if image_number==1:
        button_back=Button(Window,text=">>",state=DISABLED)
    my_label.grid()
    button_back.place(x=1000,y=970)
    button_forword.place(x=1200,y=970)
    status=Label(Window,text="Pages "+ str(image_number) + "of " + str(len(image_list)),bd=1,relief=SUNKEN)
    status.grid(row=0,column=0,columnspan=3)


button_back=Button(Window,text="<<",command=back,state=DISABLED)
button_forword=Button(Window,text=">>",command= lambda: forword(2))  

button_back.place(x=1000,y=970)
button_forword.place(x=1200,y=970)



#while clicking on dashboard button change the path
def dash_butt():
    path.config(text=button.cget('text'))
#image button dashboard
#Import the image using PhotoImage function
click_btn= PhotoImage(file='Dash.png')

#Let us create a label for button event
img_label= Label(image=click_btn)

#Let us create a dummy button and pass the image
button= Button(Window, image=click_btn,bg='#2C49A0',activebackground='#2C49A0',borderwidth=0,text='Dashboard',command=dash_butt)
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
button1= Button(Window, image=click_btn1,bg='#2C49A0',activebackground='#2C49A0',borderwidth=0,text='',command=home_butt)
button1.place(x=65,y=290)
#while clicking on history button change path
def hist_butt():
    path.config(text=button2.cget('text'))
#image button History
#Import the image using PhotoImage function
click_btn2= PhotoImage(file='hist.png')

#Let us create a label for button event
img_label2= Label(image=click_btn2)

#Let us create a dummy button and pass the image
button2= Button(Window, image=click_btn2,bg='#2C49A0',activebackground='#2C49A0',borderwidth=0,text='History',command=hist_butt)
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
button3= Button(Window, image=click_btn3,bg='#2C49A0',activebackground='#2C49A0',borderwidth=0,text='Setup Profile',command=set_butt)
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
button4= Button(Window, image=click_btn4,bg='#2C49A0',activebackground='#2C49A0',borderwidth=0,text='Logout',command=log_butt)
button4.place(x=74,y=580)

#path
path= Label(Window,width=10, text="", font=('Abel',24),fg='#2C49A0',bg='#F8F9FA')
path.place(x=680,y=137)

#image button icon
#Import the image using PhotoImage function
clickk_btn= PhotoImage(file='circle.png')

#Let us create a dummy button and pass the image
button= Button(Window, image=clickk_btn,bg='#F8F9FA',borderwidth=0,activebackground='#F8F9FA')
button.place(x=1710,y=25)

#icon input
ico_label= Label(Window,width=2, text="Ni", font=('Abel',15,'bold'),fg='white',bg='#2C49A0',border=1)
ico_label.place(x=1725,y=35)


#username input
use_label=Label(Window,width=13, text="Ninja_Unicorn", font=('Poppins',14),bg='#F8F9FA',fg='#2C49A0')
use_label.place(x=1550,y=35)


#Let us create a label for button event
img_label= Label(image=click_btn)
Window_height = 230
Window_width = 500
x_cordinate = int((screen_width/2) - (Window_width/2))
y_cordinate = int((screen_height/2) - (Window_height/2))

#intialize field and added value to use later on
newField1 = up.field(1,"name","income","threshold","description")
newField = up.addedvalues(1,"comment",0,"date","idfield","name",0,0,"description",600,0)
newField3 = up.addedvalues(4,"comment",0,"date","idfield","name",0,0,"description",600,0)


# + sign
plsValue=Label(Window,width=8, text='0'+'$', font=('Abel',16),fg='white',bg='#492CA0')
plsValue.place(x=1000,y=263)
plsValue.config(text=str(newField.value)+'$')

#set predefined Window height for the popout
Window_height1 = 330
Window_width1 = 600
x_cordinate1 = int((screen_width/2) - (Window_width/2))
y_cordinate1 = int((screen_height/2) - (Window_height/2))
#popup new category
total=0
t=0
f=0
bf=0
k=0
#set the label for the number that goes up every time u add a category
catNbr=Label(Window,width=5, text='0', font=('Abel',30),fg='white',bg='#A0832C')
catNbr.place(x=400,y=240)


def popup_bonus1():
    #initialize field
    newField = up.addedvalues(0,"comment",0,"date","idfield","name",0,0,"description",600,0)
    # def myFunction(event):   
    #         estimatedvalue = Entry(Window,width=15, font=('Ariel',25),bg='#FFFFFF')
    #         estimatedvalue.place(x=900,y=newField1.modfierinitial()-94)
    #         def destroy():
    #             b.destroy()
    #         def myfunction2():
    #             newField.ija(int(estimatedvalue.get()))
    #             catestimatedvalue = Label(Window,width=15, text=estimatedvalue.get(),font=('Abel',16),fg='gray',bg='#F8F9FA')
    #             catestimatedvalue.place(x=950, y=newField1.modfierinitial()-140)
    #             estimatedvalue.destroy()
    #             destroy()
                
                
    #         b = Button(Window, text="Confirm", command=myfunction2)
    #         b.place(x=1190,y=newField1.modfierinitial()-116)
            


    # Window.bind('<Return>', myFunction)
    
    #clear entry on click
    def click2(event):
        categoryName.configure(state=NORMAL)
        categoryName.delete(0, END)
        categoryName.unbind('<Button-1>', clicked2)

    def click3(event):
        description.configure(state=NORMAL)
        description.delete(0, END)
        description.unbind('<Button-1>', clicked3)
    
    #fuction to add category
    def addCategory():
        Window_height = 230
        Window_width = 500
        x_cordinate = int((screen_width/2) - (Window_width/2))
        y_cordinate = int((screen_height/2) - (Window_height/2))
        global bf
        bf+=1
        catNbr.config(text=str(bf))
        catestimatedvalue = Label(Window,width=15, text="",font=('Abel',16),fg='gray',bg='#F8F9FA')
        catestimatedvalue.place(x=5000,y=5000)
        def myfunction2():
                # newField.ija(int(estimatedvalue.get()))
                catestimatedvalue.config(text=estimatedvalue.get())
                catestimatedvalue.place(x=940, y=newField1.modfierinitial()-120)
                catrestvalue.config(text=str(int(catestimatedvalue.cget("text"))-int(amountCat.cget("text")[0:len(amountCat.cget("text"))-1])))
                estimatedvalue.destroy()
                b.destroy()
                
            
            
                
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
            
            
            
            #function to change data on click
            def changeData():
                global t 
                global f
                global b
                global k
                
                
                
                if (amountCat.cget("fg")=="green"):
                    k=int(enterAmount.get())
                    t+=newField.addvalue(k)
                    plsValue.config(text=str(t)+'$')
                    c=int(newField.idvalue)
                    r=k-c
                    if int(c)>=k:
                        catrestvalue.config(text=str(r))
                    
                else:
                    k=int(enterAmount.get())
                    f+=newField.addvalue(k)
                    mnsValue.config(text=str(f)+'$')
                    c=int(newField.idvalue)
                    r=c-k
                    if int(c)>=k:
                        catrestvalue.config(text=str(r))
                
                amountCat.config(text=str(newField.value)+'$')
                catrestvalue.config(text=str(int(catestimatedvalue.cget("text"))-int(amountCat.cget("text")[0:len(amountCat.cget("text"))-1])))
                win.destroy()
                

            
            
            win = Toplevel()
            win.wm_title("Add New Value")
            win.geometry("{}x{}+{}+{}".format(Window_width, Window_height, x_cordinate, y_cordinate))

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

            win.wm_attributes('-toolWindow', 'True')
    
        catLabel = Label(Window,width=15, text=categoryName.get(),font=('Abel',16),fg='gray',bg='#F8F9FA')
        catLabel.place(x=390, y=newField1.modfierinitial())
        catButton= Button(Window,width=8, text='Add Value', font=('Ariel',20),fg='white',bg='#2C49A0',command=popup_bonuscat)
        catButton.place(x=660, y=newField1.modfierinitial()-35)
        catrestvalue = Label(Window,width=20, text="Waiting for estimated",font=('Abel',16),fg='gray',bg='#F8F9FA')
        catrestvalue.place(x=1270, y=newField1.modfierinitial()-40)
        estimatedvalue = Entry(Window,width=15, font=('Ariel',25),bg='#FFFFFF')
        estimatedvalue.place(x=900,y=newField1.modfierinitial()-65)
        b = Button(Window, text="Confirm", command=myfunction2)
        b.place(x=1190,y=newField1.modfierinitial()-77)
        


        #test if money type is income change amount color to green and to red if it is an outcome
        if (moneyType.get()=='Income'):
            amountCat= Label(Window,width=15, text=str(0)+'$', font=('Ariel',20,"bold"),fg='green',bg='#F8F9FA')
            amountCat.place(x=1640, y=newField1.modfierinitial()-105)
        else:
            amountCat= Label(Window,width=15, text=str(0)+'$', font=('Ariel',20,"bold"),fg='red',bg='#F8F9FA')
            amountCat.place(x=1640, y=newField1.modfierinitial()-105)
        
        
        win1.destroy()
        
    win1 = Toplevel()
    win1.wm_title("Add New Category")
    win1.geometry("{}x{}+{}+{}".format(Window_width1, Window_height1, x_cordinate1, y_cordinate1))

    win1.configure(bg='white')

    b1 = ttk.Button(win1, text="confirm", command=addCategory)
    b1.place(x=270,y=290)
    
    
    #create a multiple selection field for the outcome and income
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

    win1.wm_attributes('-toolWindow', 'True')
    


    







# add categorybutton 
addedCategory= tk.Button(Window,width=14, text='Add Category', font=('Ariel',20),fg='white',bg='#2C49A0',command=popup_bonus1).place(x=1660,y=920)



# - sign
mnsValue=Label(Window,width=8, text='0'+'$', font=('Abel',16),fg='white',bg='#2C83A0')
mnsValue.place(x=1560,y=263)


# pages screen home





Window.mainloop() 