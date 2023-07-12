class River:
	def __init__(self):
		self.stock =[]
	def stock_river(self,fish):
		self.stock.append(fish)
	def remove_fish(self):
		if self.stock[0]:
			return self.stock[0]