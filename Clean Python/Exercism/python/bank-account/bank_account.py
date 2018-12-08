class BankAccount(object):

    def __init__(self):
        self.balance = 0
        self.opened = False

    def get_balance(self):
        """Get current balance"""
        if self.opened:
            return self.balance
        else:
            raise ValueError('Not an existing account')

    def open(self):
        if self.opened:
            raise ValueError('Account already exists. Open new account.')
        else:
            self.opened = True
            self.balance = 0

    def deposit(self, amount):
        if not self.check_amount_valid(amount):
            raise ValueError(f'Amount deposited cannot be {amount}. It must be a positive amount.')
        else:
            self.balance = self.get_balance() + amount


    def withdraw(self, amount):
        if self.check_amount_valid(amount):
            if self.get_balance() < amount:
                raise ValueError(f'Cannot withdraw {amount}. Current balance is {self.balance}. Over draft not allowed')
            else:
                self.balance -= amount
        else:
            raise ValueError(f'Cannot withdraw {amount}. Current balance is {self.balance}. Over draft not allowed')

    def close(self):
        if self.opened:
            self.opened = False
            self.balance = 0
        else:
            raise ValueError('Not an existing account')

    @classmethod
    def check_amount_valid(cls, amount):
        return None != amount > 0
