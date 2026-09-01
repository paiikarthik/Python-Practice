#bruteforce using python


import os
from random import randint

pas=input("Send the Password:")

keys=["1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


pwd=""

while(pwd!=pas):
    pwd=""
    for i in range(len(pas)):
        guesspass=keys[randint(0,4)]
        pwd=str(guesspass)+str(pwd)
        print(pwd)
        print("cracking password")
        os.system("cls")

print(f"The pass is: {pwd}")
