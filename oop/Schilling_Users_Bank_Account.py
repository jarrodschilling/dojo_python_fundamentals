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

# ------------------------------------------------------------------------------------------
# ------------------ USER CLASS
# ------------------------------------------------------------------------------------------

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.savings = BankAccount(0.02, 0)
        self.checking = BankAccount(0.01, 0)
        self.joint = BankAccount(0.01, 0)
    
    def make_deposit(self, amount, account):
        if account == "savings":
            self.savings.deposit(amount)
            return self
        elif account == "checking":
            self.checking.deposit(amount)
            return self
        elif account == "joint":
            self.joint.deposit(amount)
            return self
    
    def make_withdrawal(self, amount, account):
        if account == "savings":
            self.savings.withdraw(amount)
            return self
        elif account == "checking":
            self.checking.withdraw(amount)
            return self
        elif account == "joint":
            self.joint.withdraw(amount)
            return self

    def display_user_balance(self, account):
        print(self.name)
        if account == "savings":
            self.savings.display_account_info()
            return self
        elif account == "checking":
            self.checking.display_account_info()
            return self
        elif account == "joint":
            self.joint.display_account_info()
            return self
        elif account == "all":
            self.savings.display_account_info()
            self.checking.display_account_info()
            self.joint.display_account_info()
            return self
    
    def transfer_money(self, amount, account, other_user, other_account):
        if account == "savings":
            self.savings.withdraw(amount)
        elif account == "checking":
            self.checking.withdraw(amount)
        elif account == "joint":
            self.joint.withdraw(amount)

        if other_account == "savings":
            other_user.savings.deposit(amount)
        elif other_account == "checking":
            other_user.checking.deposit(amount)
        elif other_account == "joint":
            other_user.joint.deposit(amount)

        print(f"Transfer from {self.name} to {other_user.name} complete")
        return self


# ------------------------------------------------------------------------------------------
# ------------------ TESTING
# ------------------------------------------------------------------------------------------

richard = User("Richard", "email@email.com")
# richard.make_deposit(5000, "checking").make_deposit(2000, "savings").make_withdrawal(500, "checking").display_user_balance("all")

brad = User("Brad", "gmail@gmail.com")

richard.make_deposit(1000, "savings").display_user_balance("all").transfer_money(200, "savings", brad, "checking").display_user_balance("all")
brad.display_user_balance("all")
