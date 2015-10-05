# Aqui escribe tu codigo

import os
import sys

All={}
country=[]
capitals=[]
def menu():
    limpiar()
    print "Countries and Capitals"
    print "select a opcion"
    print "1.) Insert Country"
    print "2.) Show Countries "
    print "3.) Show Capitals "
    print "4.) Show all"
    print "5.) Exit"
    menu = raw_input("Insert a opcion: ")

    if menu == "1":
        add_Country()
    elif menu == "2":
        Countries()
    elif menu == "3":
        Capitals()
    elif menu == "4":
        show_all()
    elif menu == "5":
        salir()
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
        enter_Country =raw_input("Enter a Country: ")
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
        print i 
        
    raw_input("press enter")
    
    menu()

def Capitals():
    limpiar()
    for i in capitals:
        print i 
    raw_input("press enter")

    menu()
def show_all():
    limpiar()
    for i in All:
        print i , All[i]
    raw_input("press enter")

    menu()
def limpiar():
    os.system("reset")
def salir():
    sys.exit()
           
menu()
