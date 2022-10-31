import json
def fileread(filename):
    user = open(filename, "r")
    final_user = user.read()
    print(final_user)




x = fileread("info.json")