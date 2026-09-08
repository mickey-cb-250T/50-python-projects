class hotel:

    def menu_card(self):

        with open("menu.txt", "r", encoding="utf-8") as f:
            print(f.read())

    def Table(self):

        a = int(input("Enter the number of people you want a table for: "))

        print(f"Your table for {a} people is booked.")

    def order(self):

        with open("menu.txt", "r", encoding="utf-8") as f:
            d = f.readlines()

        print("".join(d))

        c = int(input("What do you wanna order? : "))

        if 1 <= c <= len(d):
            print(f"Your item is added:\n{d[c - 1]}")
        else:
            print("Currently item is not available.")


while True:

    shri = hotel()

    print("\n===== HOTEL MANAGEMENT =====")
    print("1. Menu Card")
    print("2. Table Booking")
    print("3. Order")
    print("4. Exit")

    e = int(input("Enter your choice: "))

    if e == 1:
        shri.menu_card()

    elif e == 2:
        shri.Table()

    elif e == 3:
        shri.order()

    elif e == 4:
        print("Thank you for visiting!")
        break

    else:
        print("Invalid choice!")