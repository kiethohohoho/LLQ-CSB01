print("== Registration ==", end='\n\n')
user_name = input("Username: ")
print()
password = input("Password: ")
repeat_password = input("Repeat password: ")

while repeat_password != password:
    print("Passwords not match. Please input again.")
    repeat_password = input("Repeat password: ")

print()
email = input("Email: ")
print()
print("Registered successfully.")