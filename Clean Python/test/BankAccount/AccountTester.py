from BankAccount.Account import Account

acct = Account("Jose", 100)
print(acct.balance)

print(acct.owner)

print(acct)

acct.deposit(50)
acct.withdraw(75)
acct.withdraw(500)

