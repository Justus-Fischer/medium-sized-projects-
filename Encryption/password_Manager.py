#just a demo 
#Do not use for real passwords 

from ast import While
import random
import secrets

print("JUST A DEMO - DO NOT USE FOR REAL SENSITIVE DATA!")

def bu(num):
    word = []
    for i in range(num):
        sp = chr(random.randint(0, 130))
        while not sp.isprintable():
            sp = chr(random.randint(0, 130))
    
        word.append(sp)
    return "".join(word)

def zkv(wert):
    wert = wert % 0x110000  
    if 0xD800 <= wert <= 0xDFFF:  
        wert = wert + 2048  
    return wert

def zke(wert):
    wert = wert % 0x110000  
    if 0xD800 <= wert <= 0xDFFF:  
        wert = wert - 2048  
    return wert % 0x110000

def seedgen(pasw):
    stes = 5381
    
    bpasw = list(pasw)
    
    for i in range(len(bpasw)):
        stes = int((stes * 33) + ord(bpasw[i]))
        
    return stes % (2**64)

def crypto(mes,mode):
    
    if mode == 1:
        bmes = list(mes) 
        random.seed(seedgen(key)+iv)
        for i in range (len(bmes)):
            bmes[i] = ord(bmes[i])
            try:
                if i > 0:
                    bmes[i] = chr(zkv(bmes[i] + random.randint(100, 100000) - ord(bmes[i-1])*10))
                    
                else:
                    bmes[i] = chr(zkv(bmes[i] + random.randint(100, 100000)*iv))
                    
            except:
                print("unexpected error")
                break
    else:
        ivT = mes[:6]
        re = geheimtext = mes[6:]
        bmes = list(re)
        cbmes = list(re)
        random.seed(seedgen(key)+int(ivT))
        for i in range (len(bmes)):
            bmes[i] = ord(bmes[i])
            try:
                if i > 0:
                    bmes[i] = chr(zke(bmes[i] - random.randint(100, 100000) + ord(cbmes[i-1])*10))
                    
                else:
                    bmes[i] = chr(zke(bmes[i] - random.randint(100, 100000)*int(ivT)))
                    
            except:
                print("invalid password")
                break
    try:
        return "".join(bmes)
    except:
        print("Please try again")
    
            

passwords = []

usernames = []

companies = []

def print_everything():
    print("Usernames:")
    for username in usernames:
        print(crypto(username, 2))
    
    print("\nPasswords:")
    for password in passwords:
        print(crypto(password, 2))
    
    print("\nCompanies:")
    for company in companies:
        print(crypto(company, 2))

def save_password(username, password, company):
    
    global iv

    iv = secrets.randbelow(900000) + 100000
    VERusername = crypto(username, 1)
    usernames.append(str(str(iv) + VERusername))

    iv = secrets.randbelow(900000) + 100000
    VERpassword = crypto(password, 1)
    passwords.append(str(str(iv) + VERpassword))

    iv = secrets.randbelow(900000) + 100000
    VERcompany = crypto(company, 1)
    companies.append(str(str(iv) + VERcompany))


def get_password(company):
    
    for i in range(len(companies)):
        if crypto(companies[i], 2) == company:
            return crypto(usernames[i], 2), crypto(passwords[i], 2)


while True:
 
    print("Enter your master password:")
    key = str(input())

    while True:
        if len(passwords) == 0:
            print("No passwords stored yet.")

        print("Enter a command (add, get, exit):")
        command = str(input())

        if command == "add":
       
             print("Please enter the username:")
             username = str(input())
      
             print("Please enter the password:")
             password = str(input())
       
             print("Please enter the company name:")
             company = str(input())
             save_password(username,  password, company)
             continue

        if command == "get":
            print("Please enter the company name:")
            company = str(input())
            result = get_password(company)
            if result:
                  username, password = result
                  print(f"Username: {username}, Password: {password}")
                  continue
            else:
                 print("No password found for that company.")
                 continue 

        if command == "exit":
           #print_everything()
           break


