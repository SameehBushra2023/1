import string
import collections

plaintext = input("Enter your message \n")
if(plaintext[0] == "!"):
    f = open(plaintext[1:], "r")
    plaintext=f.read()
def encrypt():
    #encrypt
    x = len(plaintext)
    shift = int(input("Enter the shift \n"))
    plainkey = collections.deque(string.ascii_lowercase)
    plainkey.rotate(-shift)
    cipherkey = list(plainkey)
    plainkey.rotate(shift)
    i = 0
    while (i < x):
        y = 0
        if(plaintext[i] == " "):
            f = open("encryption.txt", "a")
            f.write(" ")
            print(" ", end='')
            y = y + 1
            i = i + 1
        while(plaintext[i] != plainkey[y]):
            y = y + 1
        if(plaintext[i] == plainkey[y]):
            encryption = cipherkey[y]
            f = open("encryption.txt", "a")
            f.write(encryption)
            print(encryption, end='')
        i = i + 1
    print(" ")
def decrypt():
    #decrypt
    shift = int(input("Enter the shift or press 0 for a brute attack\n"))
    x = len(plaintext)
    plainkey = collections.deque(string.ascii_lowercase)
    plainkey.rotate(shift)
    cipherkey = list(plainkey)
    plainkey.rotate(-shift)
    brutefile = list(plainkey)
    brutefile.append("IGNORE")
    #bruteforce
    if(shift == 0):
        k = 0
        while(k < 26):
            f = open("shift"+brutefile[k]+".txt", "w")
            f.write("")
            k = k + 1
        k = 0
        while(shift < 26):
            plainkey.rotate(shift)
            cipherkey = list(plainkey)
            plainkey.rotate(-shift)
            i = 0
            while (i < x):
                y = 0
                if(plaintext[i] == " "):
                    f = open("shift"+brutefile[k]+".txt", "a")
                    f.write(" ")
                    print(" ", end='')
                    y = y + 1
                    i = i + 1
                while(plaintext[i] != plainkey[y]):
                    y = y + 1
                if(plaintext[i] == plainkey[y]):
                    encryption = cipherkey[y]
                    if(brutefile[k] != "IGNORE"):
                        f = open("shift"+brutefile[k]+".txt", "a")
                        f.write(encryption)
                        print(encryption, end='')
                i = i + 1
            print(" ")
            shift = shift + 1
            k = k + 1
    #shift decryption
    else:
        i = 0
        while (i < x):
            y = 0
            if(plaintext[i] == " "):
              
                print(" ", end='')
                y = y + 1
                i = i + 1
            while(plaintext[i] != plainkey[y]):
                y = y + 1
            if(plaintext[i] == plainkey[y]):
                encryption = cipherkey[y]
            
                print(encryption, end='')
            i = i + 1
        print(" ")
while(1):
    choice=int(input("\n 1.Encryption \n 2.Decryption: \n 3.EXIT \n"))
    if choice==1:
        encrypt()
    elif choice==2:
        decrypt()
    elif choice==3:
        exit()
    else:
        print("Choose correct choice")