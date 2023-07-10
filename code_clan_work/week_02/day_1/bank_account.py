class BankAccount():
	def __init__(self, holder_name, balance, account_type):
		self.holder_name = holder_name
		self.balance = balance
		self.account_type = account_type

	def get_holder_name(self):
		return self.holder_name
	def get_balance(self):
		return self.balance
	def get_account_type(self):
		return self.account_type

	def set_holder_name(self, holder_name):
		self.holder_name = holder_name
	def set_balance(self, balance):
		self.balance = balance
	def set_account_type(self, account_type):
		self.account_type = account_type

	def pay_in(self, amount):
		current_balance = self.get_balance()
		self.set_balance(current_balance + amount)

	def pay_monthly_fee(self):
		current_balance = self.get_balance()
		if self.get_account_type() == "business":
			amount = 100
		elif self.get_account_type() == "personal":
			amount = 50
		self.set_balance(current_balance - amount)