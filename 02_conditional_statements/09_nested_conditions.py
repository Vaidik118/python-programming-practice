username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "1234":
        print("Login successful")

        role = input("Enter role (admin/user): ").lower()

        if role == "admin":
            print("You have admin access.")
        elif role == "user":
            print("You have user access.")
        else:
            print("Invalid role.")
    else:
        print("Incorrect password.")
else:
    print("Unknown username.")