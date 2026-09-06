def student():
    info={}
    while True:

        print("1.show student info")
        print("2.add student")
        print("3.update  student roll_no")
        print("4.update student div")
        print("5.update student contact")
        a=int(input("enter your choice: "))
        if a==1:
                b=input("enter student name: ")
                if b in info:
                    print(info[b])
                    
                else:
                    print("student not found")
        if a==2:
            c=input("enter student name : ")
            d=input("enter student div: ")
            e=int(input("enter student roll_no: "))
            f=int(input("enter student contact: "))
            info[c]=[d,e,f]
            print(info)
            
        if a==3:
            g=input("give the student name whoes roll_no u want to update: ")
            if g in info:
                h=int(input("enter the new roll_no: "))
                info[g][1]=h
                print(f"updated info {info[g]}")
                

            else:
                print("wrong input")
        if a==4:
            g=input("enter whoes div u want to update: ")
            if g in info:
                j=input("enter the updated division: ")
                info[g][0]=j
                print(f"updated info {info[g]}")
                
            else:
                print("wrong input ")
        if a==5:
            g=input("enter whoes contact u wanna update: ")
            if g in info:
                s=int(input("enter updated contact: "))
                info[g][2]=s
                print(f"the updated info is {info[g]}")
                
            else:
                print("invalid input  ")
student()