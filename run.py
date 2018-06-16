#!/usr/bin/env python3.6
from newpasslock import Pword, Login #Import the login and Pword class

def new_account (username, email, password):
    '''
    Function to create new account
    '''
    new_user=Login(username, email, password)
    return new_user

def usercreation(user):
    '''
    Function that stores user credentials
    '''
    user.usercreation()

def verify(username, passkey):
    '''
    Function that verifies and enables login
    '''
    return Login.verify(username, passkey)

def my_new_data(userid, webkey, website):
    '''
    This is a function that creates data for storing password
    '''
    new_data=Login(userid, webkey, website):
    return new_data

def add_data(data):
    '''
    This is a function that saves the new data created
    '''
    data.add_password()

use 
def dispay_data(data, number):
    '''
    This is a function that displays the user data
    '''
    return Login.display_data(data, number)

def data_existing(data):
    '''
    This is a function that checks if user data exists
    '''
    return Login.existing_data(data)

def password_generator(count):
    '''
    This is a function that generates a password
    '''
    pass_list=[]
    round=1
    while round<=count:
        gen_password = random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase )
        pass_list.append(gen_password)
        round+=1
    return ''.join(pass_list)

def copy_password(number,count):
    '''
    This is a function that copies the password to the clipboard
    '''
    Login.copy_password(number,count)
    
def main():
    '''
    Main function
    '''
    my_username=0

    entries=[]
    #print (password_generator)
    print("\n")
    print("How are you? Welcome to you password locker app")
    while True:
        print("Insert:\n nu to create new account\n li to log in\n lu to exit")
        welcome_text=input().lower().strip()
        if welcome_text=="nu":
            print("Create account to continue:"+"\n"+"_"*25+"\n Enter Username:")
            my_username=input("New Username")
            print("Enter password: ")
            my_password=input("New Password: ")
