import json
def fileread(filename):
    user = open(filename, "r")
    final_user = user.read()
    print(final_user)
    convertjson = json.loads(final_user)
    x = {
        "name":"Bless Okafor",
        "email":"xyz@bob.com",
        "age":20,
        "profession":" UI/UX designer"
    }
    convertjson["bles665"] = x
    print(convertjson)
    


x = fileread("info.json")