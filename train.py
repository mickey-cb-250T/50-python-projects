from  random  import randint
class train:
    print("---welcome to the train booking system---")
    def  __init__(self,choice1, choice2, choice3,choice4,train_no,name,fro,to,birth,price):
        self.choice1=choice1
        self.choice2=choice2
        self.choice3=choice3
        self.choice4=choice4
        self.train_no=train_no
        self.name=name
        self.fro=fro
        self.to=to
        self.birth=birth
        self.price=price
        print(choice1)
        print(choice2)
        print(choice3)
        print(choice4)
    def ticket(self):
            print(f"the train number is\n{self.train_no} and the name of the train is\n{self.name} and the route is form\n{self.fro} to{self.to}")
    def booking(self):
            maharashtra_stations = [
                        "Ahmednagar",
                        "Ajni (Nagpur)",
                        "Akalkot Road",
                        "Akola",
                        "Akurdi",
                        "Amalner",
                        "Amgaon",
                        "Amravati",
                        "Andheri",
                        "Badnera",
                        "Balharshah",
                        "Bandra Terminus",
                        "Baramati",
                        "Belapur",
                        "Bhandara Road",
                        "Bhokar",
                        "Bhusawal",
                        "Borivali",
                        "Byculla",
                        "Chalisgaon",
                        "Chanda Fort",
                        "Chandrapur",
                        "Charni Road",
                        "Chhatrapati Sambhajinagar",
                        "Chhatrapati Shivaji Maharaj Terminus",
                        "Chinchpokli",
                        "Chinchwad",
                        "Dadar (CR)",
                        "Dadar (WR)",
                        "Dahisar",
                        "Daund",
                        "Dehu Road",
                        "Devlali",
                        "Dhamangaon",
                        "Dharangaon",
                        "Dharashiv",
                        "Dharmabad",
                        "Dhule",
                        "Diva",
                        "Dudhani",
                        "Gangakher",
                        "Godhani",
                        "Gondia",
                        "Grant Road",
                        "Hadapsar",
                        "Hatkanangale",
                        "Hazur Sahib Nanded",
                        "Himayatnagar",
                        "Hinganghat",
                        "Hingoli Deccan",
                        "Igatpuri",
                        "Jalgaon",
                        "Jalna",
                        "Jeur",
                        "Jogeshwari",
                        "Kalyan Junction",
                        "Kamptee",
                        "Kandivali",
                        "Kanjur Marg",
                        "Karad",
                        "Katol",
                        "Kedgaon",
                        "Kinwat",
                        "Kopargaon",
                        "Kurduwadi Junction",
                        "Kurla Junction",
                        "Lasalgaon",
                        "Latur",
                        "Lokmanya Tilak Terminus",
                        "Lonand Junction",
                        "Lonavala",
                        "Lower Parel",
                        "Malad",
                        "Malkapur",
                        "Manmad Junction",
                        "Manwath Road",
                        "Marine Lines",
                        "Matunga",
                        "Miraj Junction",
                        "Mudkhed Junction",
                        "Mumbai Central",
                        "Mumbra",
                        "Murtizapur Junction",
                        "Nagarsol",
                        "Nagpur Junction",
                        "Nandgaon",
                        "Nandura",
                        "Nandurbar",
                        "Narkher Junction",
                        "Nashik Road",
                        "Netaji Subhash Chandra Bose Itwari Junction",
                        "Pachora Junction",
                        "Palghar",
                        "Pandharpur",
                        "Panvel Junction",
                        "Parbhani Junction",
                        "Parel",
                        "Parli Vaijnath",
                        "Partur",
                        "Phaltan",
                        "Prabhadevi",
                        "Pulgaon Junction",
                        "Pune Junction",
                        "Purna Junction",
                        "Raver",
                        "Rotegaon",
                        "Sainagar Shirdi",
                        "Sandhurst Road",
                        "Sangli",
                        "Satara",
                        "Savda",
                        "Selu",
                        "Sewagram",
                        "Shahad",
                        "Shegaon",
                        "Shivaji Nagar Pune",
                        "Shri Chhatrapati Shahu Maharaj Terminus Kolhapur",
                        "Solapur",
                        "Talegaon",
                        "Thakurli",
                        "Thane",
                        "Titvala",
                        "Tumsar Road",
                        "Umri",
                        "Uruli",
                        "Vadala Road",
                        "Vidyavihar",
                        "Vikhroli",
                        "Wadsa",
                        "Wardha",
                        "Washim",
                        "Wathar"
                        ]
            a=int(input("enter your age: "))
            while True:
                if a>18:
                    print("you are eligible  for booking the ticket")
                else:
                    print("You are not eligible for booking the ticket")
                    break
                self.fro=input("enter your boarding station:")
                if self.fro not in maharashtra_stations:
                    print("sorry your boarding station is not in maharashtra")
                    break
                else:
                    self.to=input("enter your destination:")
                    if self.to not in maharashtra_stations:
                        print("sorry your destination is not in maharashtra")
                        break
                    else:
                        a=int(input("choose the number of ticket want: "))
                        if a>1:
                            b=(int(input("enter the  no of tickets you  want:")))
                            print(f"your ticket price is {self.price*b}")
                            d=input("do you  want to book your ticket y/n:")
                            if d=="y":
                                print(f"your ticket is book successfully\n your train no is  {self.train_no} \nfrom({self.fro} to {self.to})")
                                with  open("bookings.txt","a") as f:
                                    f.write(f"your ticket is book successfully\n your train no is  {self.train_no} \nfrom({self.fro} to {self.to})")
                                    break
                        else:
                            print(f"the available birth is{self.birth}")
                            print(f"the price of  your ticekt is{self.price}")
                            d=input("do you  want to book your ticket y/n:")
                            if d=="y":
                                print(f"your ticket is book successfully your train no is  {self.train_no} from({self.fro} to {self.to})")
                                with  open("bookings.txt","a") as f:
                                    f.write(f"your ticket is book successfully  your train no is  {self.train_no} from({self.fro} to {self.to})")
                                    break
                            else:
                                print("You are not eligible for booking the ticket")
                                pass
    def ticketinfo(self):
                l=int(input("enter the train number to get the train info: "))
                with open("bookings.txt","r") as f:
                    for railway in f:
                        if str(l) in railway:
                            print(railway)
    def cancel(self):
            if  self.choice4:
                c=input("do want to cancel your  ticket y/n: ")
                if c=="y":
                    print("your ticket is cancelled successfully")

b=train("traininfo","booking","ticketinfo","cancellation",randint(212021,212054),"maharashtra expreess","satara","amravati",randint(1,5),randint(260,450))
r=int(input("Enter the choice: "))
if  r==1:
    b.ticket()
elif r==2:
    b.booking()
elif r==3:
    b.ticketinfo()
else:
    b.cancel()
