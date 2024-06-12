def handleLogin():
    print("Enter your login details")
    userName = input("Enter your user-name:")
    password = input("Enter your password:")
    print("Logged-in Successfully")
 
def handleSignup():
    print("Enter your details to create an account")
    fullName = input("Enter your full-name:")
    userName = input("Enter your user-name:")
    password = input("Enter your password:")
    print("Account created Successfully")
 
 
while True:
    print("-----------------------------------------------------")
    print("1 - Login")
    print("2 - Singup")
    print("3 - Exit")
    option = int(input("Choose the option:"))
    print("-----------------------------------------------------")
 
    if option == 1: 
        handleLogin() 
    elif option == 2:
        handleSignup()
    else:
        print("Thanks for using Instagram")
        exit(0)
    