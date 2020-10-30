from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector

allBid = []
mypass = "mirella@29"
mydatabase="db"
con = mysql.connector.connect( host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

cur.execute("select bid from books;")

bookTable='books'
bid='101'

for i in cur:
    allBid.append(i[0])

print(allBid)    

if bid in allBid:
            checkAvail = "select status from "+bookTable+" where bid = '"+bid+"'"
            cur.execute(checkAvail)
            
            for i in cur:
                check = i[0]
            print(check)    
                
            if check == 'avail':
                status = True
            else:
                status = False