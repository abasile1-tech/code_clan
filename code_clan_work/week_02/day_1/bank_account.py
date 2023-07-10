class BankAccount():
	def __init__(self, holder_name, balance, account_type):
		self.__holder_name = holder_name
		self.__balance = balance
		self.__account_type = account_type
		self.__rates = {
			"personal": 50,
			"business": 100,
			"charity": 0
		}

	@property
	def holder_name(self):
		return self.__holder_name
	@property
	def balance(self):
		return self.__balance
	@property
	def account_type(self):
		return self.__account_type
	@property
	def rates(self):
		return self.__rates

	def get_holder_name(self):
		return self.__holder_name
	def get_balance(self):
		return self.__balance
	def get_account_type(self):
		return self.__account_type

	def set_holder_name(self, holder_name):
		self.__holder_name = holder_name
	def set_balance(self, balance):
		self.__balance = balance
	def set_account_type(self, account_type):
		self.__account_type = account_type

	def pay_in(self, amount):
		current_balance = self.get_balance()
		self.set_balance(current_balance + amount)

	def pay_monthly_fee(self):
		current_balance = self.get_balance()
		amount = self.rates[self.get_account_type()]
		self.set_balance(current_balance - amount)