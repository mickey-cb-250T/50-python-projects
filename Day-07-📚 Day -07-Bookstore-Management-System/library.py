class library:

    available = {
    1: ("Atomic Habits", 350),
    2: ("To Kill a Mockingbird", 299),
    3: ("The Alchemist", 250),
    4: ("1984", 220),
    5: ("Rich Dad Poor Dad", 320),
    6: ("The Great Gatsby", 199),
    7: ("Psychology of Money", 340),
    8: ("Ikigai", 280),
    9: ("Sapiens", 450),
    10: ("The Silent Patient", 310)
    }
    for book_id,(title,price) in available.items():
        print(f"{book_id} {title}---{price}")
    
    def options(self):
            books={}
                
            a=int(input("enter your choice: "))
            books[a]=self.available[a]
            b=input("wanna add some more books (y/n): ")
            while True:
                if b=="y":
                    
                        c=int(input("add more books: "))
                        
                            
                        
                        books[c]=self.available[c]
                        for details in books.values():
                                print(details[0])
                        d=input("payment?y/n: ")
                        if d=="y":
                                print(f"===orders===")
                                for items in books.values():
                                    print(items[0], items[1])
                                print("==grand total==")
                        
                                grand_total=sum(item[1] for item in books.values())
                                print(grand_total)
                                break
                                    
                            
                else:
                        print("===orders===")
                        for items in books.values():
                            print(items[0],items[1])
                            print("==grand total=")
                            print(items[1])
                        
                        break

                    

shri=library()
    
shri.options()