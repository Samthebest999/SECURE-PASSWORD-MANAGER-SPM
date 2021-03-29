import json
masterpassword = open(".env", "r").read()
master_dict = json.loads(masterpassword)
print(master_dict["google.com"])