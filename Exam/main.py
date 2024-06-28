import getpass #getpass library is used for inputs when you write in them text doesn't shows up 
import append_to_datas
import time
email = ""
password = ""
email_line = ""
password_line = ""
balance_line = ""
Fullname = ""
old_balance = 0
balance = 0
def Deposit():
    global balance
    Money = input("How much money do you want to deposit: ")
    while not Money.isdigit():
        Money = input("How much money do you want to deposit: ")
    balance = old_balance + int(Money)
    with open("datas.txt") as file:
        z = file.read()
    x = z.replace(email_line + password_line + balance_line,email_line + password_line + "Balance:" + str(balance) + "\n")
    r1 = open("datas.txt", "w")
    r1.write(x)
    r1.close()
    time.sleep(3)
    print("Operation was Succsesful!")
    after()
def Withdraw():
    global balance
    Money = input("How much money do you want to withdraw: ")
    while not Money.isdigit():
        Money = input("How much money do you want to withdraw: ")
    while old_balance < int(Money):
        print("You dont have enough money,try again!")
        Money = input("How much money do you want to withdraw: ")
    balance = old_balance - int(Money)
    with open("datas.txt") as file:
        z = file.read()
    x = z.replace(email_line + password_line + balance_line,email_line + password_line + "Balance:" + str(balance) + "\n")
    r1 = open("datas.txt", "w")
    r1.write(x)
    r1.close()
    time.sleep(3)
    print("Operation was Succsesful!")
    after()
def Transfer_money():
    name = input("Who do you want to transfer money with: ")
    with open("datas.txt") as file:
        r1 = file.read()
    if name not in r1:
        print("We could find person with that name!")
        print("If you want to exit Transfering money press 1.\nIf you want to try again press 2.")
        x = input()
        while x != "1" and x != "2":
            x = input()
        if x == "1":
            after()
        elif x == "2":
            Transfer_money()
    money = input("How much money you want to transfer: ")
    while not money.isdigit():
        print("Enter numeric value!")
        money = input("How much money you want to transfer: ")
    while int(money) > balance:
        print("You don't have enough money!")
        money = input("How much money you want to transfer: ")
    name_line = ""
    pas_line = ""
    bal_line = ""
    mail_line = ""
    bal = 0
    counter = 0
    doc = open("datas.txt")  
    for line in doc:
        if line == "Name:" + name + "\n":
            name_line = line
            counter += 1
        elif line.startswith("Email") and counter:
            mail_line = line
        elif line.startswith("Password") and counter:
            pas_line = line
        elif line.startswith("Balance:") and counter:
            bal_line = line
            bal = int(line[8:-1])
            counter = 0
    ballance = bal + int(money)
    with open("datas.txt") as file:
        z = file.read()
    y = z.replace(mail_line + pas_line + bal_line,mail_line + pas_line + "Balance:" + str(ballance) + "\n")
    r1 = open("datas.txt", "w")
    user_balance = balance - int(money)

    x = y.replace(email_line + password_line + balance_line,email_line + password_line + "Balance:" + str(user_balance) + "\n")
    r1.write(x)
    r1.close()
    time.sleep(3)
    print("succsesfuly sent the money!")
    after()
    
def Settings():
    n_line = ""
    e_line = ""
    p_line = ""
    b_line = ""
    counter = 0
    doc = open("datas.txt")  
    for line in doc:
        if line == "Name:" + Fullname + "\n":
            n_line = line
        if line == "Email:" + email + "\n":
            e_line = line
            counter += 1
        elif line == "Password:" + password + "\n":
            p_line = line
        elif line.startswith("Balance:") and counter:
            b_line = line
            counter = 0
    print("1. Delete account 2. Change password")
    x = input()
    while x != "1" and x != "2":
        x = input()
    match x:
        case "1":
            z = input("You can't undo the changes. You will loose entire account with money if you agree enter 'Y' else 'N':  ")
            while z != "Y" or z!= "N":
                print("Invalid input!")
                z = input("You cann't undo the changes. You will loose entire account with money if you agree enter 'Y' else 'N':  ")
            match z:
                case "Y":
                    with open("datas.txt") as file:
                        z = file.read()
                    x = z.replace(n_line + e_line + p_line + b_line,"" + "\n")
                    r1 = open("datas.txt", "w")
                    r1.write(x)
                    r1.close()
                    print("Sad to see you go😥")
                    time.sleep(3)
                    print("Succesfuly deleted the account!")
                case "N":
                    after()
        case "2":
            old_password = input("Enter your old password: ")
            print(p_line[10:-1])
            while old_password != p_line[10:-1] and old_password != "back":
                old_balance = getpass.getpass("Enter your old password(if you want to exit to main menu enter back) : ")
            if old_password == "back":
                after()
            
            
                
    
def Exit():
    pass
def users():
    doc = open("datas.txt")
    listn = []
    for line in doc:
        if line.startswith("Name"):
            listn.append(line[5:-1])
    if len(listn) == 1:
        print("Our user:")
    else:
        print("Our users:")
    print("\n".join(listn))
def after():

    global password
    global password_line
    global balance_line
    global old_balance
    global email_line
    global balance
    counter = 0
    doc = open("datas.txt")  
    for line in doc:
        if line == "Email:" + email + "\n":
            email_line = line
            counter += 1
        elif line == "Password:" + password + "\n":
            password_line = line
        elif line.startswith("Balance:") and counter:
            balance_line = line
            old_balance = int(line[8:-1])
            balance = int(line[8:-1])
            counter = 0
    print("Your balance: " +str(balance) + "$")
    print("What do you want to do next: ")
    print("1. Deposit\n2. Withdraw\n3. Transfer money\n4. Update account's info\n5. Our users\n6. Exit\n")
    x = input()
    while x != "1" and x!= "2" and x!= "3" and x!= "4" and x!= "5" and "6":
        x = input()
    match x:
        case "1":
            Deposit()
        case "2":
            Withdraw()
        case "3":
            Transfer_money()
        case "4":
            Settings()
        case "5":
            users()
        case "6":
            Exit()
def Login():
    global password
    global email
    global Fullname
    Fullname = input("Enter your fullname: ")
    email = input("Enter your email: ")
    while "@" not in email:
        email = input("Enter your email: ")
    password = getpass.getpass("Enter your password: ")
    x = "Name:" + Fullname + "\n" + "Email:" + email + "\n" + "Password:" + password
    with open("datas.txt") as file:
        z = file.read()
    if x not in z:
        print("We couldn't find your information in our database.")
        print("If you want to login again press 1 and if you want to register press 2.")
        y = input("1. Login\n2. Register\n")
        while y != "1" and y != "2":
            y = input("1. Login\n2. Register\n")
        if y == "1":
            Login()
        elif y == "2":
            Register()
    else:
        print("Succsefuly logged in.")
        after()
    
def Register():
    fullname = input("What's your fullname: ")
    while "1" in fullname or "2" in fullname or "3" in fullname or "4" in fullname or "5" in fullname or "6" in fullname or "7" in fullname or "8" in fullname or "9" in fullname or "0" in fullname:
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
    with open("datas.txt") as file:
        z = file.read()
    if email in z:
        z.close()
        print("Email already in use.")
        print("Try logging in.")
        print("If you want to login press 1 and if you want to try registering again press 2.")
        y = input("1. Login\n2. Register\n")
        while y != "1" and y != "2":
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
print("If you already have an account and you want to login press 1.\nIf you don't have an account and you want to register press 2.")
y = input("1. Login\n2. Register\n")
while y != "1" and y != "2":
    y = input("1. Login\n2. Register\n")
if y == "1":
    Login()
elif y == "2":
    Register()





