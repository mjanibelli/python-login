import signup_signin, load_save

print(" Welcome to Python Login! ".center(48, "="))
check = input("Do you have an account?[y/n]: ")

while check[0].lower() != "y" and check[0].lower() != "n":
    print("This option does not exist! Try again...")
    check = input("Do you have an account?[y/n]: ")

if check[0].lower() == "y":
    if load_save.load_users():
        signup_signin.sign_in()
    else:
        print("No users have been saved yet. Try creating a new account.")
        signup_signin.sign_up()
if check[0].lower() == "n":
    signup_signin.sign_up()
