import os
import hashlib
import time

print("Welcome to the SPM Setup!\nLet's get started!")
info = input("Would you like a bit of info on how secure this SPM is?")
if info == "yes":
    print("We use sha3-512 hashing to protect your passwords.")
    print("OK! Time to set your Master Password!")
    master_password = input("What do you choose to be your Master Password?")
    master_password_encoded = master_password.encode("utf-8")
    master_password = None
    master_password_encoded_hashed = hashlib.sha3_512(master_password_encoded)
    master_password_encoded_hashed_hexdigested = master_password_encoded_hashed.hexdigest()
    open("master_password.txt", "w").write(master_password_encoded_hashed_hexdigested)
    print("Done with creating your Master Password")
    time.sleep(4.5)
else:
    print("OK! Time to set your Master Password!")
    master_password = input("What do you choose to be your Master Password?")
    master_password_encoded = master_password.encode("utf-8")
    master_password = None
    master_password_encoded_hashed = hashlib.sha3_512(master_password_encoded)
    master_password_encoded_hashed_hexdigested = master_password_encoded_hashed.hexdigest()
    open("master_password.txt", "w").write(master_password_encoded_hashed_hexdigested)
    print("Done with creating your Master Password")
    open("main.py", "w").write("""import hashlib, json

print("Welcome to SPM \nYour Secure Password Manager!")
master_password = input("What is your MASTER PASSWORD? (If this is your first time just hit \"enter\" ")
master_password_encoded = master_password.encode("utf-8")
master_password = None
master_password_encoded_hashed = hashlib.sha3_512(master_password_encoded)
master_password_encoded = None
master_password_encoded_hashed_hexdigested = master_password_encoded_hashed.hexdigest()
master_password_encoded_hashed = None
real_master_password_hashed_hexdigested = open("master_password.txt", "rt").read()
if master_password_encoded_hashed_hexdigested is real_master_password_hashed_hexdigested:
    print("You can: Recall a password - Just say "find the password for [website]" it will give you the password and" 
    "username")
    print("Also you can add a password by editing passwords.txt")
    action = input("What would you like to do?")
""")
    time.sleep(3.5)
