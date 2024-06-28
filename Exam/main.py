import getpass
import append_to_datas
import time

def Login():
    email = input("Enter your email: ")
    while "@" not in email:
        email = input("Enter your email: ")
    password = getpass.getpass("Enter your password: ")
    while len(password) <=5:
        print("Your entered password is to small, try again!")
        password = getpass.getpass("Enter your password: ")
    x = "Email:" + email + "\n" + "Password:" + password + "\n"
    z = open("datas.txt")
    if x not in z:
        print("We couldn't find your information in our database.")
        print("If you want to login again press 1 and if you want to register press 2.")
        y = input("1. Login\n2. Register\n")
        while y != "1" or y != "2":
            y = input("1. Login\n2. Register\n")
        if y == "1":
            Login()
        elif y == "2":
            Register()
    else:
        print("Succsefuly logged in.")
    
def Register():
    fullname = input("What's your fullname: ")
    while "1" in name or "2" in name or "3" in name or "4" in name or "5" in name or "6" in name or "7" in name or "8" in name or "9" in name or "0" in name:
        name = input("What's your real fullname: ")
    email = input("Enter your email: ")
    while "@" not in email:
        email = input("Enter your email: ")
    password = getpass.getpass("Enter your password: ")
    while len(password) <=5:
        print("Your entered password is to small, try again!")
        password = getpass.getpass("Enter your password: ")
    password2 = getpass.getpass("Confirm your password: ")
    while password2 != password:
        print("Enter exact password you entered previously!")
        password2 = getpass.getpass("Confirm your password: ")
    z = open("datas.txt")
    if email in z:
        z.close()
        print("Email already in use.")
        print("Try logging in.")
        print("If you want to login press 1 and if you want to try registering again press 2.")
        y = input("1. Login\n2. Register\n")
        while y != "1" or y != "2":
            y = input("1. Login\n2. Register\n")
        if y == "1":
            Login()
        elif y == "2":
            Register()
    else:
        append_to_datas.append(fullname,email,password)
        print("Succsesfuly registered!")
        print("Now you can login.")
        Login()
print("Welcome to MyBank!")
print("If you arleady have an account and you want to login press 1.\nIf you don't have an account and you want to register press 2.")
y = input("1. Login\n2. Register\n")
while y != "1" and y != "2":
    y = input("1. Login\n2. Register\n")
if y == "1":
    Login()
elif y == "2":
    Register()
