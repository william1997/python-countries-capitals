# Aqui escribe tu codigo

import os
import sys
from collections import OrderedDict
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
            country.append(enter_Country)
            idea = False
        else:
            print "only words please" 
            idea = True  
    while idea== False:
        enter_Capitals =raw_input("Enter a Capital: ")
        if enter_Capitals.isalpha() or " " in enter_Capitals:
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
    for i in country:
        print "Countries"
        print i.center(10) 
    raw_input("press enter")
    
    menu()

def Capitals():
    limpiar()
    for i in capitals:
        print "Capitals"
        print i.center(10) 
    raw_input("press enter")

    menu()
def show_all():
    limpiar()
    for i in All:
        print "Countries              Capitals"
        print i.ljust(15, " ") , All[i].rjust(15, " ")
    raw_input("press enter")
    menu()
def mail():
    pass
def all_Order():
    limpiar()
    ordered = OrderedDict(sorted(All.items(), key=lambda x: x[1:]))
    for key, value in ordered.items():
        print "Countries             Capitals"
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
