import login_functions

print(" Welcome to Python Login! ".center(48, "="))
check = input("Do you have an account?[y/n]: ")

while check[0].lower() != "y" and check[0].lower() != "n":
    print("This option does not exist! Try again...")
    check = input("Do you have an account?[y/n]: ")

if check[0].lower() == "y":
    if login_functions.load_users():
        login_functions.signin()
    else:
        print("No users have been saved yet. Try creating a new account.")
        login_functions.signup()
if check[0].lower() == "n":
    login_functions.signup()
