# Register
# - first names,last names, password, email
# - generate the user account

# login
# - Account number email and Password

# bank Operations
# Initializing the system
import random

database = {} #dictionary

def init():

    isValidOptionSelected = False
    print("Welcome to Bank PHP")

    while isValidOptionSelected == False:

        haveAccount = int(input("Do you have account with us : 1. (yes) 2. (no)\n"))
        if(haveAccount == 1):
            isValidOptionSelected = True
            login()
        elif(haveAccount == 2):
            isValidOptionSelected = True
            register()
        else:
            print("You have selected invalid option")



def login():
    print('this is the login function')


def register():

    print("************Kindly register with our bank*************")

    email = input("What is your email address? \n")
    print(email)
    first_name = input("What is your first name? \n")
    print(first_name)
    last_name = input("What is your last name? \n")
    print(last_name)
    password = input("create your password? \n")
    print(password)
    accountNumber = generationAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password ]

    return database

def bankOperation():
    print("Bank Operations")

def withdrawalOperational():
    print("withdrawal")

def depositOperational():
    print("Deposits Operations")

def generationAccountNumber():

    print("account number generator")
    return random.randrange(0000000000,9999999999)


### ACTUAL BANKING SYSTEM

init()