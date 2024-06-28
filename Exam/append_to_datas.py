def append(fullname,email,password):
    r1 = open("datas.txt","a")
    r1.write("Name:" + fullname + "\n" + "Email:" + email + "\n" "Password:" + password + "\n" "Balance:0" + "\n")
    r1.close()