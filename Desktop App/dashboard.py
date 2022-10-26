from tkinter import *
from turtle import width
from PIL import ImageTk
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from tkcalendar import *


#create Window 
Window=Tk()

#modify Window title
Window.title("Dashboard")
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





bg = ImageTk.PhotoImage(file = "Dashboard.png")



canvas1 = Canvas( Window, width = screen_width,
                 height = screen_height)
canvas1.pack(fill = "both", expand = False)
canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")
# my_label=Label(image=bg)
# my_label.grid()


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
path= Label(Window,width=10, text="Dashboard", font=('Abel',24),fg='#2C49A0',bg='#FFFFFF')
path.place(x=580,y=100)

#image button icon
#Import the image using PhotoImage function
clickk_btn= PhotoImage(file='circle.png')

#Let us create a dummy button and pass the image
button= Button(Window, image=clickk_btn,bg='#FFFFFF',borderwidth=0,activebackground='#F8F9FA')
button.place(x=1710,y=25)

#icon input
ico_label= Label(Window,width=2, text="Ni", font=('Abel',15,'bold'),fg='white',bg='#2C49A0',border=1)
ico_label.place(x=1725,y=35)


#username input
use_label=Label(Window,width=13, text="Ninja_Unicorn", font=('Poppins',14),bg='#FFFFFF',fg='#2C49A0')
use_label.place(x=1550,y=35)



#pie chart for income
#import excel income file data
incomeData=pd.read_excel("C:/Users/PC/Desktop/Education/Stage_Achraf_Oumayma/implementation maquettes Desktop/income.xlsx")

#sum all the incomes by category
sumWork=sum(incomeData['Work'])
sumPocket=sum(incomeData['Pocket'])
sumParents=sum(incomeData['Parents'])

#plot income pie chart
incomeFig=plt.figure(figsize=(6,6), dpi=100)
incomeFig.set_size_inches(6,4)

#data to plot
labels= 'Work','Pocket','Parents'
sizes= [sumWork,sumPocket,sumParents]
colors=['#007AFF','#FB8832','#9013FE']
explode=(0,0,0)

#plot pie chart
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=False,startangle=140)


plt.axis('equal')

canvasbar= FigureCanvasTkAgg(incomeFig,master=Window)
canvasbar.draw()
canvasbar.get_tk_widget().place(x=800,y=300)


#pie chart for outcome
#import excel income file data
outcomeData=pd.read_excel("C:/Users/PC/Desktop/Education/Stage_Achraf_Oumayma/implementation maquettes Desktop/outcome.xlsx")

#sum all the incomes by category
sumDoctor=sum(outcomeData['Doctor'])
sumTransport=sum(outcomeData['Transport'])
sumFood=sum(outcomeData['Food'])

#plot income pie chart
outcomeFig=plt.figure(figsize=(6,6), dpi=100)
outcomeFig.set_size_inches(6,4)

#data to plot
labels1= 'Doctor','Transport','Food'
sizes1= [sumDoctor,sumTransport,sumFood]
colors1=['#007AFF','#FB8832','#9013FE']
explode1=(0,0,0)

#plot pie chart
plt.pie(sizes1,explode=explode1,labels=labels1,colors=colors1,autopct='%1.1f%%',shadow=False,startangle=140)


plt.axis('equal')

canvasbar1= FigureCanvasTkAgg(outcomeFig,master=Window)
canvasbar1.draw()
canvasbar1.get_tk_widget().place(x=1300,y=300)



#calendar 
cal = Calendar(Window, selectmode = 'day',
               year = 2022, month = 10,
               day = 10,font=('Ariel',15))
cal.place(x=450,y=380)


 
def grab_date():
    date.config(text = "Selected Date is: " + cal.get_date())
 
# Add Button and Label
calendarButton=Button(Window, text = "Get Date",
       command = grab_date)
calendarButton.place(x=600,y=650)
 
date = Label(Window, text = "")
date.place(x=550,y=700)


Window.mainloop() 