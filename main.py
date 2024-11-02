class BankAccount:
    def __init__(self, account_name):
        self.account_name = account_name
        self.balance = 0.0


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ${amount:.2f}. New balance: ${self.balance:.2f}.")
        else:
            print("Deposit amount must be positive.")

    def view_balance(self):
        print(f"Current balance for account {self.account_name}: ${self.balance}")



class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        account_name = input("Enter your account name: ")
        if account_name in self.accounts:
            print("Account already exist")
        else:
            self.accounts[account_name] = BankAccount(account_name)
            print("Account created successfully")


    def deposit_money(self):
        account_name = input("Enter account name: ")
        if account_name in self.accounts:
            amount = int(input("Enter deposit amount: "))
            self.accounts[account_name].deposit(amount)
        else:
            print("Account not found")


    def view_balance(self):
        account_name = input("Enter account name: ")
        if account_name in self.accounts:
            return self.accounts[account_name].view_balance()
        else:
            print("Account not found")


    def run(self):
        while True:
            print("\n1. Create Account\n2. Deposit Money\n3. View Balance\n4. Exit")
            choice = input("Enter choice: ")
            if choice == '1':
                self.create_account()
            elif choice == "2":
                self.deposit_money()
            elif choice == "3":
                self.view_balance()
            elif choice == '4':
                print("Exiting the system. Goodbye!")
                break

            else:
                print("Unknown choice!!!")


if __name__ == "__main__":
    banking_system = BankingSystem()
    banking_system.run()