import json
import re
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
            json.dump(users, file)
    else:
        users = {user:password}
        with open(filename, "w") as file:
            json.dump(users, file)


def input_new_username():
    """Allows the username input and checks if it's already in use."""
    users = load_users()
    new_user = input("Type your username: ")
    if users:
        while new_user in users.keys():
            print("This username is already in use! Try again.")
            return input_new_username()
    return new_user


def check_password(password):
    """Checks if the password is safe enough (At least 1 number, 1 capital letter and 1 special character)."""
    cap_letter_regex = re.compile(r"[A-Z]+")
    cap_letter_found = re.search(cap_letter_regex, password)

    number_regex = re.compile(r"\d+")
    number_found = re.search(number_regex, password)

    spec_charac_regex = re.compile(r"\W+")
    spec_charac_found = re.search(spec_charac_regex, password)

    if cap_letter_found and number_found and spec_charac_found:
        return True
    else:
        return False

def input_new_password():
    """Allows the password input and checks if it's valid or not."""
    new_password = input("Type your password: ")
    if check_password(new_password):
        password_check = input("Type your password again: ")
        while password_check != new_password: 
            print("Passwords doesn't match! Try again.")
            return input_new_password()
        return new_password
    else:
        print("Your password needs to be stronger! (At least 1 number, 1 capital letter and 1 special character)")
        return input_new_password()
        

def signup():
    """Create a new user."""
    new_user = input_new_username()
    new_password = input_new_password()
    save_user(new_user, new_password)
    print("Your account has been successfully created.")


def signin():
    """Sign in."""
    users = load_users()
    chances = 3
    user_entry = input("Username: ")

    if user_entry in users.keys():
        password_entry = input("Password: ")
        chances -= 1
        while chances > 0 and password_entry != users[user_entry]:
            print("Wrong password! Try again: ")
            password_entry = input("Password: ")
            chances -= 1
        if password_entry == users[user_entry]:
            print(f"Welcome back, {user_entry}!")
        if chances == 0: 
            print("You have exceeded the limit of login attempts.")
    else:
        print("This user isn't saved yet! Try again.")
        