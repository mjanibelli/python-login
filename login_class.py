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
    """Create a new user."""
    new_user = input("Type your username: ")
    new_password = input("Type your password: ")
    password_check = input("Type your password again: ")
    while password_check != new_password:
        print("Passowords doesn't match! Try again.")
        new_password = input("Type your password: ")
        password_check = input("Type your password again: ")
    save_users(new_user, new_password)
    print("Your account has been successfully saved!")


def signin():
    """Makes the login."""
    users = load_users()
    user_entry = input("Username: ")

    if user_entry in users.keys():
        password_entry = input("Password: ")
        if password_entry == users[user_entry]:
            print(f"Welcome back, {user_entry}!")
 

