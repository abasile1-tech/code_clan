class PetShop:
	def __init__(self, name, cash, pets):
		self.name = name
		self.cash = cash
		self.pets = pets
		self.pets_sold = 0

	def stock_count(self):
		return len(self.pets)

	def increase_total_cash(self, amount):
		self.cash += amount

	def add_pet(self, pet):
		self.pets.append(pet)

	def remove_pet(self, pet):
		self.pets.remove(pet)

	def find_pet_by_name(self, name):
		for pet in self.pets:
			if pet.name == name:
				return pet

	def find_pet_by_name_list_comp(self, name):
		return [pet for pet in self.pets if pet.name == name][0]

	def increase_pets_sold(self):
		self.pets_sold += 1

	def sell_pet(self, name):
		pet = self.find_pet_by_name(name)
		self.increase_total_cash(pet.price)
		self.remove_pet(pet)
		self.increase_pets_sold()
		return pet