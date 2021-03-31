import re, bcrypt
from load_save import loadUsers


def checkPassword(password):
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


def inputNewUsername():
    """Allows the username input and checks if it's already in use."""
    users = loadUsers()
    new_user = input("Type your username: ")

    if users:
        while new_user in users.keys():
            print("This username is already in use! Try again.")
            return inputNewUsername()
    return new_user


def inputNewPassword():
    """Allows the password input and checks if it's valid or not."""
    new_password = input("Type your password: ")

    if checkPassword(new_password):
        password_check = input("Type your password again: ")
        while password_check != new_password: 
            print("Passwords doesn't match! Try again.")
            return inputNewPassword()
        hashed_password = bcrypt.hashpw(new_password.encode("utf-8"), bcrypt.gensalt())
        return hashed_password.decode("utf-8")
    else:
        print("Your password needs to be stronger! (At least 1 number, 1 capital letter and 1 special character)")
        return inputNewPassword()