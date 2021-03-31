import bcrypt
import load_save, inputs


def signUp():
    """Create a new user."""
    new_user = inputs.inputNewUsername()
    new_password = inputs.inputNewPassword()
    load_save.saveUser(new_user, new_password)
    print("Your account has been successfully created.")


def signIn():
    """Sign in."""
    users = load_save.loadUsers()
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