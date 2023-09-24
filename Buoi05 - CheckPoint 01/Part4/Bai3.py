print("== Registration ==", end='\n\n')
user_name = input("Username: ")
print()
password = input("Password: ")
while len(password) <= 8 and password.isalnum():
    print("Invalid password. Please input again.")
    password = input("Password: ")
repeat_password = input("Repeat password: ")

while repeat_password != password:
    print("Passwords not match. Please input again.")
    repeat_password = input("Repeat password: ")

print()
email = input("Email: ")
while email.__contains__("@") == False or email.__contains__(".") == False:
    print("Invalid email. Please input again.")
    email = input("Email: ")
print()
print("Registered successfully.")