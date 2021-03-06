#!/usr/bin/env python
import os
import getpass
import bank_db

def withdraw(acct,database):
    print ("\nYour balance is: {}".format(database.get_balance(acct)))
    while True:
        amt=float(raw_input("How much $$?:"))
        if database.get_balance(acct) - amt >= 0.0 and amt > 0:                
            print("\nPrevious balance: {}".format(database.get_balance(acct)))
            database.set_balance(acct, database.get_balance(acct) - amt)  
            print("\nCurrent balance: {}".format(database.get_balance(acct))) 
            return
        else:
            print("Try again.")
                
def deposit(acct,database):
    print ("\nYour balance is: {}".format(database.get_balance(acct)))
    while True:
        amt=float(raw_input("How much are you depositing today?:"))
        if amt > 0.0:                
            print("\nPrevious balance: {}".format(database.get_balance(acct)))
            database.set_balance(acct,database.get_balance(acct) + amt)  
            print("\nCurrent balance: {}".format(database.get_balance(acct))) 
            return
        else:
            print("Enter an amount greater than 0.")

def quickcash(acct,database):
    print ("\nYour balance is: {}".format(database.get_balance(acct)))

    if database.get_balance(acct) - 40.0 >= 0.0:                
        print("\nPrevious balance: {}".format(database.get_balance(acct)))
        database.set_balance(acct, database.get_balance(acct) - 40.0)
        print("\nCurrent balance: {}".format(database.get_balance(acct))) 
        return
    else:
        print("Insufficient funds.")

def access_account(acct,database):
    
    
    print ("\n\n\nHello {}\n".format(database.get_name(acct)))

    while True:
        valid_selection = False
        print("|=============================================|")
        print("|1:Print balance..............................|")
        print("|2:Withdraw...................................|")
        print("|3:Deposit....................................|")
        print("|4:Fast  Cash.................................|")
        print("|5:Exit.......................................|")
        print("|=============================================|")
        while not valid_selection:
            selection=raw_input("Please make a selection:")
            selection = int(selection)
            if selection in [1,2,3,4,5]:
                valid_selection = True
        
        if selection==1:
            #print balance
            print ("\nYour balance is: {}".format(database.get_balance(acct)))
        elif selection==2:
            #withdraw
            withdraw(acct,database)
        elif selection==3:
            #deposit
            deposit(acct,database)
        elif selection==4:   
            #quick cash
            quickcash(acct,database)
        elif selection==5:
            #exit
            return
   

#def print_balance(selection):
    

def get_user(database):

    valid_user = False
    os.system("clear")
    os.system("sleep 1")

    print("Welcome to my ATM machine where there are no fees")
    while not valid_user:
        acct=raw_input("Please enter your 4 digit account number:")
        pin=getpass.getpass("Please enter your 4 digit pin number:")
        valid_user = database.validate_user(int(acct),int(pin))
        
        if valid_user == False:
            print("That is not a valid account.. please try again")
    return int(acct)


def main():
    filename = 'accounts'
    #database = bank_db.PickleBankDatabase(filename)
    database = bank_db.SqlBankDatabase("first_tech")
    while True: 
        acct=get_user(database)
        access_account(acct,database)
        
main()


