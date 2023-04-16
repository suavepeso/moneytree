import re


username = input("Enter username: ")
password = input("Enter password: ")


if not re.search(r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$", password):
    print("Password should contain at least one uppercase letter, one special symbol, and one number.")
else:
   
    with open("accounts.txt", "a") as f:
        f.write(f"{username}:{password}\n")

    
    print("You have successfully made an account.")


print("Username:", username)
print("Password:", password)

