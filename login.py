import login_functions

print(" Welcome to Python Login! ".center(48, "="))
check = input("Do you have an account?[y/n]: ")

while check[0].lower() != "y" and check[0].lower() != "n":
    print("This option does not exist! Try again...")
    check = input("Do you have an account?[y/n]: ")
if check[0].lower() == "y":
    login_functions.signin()
if check[0].lower() == "n":
    login_functions.signup()
