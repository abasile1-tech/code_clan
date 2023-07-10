from bank_account import BankAccount

account = BankAccount("Rob", 50000, "business")

print(account.get_holder_name())
print(account.get_account_type())
print(account.get_balance())

account2 = BankAccount("Cass", 1000, "personal")
print(account2.get_balance())

account.pay_in(50)
print(account.get_balance())