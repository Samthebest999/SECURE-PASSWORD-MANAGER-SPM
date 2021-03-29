import hashlib
import json
print("Welcome to SPM \nYour Secure Password Manager!")
master_password = input("What is your MASTER PASSWORD?")
master_password_encoded = master_password.encode("utf-8")
master_password = None
master_password_encoded_hashed = hashlib.sha3_512(master_password_encoded)
master_password_encoded = None
master_password_encoded_hashed_hexdigested = master_password_encoded_hashed.hexdigest()
master_password_encoded_hashed = None
real_master_password_hashed_hexdigested = open("master_password.txt", "rt").read()
if master_password_encoded_hashed_hexdigested is real_master_password_hashed_hexdigested:
    master_password_hashed_hexdigested = None
    real_master_password_hashed_hexdigested = None
    print("You can: Recall a password - Just say \"find details\" it will give you the password and"
          "username")
    print("Also you can add login details by using this guide")
    action = input("What would you like to do?")
    if action == "find details":
        contents = open(".env", "r")
        password_dict = json.loads(contents)
        contents = None
        website = input("Which website would you like to pull up details for??")
        print(password_dict[website])
        password_dict = None