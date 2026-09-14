import random
from datetime import datetime


class BankAccount:

    def __init__(self, name, account_type, initial_balance=0):
        self.name = name
        self.account_type = account_type
        self.account_number = random.randint(100000, 999999)
        self.balance = initial_balance
        self.transactions = []

    # Deposit money
    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount!")
            return

        self.balance += amount

        self.transactions.append(
            f"Deposited ₹{amount:.2f} | {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
        )

        print(f"₹{amount:.2f} deposited successfully.")

    # Withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount!")
            return

        if amount > self.balance:
            print("Insufficient balance!")
            return

        self.balance -= amount

        self.transactions.append(
            f"Withdrawn ₹{amount:.2f} | {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
        )

        print(f"₹{amount:.2f} withdrawn successfully.")

    # Compound Interest
    def calculate_interest(self, rate, years, frequency=1):

        principal = self.balance

        # A = P(1 + r/n)^(nt)
        amount = principal * (
            1 + rate / (100 * frequency)
        ) ** (frequency * years)

        interest = amount - principal

        print("\n----- COMPOUND INTEREST -----")
        print(f"Principal Amount : ₹{principal:.2f}")
        print(f"Interest Rate    : {rate}%")
        print(f"Time             : {years} years")
        print(f"Compounds/Year   : {frequency}")
        print(f"Interest Earned  : ₹{interest:.2f}")
        print(f"Final Amount     : ₹{amount:.2f}")

        self.balance = amount

        self.transactions.append(
            f"Interest added: ₹{interest:.2f}"
        )

    # Show account details
    def account_details(self):

        print("\n========== ACCOUNT DETAILS ==========")
        print(f"Account Holder : {self.name}")
        print(f"Account Number : {self.account_number}")
        print(f"Account Type   : {self.account_type}")
        print(f"Balance        : ₹{self.balance:.2f}")
        print("=====================================")

    # Transaction history
    def transaction_history(self):

        print("\n========== TRANSACTION HISTORY ==========")

        if not self.transactions:
            print("No transactions yet.")
        else:
            for transaction in self.transactions:
                print(transaction)

        print("=========================================")


# ---------------- MAIN PROGRAM ----------------

print("========================================")
print("        PYTHON BANKING SYSTEM")
print("========================================")

name = input("Enter account holder name: ")

print("\nSelect Account Type")
print("1. Savings Account")
print("2. Current Account")

choice = input("Enter choice: ")

if choice == "1":
    account_type = "Savings"
else:
    account_type = "Current"

initial_balance = float(input("Enter initial deposit: ₹"))

account = BankAccount(
    name,
    account_type,
    initial_balance
)

print("\nAccount created successfully!")
print(f"Your Account Number is: {account.account_number}")


# ---------------- MENU ----------------

while True:

    print("\n========== BANK MENU ==========")
    print("1. Account Details")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Calculate Compound Interest")
    print("5. Check Balance")
    print("6. Transaction History")
    print("7. Exit")
    print("===============================")

    choice = input("Enter your choice: ")

    # Account Details
    if choice == "1":

        account.account_details()

    # Deposit
    elif choice == "2":

        amount = float(input("Enter deposit amount: ₹"))
        account.deposit(amount)

    # Withdraw
    elif choice == "3":

        amount = float(input("Enter withdrawal amount: ₹"))
        account.withdraw(amount)

    # Compound Interest
    elif choice == "4":

        rate = float(input("Enter annual interest rate (%): "))
        years = float(input("Enter time in years: "))

        print("\nCompounding Frequency")
        print("1. Yearly")
        print("2. Half-Yearly")
        print("4. Quarterly")
        print("12. Monthly")

        frequency = int(input("Enter frequency: "))

        account.calculate_interest(
            rate,
            years,
            frequency
        )

    # Balance
    elif choice == "5":

        print(f"\nCurrent Balance: ₹{account.balance:.2f}")

    # History
    elif choice == "6":

        account.transaction_history()

    # Exit
    elif choice == "7":

        print("\nThank you for using Python Banking System!")
        break

    else:

        print("Invalid choice! Please try again.")