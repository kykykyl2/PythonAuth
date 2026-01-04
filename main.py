from auth.user import create_user, authenticate_user, delete_account

while True :
    print("1. New account")
    print("2. Login")
    print("3. Delete account")
    print ("4. Exit")

    choice = input("Select an option: ")
    if choice == "1":
        username = input("Enter a new username: ")
        password = input("Enter a new password: ")
        # Here you would call the create_user function
        create_user(username, password)

    elif choice == "2":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        # Here you would call the authenticate_user function
        authenticate_user(username, password)
    elif choice == "3":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        delete_account(username, password)
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please try again.")