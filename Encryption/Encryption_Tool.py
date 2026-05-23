import random



def crypto(mes,mode):
    
    if mode == 1:
        bmes = list(mes)
        for i in range (len(bmes)):
            bmes[i] = ord(bmes[i])
            bmes[i] = chr(bmes[i] + random.randint(100, 100000))
    else:
        bmes = list(mes)
        for i in range (len(bmes)):
            bmes[i] = ord(bmes[i])
            bmes[i] = chr(bmes[i] - random.randint(100, 100000))
    return "".join(bmes)
            

    
print("Welcome to Crypto_Text!")  


while True:
    print("Do you want to Encrypt or Decrypt? (En/De)")
    if "EN" in input().upper():
        print('Choose your key (a number bigger than 0) or type "generate" for a key which is saver')
        sp = input()
        if "GEN" in sp.upper():
            key = random.randint(50, 9999) 
        else:
            key = int(sp)
            
        random.seed(key)
        
        print("Type in the message that should be encrypted")
        mes = str(input())
        
        print("Your encrypted message is: ")
        print(" ")
        print(str(crypto(mes,1)))
        print(" ")
        print("Please don't forget your Key: " + str(key))
            
        
        
    else:
        print("Type in/Paste the encrypted message")
        mes = str(input())
        print("Type in the Key")
        key = int(input())
        random.seed(key)
        print(" ")
        print("The decrypted message is: ")
        print(" ")
        print(str(crypto(mes,2)))
        print(" ")