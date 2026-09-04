import random
def game():

        
                
                computer=random.choice([-1,0,1])
                you=input("enter your choice: ")
                do={"r":-1,"p":0,"s":1}
                reversedo={-1:"rock",0:"paper",1:"scissor"}
                choose =  do[you]
                print(f"you chose{reversedo[choose]} \n computer  chose{reversedo[computer]}")
                
                
                if  computer==choose:
                        print("its a  draw")
                        with open("result.txt","w")  as f:
                                f.write("its a draw\n")
                elif  choose==-1 and computer==0:
                        print("you won")
                        with open("result.txt","w")  as f:
                                f.write("you won\n")
                elif choose==-1 and computer==1:
                        print("you lose")
                        with open("result.txt","w") as  f:
                                f.write("you  lose\n")
                elif  choose==0  and  computer==-1:
                        print("you lose")
                        with open("result.txt","w") as  f:
                                f.write("you  lose\n")
                elif  choose==0  and  computer==1:
                        print("you won")
                        with open("result.txt","w")  as f:
                                f.write("you won\n")
                elif  choose==1  and computer==0:
                        print("you lose")
                        with open("result.txt","w") as  f:
                                f.write("you  lose\n")
                elif  choose==1 and computer==-1:
                        print("you won")
                        with open("result.txt","w")  as f:
                                f.write("you won\n")
while True:
        game()


        h=(input("you wanna play again(y/n):"))

        if h=="n":
                break