

class BankAccount:
    def __init__(self, account_number, first_name, last_name):
        self.account_number = account_number
        self.account_holder = f"{first_name} {last_name}"
        self.balance = 0.0

    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError("Invalid amount. Please provide a numeric value.")
        
        self.balance += amount
        print(f"Your balance after the deposit is: {self.balance}")

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError("Invalid amount. Please provide a numeric value.")
        
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Your balance after the withdrawal is: {self.balance}")



account_number = int(input("Enter your account number: "))
first_name = input("Enter your First name: ")
last_name = input("Enter your last name: ")


account = BankAccount(account_number, first_name, last_name)

while True:
    print("\nOptions:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")

    choice = int(input("Enter your choice (1, 2, or 3): "))

    if choice == 1:
        deposit_amount = float(input("Enter deposit amount: "))
        account.deposit(deposit_amount)
    elif choice == 2:
        withdraw_amount = float(input("Enter withdrawal amount: "))
        account.withdraw(withdraw_amount)
    elif choice == 3:
        print("Exiting program. Thank you!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")






