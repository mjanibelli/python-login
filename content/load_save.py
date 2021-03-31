import json

filename = "login.json"


def loadUsers():
    """If the file exists, loads it and returns the users dict."""
    try:
        with open(filename) as file:
            info = json.load(file)
    except FileNotFoundError:
        return None
    else:    
        return info
    

def saveUser(user, password):
    """Save user's info. (Username and password.)."""
    users = loadUsers()

    if users:
        users[user] = password
        with open(filename, "w") as file:
            json.dump(users, file, sort_keys=True, indent=4)
    else:
        users = {user:password}
        with open(filename, "w") as file:
            json.dump(users, file, sort_keys=True, indent=4)