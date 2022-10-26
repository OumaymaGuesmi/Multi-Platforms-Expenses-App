from ast import Break
from ctypes import resize
from mimetypes import init
from msilib.schema import Font
from sqlite3 import Date
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from unicodedata import name
from PIL import ImageTk, Image
import subprocess 
from openpyxl import Workbook, load_workbook
import openpyxl
import os,os.path
from cgitb import text
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk

#check if excel file exists if it doesn't it will create one
if os.path.isfile("fieldname.xlsx"):
    Break
else:
    workbook = Workbook()
    workbook.save(filename="filednames.xlsx")

# ******************************************************************************

def turn(s):
        r=""
        for i in range (len(s)):
            r += "*"
        return r
class user ():
    def __init__(self,id,username,passwrod) :
        self.id=id
        self.username=username
        self.passwrod=passwrod
    
    def updateprofile(self,args={}) :
        #manage all errors when getting an input
        newpassword=args.get("newpassword","")
        confirmpassword=args.get("confirmpassword","")
        X=self.username
        username=args.get("username",X)
        if username == "" :
            username=self.username
        l1=args.get("label1",None)
        l2=args.get("label2",None)
        if (len(self.username)==0):
            if (len(newpassword)==0):
                if (len(confirmpassword)==0):
                    messagebox.showerror('Input Error', 'Username,password and cofirm password fields are empty')
                    Break
                else:
                    messagebox.showerror('Input Error', 'Username and password fields are empty')
                    Break  
            else:
                messagebox.showerror('Input Error', 'Username is empty')
                Break
        elif (len(newpassword)==0):
            messagebox.showerror('Input Error', 'Password is empty')
            Break
        elif (len(confirmpassword)==0):
            messagebox.showerror('Input Error', 'Confirm password is empty')
            Break
        else:
            #get input from password and username and chheck if password and confirm password match
            if (newpassword==confirmpassword):
                self.username=username
                self.passwrod=newpassword
                l2.config(text=turn(newpassword))
                l1.config(text=username[0:2])
                l1.config(text=username)
            else:
                messagebox.showerror('Input Error', 'Passwords do not match')
                Break
list = []
class field ( ):
    def __init__(self,idfield,name,typefield,threshold,description,initial=450):
        id=1
        self.initial=initial
        self.idfield=idfield
        self.name=name
        self.typefield=typefield
        self.threshold=threshold
        self.description=description
 
    
    def modifiyfiled(self,newname,newtypefield,newthreshold,newdescription):
        self.name=newname
        self.type=newtypefield
        self.threshold=newthreshold
        self.description=newdescription
    def modfierinitial (self):
        self.initial+=20
        return self.initial
    # def savefield(self,name,type,threshhold,description):
        

    # def deletefield(self):

    

class addedvalues  (field):
    def __init__(self,idvalue,comment,value,date,idfield,name,typefield,threshold,description,initial,total):
        self.total=total
        self.idvalue=idvalue
        self.comment=comment
        self.value=value
        self.date=date
        field.__init__(self,idfield,name,typefield,threshold,description,initial)

    def addvalue(self,newvalue):
        self.total+=newvalue
        self.value+=newvalue
        return newvalue
    def alertuser(self):
        if self.value - self.threshhold==10 :
            print("be careful")
    def total(self):
        return self.total
    def ija(self,new):
        self.idvalue=new
        return new
# class estimated(field,tk.Tk):
#     def __init__(self,initial=450):
#         window=Tk()
#         estimatedvalue = Entry(window,width=15, font=('Ariel',25),bg='#FFFFFF')
#         self.estimatedvalue=estimatedvalue
#         catestimatedvalue = Label(window,width=15, text=estimatedvalue.get(),font=('Abel',16),fg='gray',bg='#F8F9FA')
#         self.catestimatedvalue=catestimatedvalue
#         catrestvalue = Label(window,width=15, text=estimatedvalue.get(),font=('Abel',16),fg='gray',bg='#F8F9FA')
#         self.catrestvalue=catrestvalue
#         self.initial=initial
        
#     def modfierinitial (self):
#         self.initial+=30
#         return self.initial
#     def estimatedvalue(self):
#         return self.estimatedvalue
#     def catestmatedvalue(self):
#         return self.catestimatedvalue
#     def catrestvalue(self):
#         return self.catrestvalue
    

# estimated =estimated()
# print (estimated.estimatedvalue.get())

# # def home () :
# #     newField1 = field(1,"name","income","threshold","description")
# #     for i in range (4):
# #         list=[]
# #         list.append(newField1.modfierinitial())

# #     return list

# # home ()

    







     