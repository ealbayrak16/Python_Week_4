from math import gcd
def ekok():
    print("Please Enter 4 Possitive Number")
    while True:
        a = input("Enter 1. Number : ")
        b = input("Enter 2. Number : ")
        c = input("Enter 3. Number : ")
        d = input("Enter 4. Number : ")
        if a=="0" or b=="0" or c=="0" or d=="0":
            print("Please Enter Number Except Zero")
            continue
        try:
            eko = int(a) * int(b) * int(c) * int(d) / gcd(int(a), int(b), int(c), int(d))
            print("EKOK Of 4 Numbers:", eko)
            break
        except ValueError as va:
            print("Please Enter Only Number :", va)

ekok()