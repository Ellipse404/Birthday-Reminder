# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 21:01:49 2020

@author: BHASKAR NEOGI
"""

try :
    dict = {}
    while True :
        print('''
                    ---------- BIRTHDAY REMINDER ----------''')
        print('''              1. Show Birthday
                  2. Add to Birthday List
                  3. Exit ''')
        choice = int(input("Enter The Choice : "))
        if choice == 1 :
            if len(dict.keys()) == 0 :
                print("Nothing To Show")
            else :
                name = input("Enter Name to Look For Bithday : ")
                birthday = dict.get(name, "No Data Found !!")
                print(birthday)
                
        elif choice == 2 :
            name = input("Enter Name : ")
            month = input("Enter Month : ")
            date = int(input("Enter Date : "))
            if date == 1 :
                suff = 'st'
            elif date == 2 :
                suff = 'nd'
            elif date == 3 :
                suff = 'rd'
            else :
                suff = 'th'
            b_date = str(date) + suff + ' ' + month
            dict[name] = b_date
            print("Bithday Added . ")
            
        elif choice == 3 :
            break
        else :
            print("Choose a Valid Option !!")
            
except ValueError :
    print("Please Type Correctly !")
except SyntaxError :
    print("Check For Unexpected Syntax !")    
