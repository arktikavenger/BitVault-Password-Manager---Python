# TODO: Password generator
# import nacl.secret
#import nacl.utils
# import nacl.pwhash
#import nacl.hashlib
# import base64
import json
# import PySimpleGUI as sg  # Added GUI library for further development
import os

### The libraries hashed out above are not working or broken and should not be used unitl the encryption
### file is complete or in alpha 0.0.2

print("Welcome to BitVault, the free, open-source, and secure password manager for everyone!")

signup_prompt = input("Is it your first time using BitVault? ")


def create_userList():
    if os.path.exists('userlist.json'):
        return
    else:
        with open('userlist.json', 'w') as fc:
            json.dump({}, fc)
            return


create_userList()


def get_userlist():
    with open('userlist.json', 'rt') as f:
        return json.load(f)


def check_userlist(username):
    userfile = get_userlist()
    if username in userfile.keys():
        return True
    else:
        return False


def check_password(username, password):
    userfile = get_userlist()
    if check_userlist(username):
        if userfile[username] == password:
            return True
        else:
            return False
    else:
        return False


def update_userlist(username, password):
    userfile = get_userlist()
    if check_userlist(username):
        return False
    else:
        userfile[username] = password
        with open('userlist.json', 'wt') as f:
            json.dump(userfile, f)
        return True


if signup_prompt.lower()[0] == "y":
    new_un = input("Please enter a username: ")
    new_pw = input("Please enter a password: ")
    if update_userlist(new_un, new_pw):
        print("Username added!")
    else:
        print("Username already exists!")

if signup_prompt.lower()[0] == "n":
    for i in range(0, 3):
        un = input("Please enter your username: ")
        pw = input("Please enter your password: ")
        if check_userlist(un):
            if check_password(un, pw):
                print("Login successful...")
                p = pw
                break
            else:
                print("Incorrect password")
        else:
            print("User does not exist")
    else:
        print("Maximum login attempts exceeded")
        quit()

use = input("Would you like to add a password or retrieve a password? ")

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
        un = input("Enter your username: ")
        pw = input("Enter your password: ")
        pwList.append([accType, un, pw])

    with open(r'C:\Users\steve\Coding\PasswordManager\PWList.txt', 'a') as fp:
        for list in pwList:
            fp.write(str(pwList[0]) + "\n")
            fp.close()

# in progress
if use.lower() == "retrieve a password":
    access = input("Please enter your master password to access passwords: ")
    if access != p:
        print("Access Denied.")
        quit()
    else:
        print("Access Granted!")
    retrieve = input("Would you like to access all passwords or a specific password?")

'''
password = b"I like Python"
secret_msg = b"Actually, I prefer Javascript..."

# Generate the key:
kdf = nacl.pwhash.argon2i.kdf # our key derivation function
salt_size = nacl.pwhash.argon2i.SALTBYTES # The salt musts have a size of 16 bytes
salt = nacl.utils.random(salt_size) # can be sth like: b'3\xba\x8f\r]\x1c\xcbOsU\x12\xb6\x9c(\xcb\x94'
print(salt) # To decrypt the data later, you have to save this salt somewhere.
key = kdf(nacl.secret.SecretBox.KEY_SIZE, password, salt)

# Encrypt the data:
box = nacl.secret.SecretBox(key)
encrypted = box.encrypt(secret_msg)

# Store the data with binary mode:
with open('file.bin', 'wb') as f:
  f.write(encrypted)

# Store the data with text mode:
with open('file.txt', 'w') as f:
  content = base64.b64encode(encrypted).decode("ascii")
f.write(content)
'''
