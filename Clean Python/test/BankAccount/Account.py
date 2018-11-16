class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit_amount):
        print("Deposit Accepted")
        self.balance += deposit_amount

    def withdraw(self, withdraw_amount):
        if self.balance - withdraw_amount < 0:
            print("Funds Unavailabe!")
        else:
            print("Withdraw Accepted")
            self.balance -= withdraw_amount

    def __str__(self):
        return "Account owner: {owner:>6} \nAccount balance: {balance:>2}".format(owner=self.owner, balance=self.balance)