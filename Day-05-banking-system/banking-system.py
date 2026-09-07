from random import randint

def userinfo():
        acc={}
        while True:
            
            print("1. account creation")
            print("2. account info")
            print("3 add amount to account ")
            print("4. withdrawal")
            print("5. Transaction history")
            a=int(input("ente your choice: "))
            if a==1:
                print("1.savings account: ")
                print("2. cuurent account: ")
                b=int(input("enter your choice: "))
                if b ==1:
                    c=input("enter your name: ")
                    d=int(input("enter your contact no: "))
                    e=randint(200001,300000)
                    acc[c]=[e,d]

                    print(f"Acoount creation successfull\n your account no is{e} \n and the account info is \n{acc}")
                    
                else:
                    c=input("enter your name: ")
                    d=int(input("enter your contact no: "))
                    e=randint(200001,300000)
                    acc[c]=[e,d]
                    print(f"Acoount creation successfull\n your account no is{e} \n and the account info is \n{acc}")
                    
            if a ==2:
                c=input("enter username: ")
                if c in acc:
                    print(acc[c])
                else:
                    print("invalid info")
            if a==3:
                c=input("enter acc username: ")
                if c in acc:
                    g=int(input("enter the amount u wanna add: "))
                    n=int(input("enter the pin: "))
                    acc[c]=[d,e,g,n]
                    print(f"the amount added to your account \n current balence is {acc[c]}")
                else:
                    print("user not found ")
            if a == 4:
                c = input("Enter your username: ")

                if c in acc:
                    w = int(input("Enter amount you want to withdraw: "))
                    n = int(input("Enter the PIN: "))

                    if n == acc[c][3]:

                        if w <= acc[c][2]:
                            acc[c][2] -= w

                            print("Withdrawal successful")
                            print("Remaining balance:", acc[c][2])

                            with open("file.txt", "a") as f:
                                f.write(f"amount debited={w}\n")
                                f.write(f"remaining balance={acc[c][2]}\n\n")

                        else:
                            print("Insufficient balance")

                    else:
                        print("Incorrect PIN")

            else:
                    print("User not found")
            if a ==5:
                c=input("enter your username: ")
                if c in acc:
                    with open("file.txt","r") as f:
                        print(f.readlines())
userinfo()
