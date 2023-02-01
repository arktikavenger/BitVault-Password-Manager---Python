# TODO: Password generator
import nacl.secret
import nacl.utils
import nacl.pwhash
import base64

print("Welcome to BitVault, the simple and secure password manager for everyone!")


signup_prompt = input("Is it your first time using BitVault? ")

if signup_prompt.lower() == "yes":
    user_list = []
    new_un = input("Please enter a username: ")
    new_pw = input("Please enter a password: ")
    user_list.append(new_un + " " + new_pw)
    with open(r'UserList.txt', 'a') as ul:  
        ul.write(str(user_list[0]))
        pass

if signup_prompt.lower() == "no":
    k = 1
    while k < 2:
            user_list2 = []
            user = input("Please enter your username: ")
            pass_ = input("Please enter your password: ")
            user_list2.append([user, pass_])
            a = open(r'.\UserList.txt', 'r')
            ultext = a.read()
            
            if user and pass_ in ultext:
                print("Logging in...")
                p = pass_
                break
                k += 1
            if user or pass_ not in ultext:
                print("Username or Password incorrect. Please try again.")


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

