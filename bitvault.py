# TODO: Password generator
import json

print("Welcome to BitVault, the simple and secure password manager for everyone!")


signup_prompt = input("Is it your first time using BitVault? ")

if signup_prompt.lower() == "yes":
    user_list = []
    new_un = input("Please enter a username: ")
    new_pw = input("Please enter a password: ")
    user_list.append(new_un + " " + new_pw)
    with open(r'C:\Users\steve\Coding\PasswordManager\UserList.txt', 'a') as ul:
        ul.write(str(user_list[0]))
        ul.close()

if signup_prompt.lower() == "no":
    k = 1
    while k < 2:
            user_list2 = []
            user = input("Please enter your username: ")
            pass_ = input("Please enter your password: ")
            user_list2.append([user, pass_])
            p = pass_
            a = open(r'.\UserList.txt', 'r')
            ultext = a.read()
            
            if user and pass_ in ultext:
                print("Logging in...")
                break
                k += 1
            if user or pass_ not in ultext:
                print("Username or Password incorrect. Please try again.")
                    

#readlines() turns txt file into list, len determines number of lines

use = input("Would you like to add a password or retrieve a password? " )

if use.lower() == "add a password":
    print("Type 'quit' and click enter on the first question to end the process.")

    pwList = [
    ]

    i = 1
    while i < 2:
        accType = input("What is the name of the application? ")
        if accType.lower() == "quit":
            break
            i += 1
        un = input("Enter your username: " )
        pw = input("Enter your password: " )
        pwList.append([accType, un, pw])


    with open(r'C:\Users\steve\Coding\PasswordManager\PWList.txt', 'a') as fp:
        for list in pwList:
            fp.write(str(pwList[0]) + "\n")
            fp.close()

#in progress
if use.lower() == "retrieve a password":
    access = input("Please enter your master password to access passwords: ")
    if access != p:
        print("Access Denied.")
        quit()
    else: 
        print("Access Granted!")
    retrieve = input("Would you like to access all passwords or a specific password?")


