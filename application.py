# Aqui escribe tu codigo

import os
import sys
import time
import smtplib
import getpass
from collections import OrderedDict
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
All={}
country=[]
capitals=[]        
def ask():
    enter=raw_input("do you wish to keep entering y/n: " )
    enter=enter.lower()
    if enter == "y":
        add_Country()
    elif enter== "n":
        menu()
    else:
        print "It is not valid, pleas try again"
        limpiar()
        ask()
def add_Country():
    limpiar()
    idea = True
    while idea == True:
        print"_______________________"
        enter_Country =raw_input(" Enter a Country: ")
        print"_______________________"
        if enter_Country.isalpha() or " " in enter_Country:
            enter_Country = enter_Country.capitalize()
            country.append(enter_Country)
            idea = False
        else:
            print "only words please" 
            idea = True  
    while idea== False:
        enter_Capitals =raw_input("Enter a Capital: ")
        if enter_Capitals.isalpha() or " " in enter_Capitals:
            enter_Capitals = enter_Capitals.capitalize()
            capitals.append(enter_Capitals)
            idea = True 
        else:
            print "only words please"
            idea = False

    All[enter_Country] = enter_Capitals
    ask()    
    menu()
def Countries():
    limpiar()
    print "Countries"
    print "----------"
    for i in country:
        print i.center(10) 
    raw_input("press enter")
    
    menu()

def Capitals():
    limpiar()
    print "Capitals"
    print "---------"
    for i in capitals:
        print i.center(10) 
    raw_input("press enter")

    menu()
def show_all():
    limpiar()
    print "All the countries and capitals"
    print "-------------------------------"
    print "Countries              Capitals"
    for i in All:
        print i.ljust(15, " ") , All[i].rjust(15, " ")
    raw_input("press enter")
    menu()
def mail():
   print "Send email by gmail"

   fromaddr = raw_input("Count from gmail: ")
   password = getpass.getpass("Password: ")
   toaddrs = raw_input("to: ")
   #asunto = raw_input("subject, from message: ")
   body = "Countries\t===========\tCapitals\n"
   for msg in All:
        body = body + str(msg).center(20) +str(All[msg]).center(20) + "\n" 
   msg = MIMEMultipart()
   msg['From'] = fromaddr #This saves the mail of the sender
   msg['To'] = toaddrs  #This saves the mail of the receiver
   msg['Subject'] = "Countries and Capitals"  #This saves the subject
   msg.attach(MIMEText(body, 'plain')) #This saves the message

   try:
       server = smtplib.SMTP('smtp.gmail.com:587')
       server.starttls()
       server.login(fromaddr,password)
       text = msg.as_string()
       server.sendmail(fromaddr, toaddrs, text)
       server.quit()
       print "yes"
       raw_input("press enter")
   except (smtplib.SMTPAuthenticationError):
       print "No se envio nada"
       raw_input("presione enter")
       mail()
def all_Order():
    limpiar()
    print " ORDERED"
    print "---------"
    ordered = OrderedDict(sorted(All.items(), key=lambda x: x[1:]))
    print "Countries             Capitals"
    for key, value in ordered.items():
        print key.ljust(15, " ") + value.rjust(15, " ")
    raw_input("Press Enter to Continue")
    menu()

def limpiar():
    os.system("reset")
def salir():
    sys.exit()
def menu():
    limpiar() 
    print "______________________________________"
    print "Countries and Capitals"
    print "--------------------------------------"
    print "select a opcion"
    print "--------------------------------------"
    print "! 1. Insert Country                  !"
    print "! 2. Show Country                    !"
    print "! 3. Show Capitals                   !"
    print "! 4. Show all                        !"
    print "! 5. ORDERED                         !"
    print "! 6. MAIL                            !"
    print "! 7. Exit                            !"
    print "!____________________________________!"
    insertmenu = raw_input("Insert a opcion: ")

    if insertmenu == "1" or insertmenu == "insert country" or insertmenu == "Insert Country" or insertmenu == "INSERT COUNTRY":
        add_Country()
    elif insertmenu == "2" or insertmenu == "show country" or insertmenu == "Show Country" or insertmenu == "SHOW COUNTRY":
        Countries()
    elif insertmenu == "3" or insertmenu == "show capitals" or insertmenu == "Show Capitals" or insertmenu ==" SHOW CAPITALS":
        Capitals()
    elif insertmenu == "4" or insertmenu == "show all" or insertmenu == "Show All" or insertmenu == "SHOW ALL":
        show_all()
    elif insertmenu == "5" or insertmenu == "all order" or insertmenu == "All Order" or insertmenu =="ALL ORDER":
        all_Order()
    elif insertmenu == "6" or insertmenu == "MAIl" or insertmenu == "Mail" or insertmenu == "mail":
        mail()
    elif insertmenu == "7" or insertmenu == "exit" or insertmenu == "Exit" or insertmenu == "EXIT":
        salir()
    else:
        raw_input("press enter to continue")
        limpiar()
        menu()            
menu()
