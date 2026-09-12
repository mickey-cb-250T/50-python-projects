class form:
    print("***Sports Registration Form***")
    print("note** kindly fill all the details  ")
    def forum(self):
        teamc={}
        teamk={}
        teamv={}
        teamkh={}
        a=int(input(" PLEASE ENTER YOUR  PRN: "))
        if 24067971242001<a<24067971242063:
            b=int(input("ENTER YOUR ROLL NO. : "))
            if 24212001<b<24212058:
                print("soo good to see you\n kindly enter further details to participate in sports event!!")
                c=input("enter your sports catagory\ncricket/kabbadi/volleyball/khokho: ").lower()
                if c=="cricket":
                    print("welcome to cricket registration🏏 ")
                    d=input("Please enter your team name: ")
                    cap=input("please enter captain name: ")
                    p2=input("player 2 name: ")
                    p3=input("player 3 name: ")
                    p4=input("player 4 name: ")
                    p5=input("player 5 name: ")
                    p6=input("player 6 name: ")
                    p7=input("player 7 name: ")
                    p8=input("player 8 name: ")
                    p9=input("player 9 name: ")
                    p10=input("player 10 name: ")
                    p11=input("player 11 name: ")
                    teamc[d]=[cap,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11]
                    print("Registration succesfull 🥳")
                    print(f"all the best👍\nTeam={d}\n and {teamc}")
                    print("Thanks for visiting")
                elif c=="kabaddi":
                    print("Welcome to kabbadi registration🤼‍♂️ ")
                    e=input("Enter your team name ")
                    cap=input("enter captian name: ")
                    p2=input("player 2 name: ")
                    p3=input("player 3 name: ")
                    p4=input("player 4 name: ")
                    p5=input("player 5 name: ")
                    p6=input("player 6 name: ")
                    p7=input("player 7 name: ")
                    p8=input("player 8 name: ")
                    teamk[e]=[cap,p2,p3,p4,p5,p6,p7,p8]
                    print("Registration succesfull 🥳")
                    print(f"All the best👍\nTeam={e}\nand{teamk}")
                    print("Thanks for visiting")
                elif c=="Khokho":
                    print("Welcome to khokho registration🏃🏻‍♂️")
                    f=input("Enter your team name : ")
                    cap=input("Enter captain name: ")
                    p2=input("Player 2 name: ")
                    p3=input("Player 3 name: ")
                    p4=input("Player 4 name: ")
                    p5=input("Player 5 name: ")
                    p6=input("Player 6 name: ")
                    p7=input("Player 7 name: ")
                    p8=input("Player 8 name: ")
                    p9=input("Player 9 name: ")
                    p10=input("Player 10 name: ")
                    teamkh[f]=[cap,p2,p3,p4,p5,p6,p7,p8,p9,p10]
                    print("Registration succesfull 🥳")
                    print(f"All the best👍\nTeam={f}\nand{teamkh}")
                    print("Thanks for visiting")
                elif c=="volleyball":
                    print("Welcome to volleyball registration🏐")
                    g=input("Enter your team name: ")
                    cap=input("enter captain name: ")
                    p2=input("Player 2 name: ")
                    p3=input("Player 3 name: ")
                    p4=input("Player 4 name: ")
                    p5=input("Player 5 name: ")
                    p6=input("Player 6 name: ")
                    p7=input("Player 7 name: ")
                    teamv[g]=[cap,p2,p3,p4,p4,p5,p6,p7]
                    print("Registration succesfull 🥳")
                    print(f"All the best👍\n{g}\nand Team={teamv}")
                    print("Thanks for visiting")
                else:
                    print("Wrong Choice👎")
                    print("Thanks for visiting")
shri=form()
shri.forum()
