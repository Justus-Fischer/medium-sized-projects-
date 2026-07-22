#just a demo 
#Do not use for real passwords 

import time
import random
import secrets
import json
import os

def fillup(password):
    filledpassword = password.ljust(35,"\x00")
    return filledpassword

def short(password):
    shortpassword = password.rstrip("\x00")
    return shortpassword

def saveData():
    daten = {
        "usernames": usernames,
        "passwords": passwords,
        "companies": companies
    }
    
    with open("psdata.txt", "w", encoding="utf-8") as file:
        json.dump(daten, file)


def loadData():
    global usernames, passwords, companies
    if os.path.exists("psdata.txt"): 
        with open("psdata.txt", "r", encoding="utf-8") as file:
            daten = json.load(file)
            usernames = daten["usernames"]
            passwords = daten["passwords"]
            companies = daten["companies"]

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

stes = 15
def seedgen(pasw):
    global stes
    if stes != 15:

        return stes

    stes = 5381
    bpasw = list(pasw)
    pr = time.time()
    for r in range(600000):
        for i in range(len(bpasw)):

            stes = int(((stes * 33) + ord(bpasw[i]) + r) % (2 ** 256))
    #print(time.time()-pr)
    return stes


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
    
    for i in range(len(companies)):
        print(f"Company: {crypto(companies[i], 2)}, Username: {crypto(usernames[i], 2)}, Password: {short(crypto(passwords[i], 2))}")

    print(" ")


def save_password(username, password, company):
    
    global iv

    iv = secrets.randbelow(900000) + 100000
    VERusername = crypto(username, 1)
    usernames.append(str(str(iv) + VERusername))

    iv = secrets.randbelow(900000) + 100000
    VERpassword = crypto(fillup(password), 1)
    passwords.append(str(str(iv) + VERpassword))

    iv = secrets.randbelow(900000) + 100000
    VERcompany = crypto(company, 1)
    companies.append(str(str(iv) + VERcompany))


def get_password(company):
    
    for i in range(len(companies)):
        if  crypto(short(companies[i]), 2).lower() == company.lower():
            return crypto(usernames[i], 2), short(crypto(passwords[i], 2))
    for i in range(len(companies)):
        if company.lower() in crypto(companies[i], 2).lower():
            print(f"Did you mean '{crypto(companies[i], 2)}'?")
            


while True:
 
    print("Enter your master password:")
    key = str(input())
    print("Please wait a moment")
    print("Decrypting can take a few seconds.")
    seedgen(key)
    print(" ")
    loadData()

    while True:
        if len(passwords) == 0:
            print("No passwords stored yet.")

        print("Enter a command (add, get, exit, more, help):")
        command = str(input().lower())
        print(" ")

        if command == "more":
            print("Other commands: everything, delete, reset, help")
            command = str(input().lower())
            print(" ")

        if command == "help":
            print("Explaination of commands:")
            print("add - Add a new password")
            print("get - Get a password for a given company")
            print("exit - Exit the program")
            print("everything - Show all stored information")
            print("delete - Delete a password for a given company")
            print("reset - Reset all stored data")
            print("help - Show this help message")
            print(" ")
            print("What do you want to do?")
            command = str(input().lower())
            print(" ")

        if command == "add":
       
             print("Please enter the username:")
             username = str(input())
      
             print("Please enter the password:")
             password = str(input())
       
             print("Please enter the company name:")
             company = str(input())
             save_password(username,  password, company)
             print(" ")
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
                 print(" ")
                 continue 

        if command == "exit":
           
           saveData()
           key = None
           print(" ")
           break

        if command == "delete":
            print("Please enter the company name to delete:")
            company = str(input())
            for i in range(len(companies)):
                if crypto(companies[i], 2) == company:
                    del usernames[i]
                    del passwords[i]
                    del companies[i]
                    print(f"Deleted password for {company}.")
                    print(" ")
                    continue
            
            for i in range(len(companies)):
                 if company.lower() in crypto(companies[i], 2).lower():
                      print(f"Did you mean '{crypto(companies[i], 2)}'?")
                      continue 
                        

            print("No password found for that company.")
                    


        if command == "reset":
            print("Are you sure you want to reset all data? (yes/no)")
            confirmation = str(input())
            print(" ")
            if confirmation.lower() == "yes":
                usernames = []
                passwords = []
                companies = []
                saveData()
                print("All data has been reset.")
                print("")
            else:
                print("Reset cancelled.")
                print("")
            continue

        if command == "everything":
            print_everything()
            print(" ")
            print("")
            continue



