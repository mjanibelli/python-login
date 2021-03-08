import json
filename = "login.json"


def load_users():
    """Loads users dict."""
    try:
        with open(filename) as file:
            info = json.load(file)
    except FileNotFoundError:
        return None
    else:    
        return info


def save_users(user, password):
    """Save user's info. (Username and password.)."""
    users = load_users()

    if users:
        users[user] = password
        with open(filename, "w") as file:
            json.dump(users, file)
    else:
        users = {user:password}
        with open(filename, "w") as file:
            json.dump(users, file)


def signup():
    new_user = input("Type your username: ")
    new_password = input("Type your password: ")
    save_users(new_user, new_password)


def signin():
    users = load_users()
    user_entry = input("Username: ")

    if user_entry in users.keys():
        password_entry = input("Password: ")
        if password_entry == users[user_entry]:
            print(f"Welcome back, {user_entry}!")
 

