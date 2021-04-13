import json

filename = "login.json"


def load_users():
    """If the file exists, loads it and returns the users dict."""
    try:
        with open(filename) as file:
            info = json.load(file)
    except FileNotFoundError:
        return None
    else:    
        return info
    

def save_user(user, password):
    """Save user's info. (Username and password.)."""
    users = load_users()

    if users:
        users[user] = password
        with open(filename, "w") as file:
            json.dump(users, file, sort_keys=True, indent=4)
    else:
        users = {user: password}
        with open(filename, "w") as file:
            json.dump(users, file, sort_keys=True, indent=4)
