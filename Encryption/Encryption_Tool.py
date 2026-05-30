#JUST A DEMO - DO NOT USE FOR REAL SENSITIVE DATA!
import random

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
        
    return stes % (2**32)

def crypto(mes,mode):
    
    if mode == 1:
        bmes = list(mes)
        random.seed(seedgen(key))
        for i in range (len(bmes)):
            bmes[i] = ord(bmes[i])
            try:
                bmes[i] = chr(zkv(bmes[i] + random.randint(100, 100000)))
            except:
                print("unexpected error")
                break
    else:
        bmes = list(mes)
        random.seed(seedgen(key))
        for i in range (len(bmes)):
            bmes[i] = ord(bmes[i])
            try:
                bmes[i] = chr(zke(bmes[i] - random.randint(100, 100000)))
            except:
                print("invalid password")
                break
    
    return "".join(bmes)
    
            

    
print("Welcome to the Encryption_Tool!")  
print("JUST A DEMO - DO NOT USE FOR REAL SENSITIVE DATA!")
print(" ")

while True:
    print("Do you want to Encrypt or Decrypt? (En/De)")
    if "EN" in input().upper():
        print('Choose your password or type "generate" for a password which is saver')
        sp = input()
        if "GEN" in sp.upper():
            key = random.randint(50, 9999) 
        else:
            key = str(sp)
            
        
        print("Type in the message that should be encrypted")
        mes = str(input())
        
        print("Your encrypted message is: ")
        print(" ")
        print(str(crypto(mes,1)))
        print(" ")
        print("Please don't forget your password: " + str(key))
            
        
        
    else:
        print("Type in/Paste the encrypted message")
        mes = str(input())
        print("Type in the Key")
        key = str(input())
        print(" ")
        print("The decrypted message is: ")
        print(" ")
        print(str(crypto(mes,2)))
        print(" ")