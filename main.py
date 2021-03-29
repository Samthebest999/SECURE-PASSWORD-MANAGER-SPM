import hashlib

print("Welcome to SPM \nYour Secure Password Manager")
master_password = input("What is your MASTER PASSWORD? (If this is your first time just hit \"enter\" ")
master_password_encoded = master_password.encode("utf-8")
master_password = None
master_password_encoded_hashed = hashlib.sha3_512(master_password_encoded)
master_password_encoded = None
master_password_encoded_hashed_hexdigested = master_password_encoded_hashed.hexdigest()
master_password_encoded_hashed = None
real_master_password_hashed_hexdigested = open("master_password.txt", "rt").read()
if master_password_encoded_hashed_hexdigested is real_master_password_hashed_hexdigested:
    setup = input("Would you like to go through the setup process? ")
    if setup == "yes":
        import os

        os.system("python setup.py")
else:
    import time

    print("You can't use this program without the setup process")
    time.sleep(2.55)
