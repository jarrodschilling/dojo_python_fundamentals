class BankAccount:
    accounts_list = []
    def __init__(self, rate, balance=0):
        self.balance = balance
        self.rate = rate
        BankAccount.accounts_list.append(self)


    def deposit(self, amount):
        self.balance += amount
        return self


    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self
        else:
            self.balance -= amount
            return self


    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self


    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (1 + self.rate)
        return self
    
    @classmethod
    def all_accounts(cls):
        for account in cls.accounts_list:
            print(f"Balance: ${account.balance}, Current Rate: {account.rate * 100}%")


jarrod = BankAccount(.05)
bezos = BankAccount(.1, 1000000000)

jarrod.deposit(10000).deposit(20000).deposit(250).withdraw(4000).yield_interest().display_account_info()

bezos.deposit(1000000).deposit(25000000).withdraw(100000000).withdraw(200000000).withdraw(100000000).withdraw(3000000).yield_interest().display_account_info()

BankAccount.all_accounts()