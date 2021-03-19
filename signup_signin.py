import bcrypt
import load_save, inputs


def signup():
    """Create a new user."""
    new_user = inputs.input_new_username()
    new_password = inputs.input_new_password()
    load_save.save_user(new_user, new_password)
    print("Your account has been successfully created.")


def signin():
    """Sign in."""
    users = load_save.load_users()
    chances = 3
    user_entry = input("Username: ")

    if user_entry in users.keys():
        password_entry = input("Password: ")
        chances -= 1
        while chances > 0 and not bcrypt.checkpw(password_entry.encode("utf-8"), users[user_entry].encode("utf-8")):
            print("Wrong password! Try again: ")
            password_entry = input("Password: ")
            chances -= 1
        if bcrypt.checkpw(password_entry.encode("utf-8"), users[user_entry].encode("utf-8")):
            print(f"Welcome back, {user_entry}!")
        if chances == 0: 
            print("You have exceeded the limit of login attempts.")
    else:
        print("This user doesn't exist! Try again.")