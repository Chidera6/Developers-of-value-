import json
def fileread(filename):
    user = open(filename, "r")
    final_user = user.read()
    convertjson = json.loads(final_user)
    x = {
        "name":"Bless Okafor",
        "email":"xyz@bob.com",
        "age":20,
        "profession":" UI/UX designer"
    }
    convertjson["bles665"] = x
    user.close()
    return f"The json format is\n\n {final_user}\n\n and when converted to Python is \n\n{convertjson}."


x = fileread("info.json")
print(x)