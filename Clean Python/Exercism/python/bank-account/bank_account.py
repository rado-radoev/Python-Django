class BankAccount(object):

    def __init__(self):
        self.balance = 0
        self.opened = True

    @property
    def get_balance(self):
        """Get current balance"""
        return self.balance

    def open(self, balance = 0):
        if balance > 0:
            self.balance = balance
        else:
            self.balance = 0

    def deposit(self, amount):
        if not self.check_amount_valid(amount):
            raise ValueError(f'Amount deposited cannot be {amount}. It must be a positive amount.')
        else:
            self.balance = self.get_balance + amount


    def withdraw(self, amount):
        if not self.check_amount_valid(amount):
            if self.get_balance < amount:
                raise Exception(f'Cannot withdraw {amount}. Current balance is {self.balance}. Over draft not allowed')
            else:
                self.balance - amount

    def close(self):
        self.open(False)
        set.balance = 0

    @classmethod
    def check_amount_valid(cls, amount):
        return None != amount > 0
