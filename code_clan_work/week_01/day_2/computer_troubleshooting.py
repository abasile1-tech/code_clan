class Computer:
	def __init__(self):
		self.power_button_clicked = False,
		self.plugged_in = False,
		self.is_broken = False
	
	# Did it boot up?
	def check_boot(self):
		# Is it plugged in and did you press the power button?
		if (self.check_plug() and self.check_power_button()):
			# It's not broken
			if not self.check_broken():
				# Ask for password
				self.ask_for_password()
			# It's broken
			else:
				# Ask to fix
				self.ask_to_fix()
		# It's not plugged in
		elif not self.check_plug():
			# Ask to Plug it in
			self.ask_to_plug()
		elif (not self.check_power_button()):
			self.ask_to_push_on_button()
		elif (not self.check_plug()):
			self.ask_to_plug()
		# Yes
		else:
			# Ask for password
			self.ask_for_password()

	# def check_boot(self):
	# 	if (not self.check_plug()):
	# 		self.ask_to_plug()
	# 	elif (not self.check_power_button()):
	# 		self.ask_to_push_on_button()
	# 	elif (self.check_broken):
	# 		self.ask_to_fix()
	# 	else:
	# 		self.ask_for_password

	def check_plug(self):
		if (self.plugged_in == True):
			print("Plugged in")
			return True
		else:
			print("Not plugged in")
			return False
		
	def check_power_button(self):
		if (self.power_button_clicked == True):
			print("Power Button Clicked")
			return True
		else:
			print("Power Button Not Clicked")
			return False
			
	def check_broken(self):
		if (self.is_broken == True):
				print("It's broken")
				return True
		else:
			print("It's not broken.")
			return False

	def ask_to_fix(self):
		fix_it = input("Would you like to fix it? y/n: ")
		if (fix_it == "y"):
			self.fix_it()
			print("you fixed it")
			self.check_boot()

	def ask_for_password(self):
		password = input(f"Please enter your password: ")

	def power_on(self):
		self.power_button_clicked = True
		print("you powered it on")
		self.check_boot()
	  
	def plug_in(self):
		self.plugged_in = True
		print("you plugged it in")
		self.check_boot()

	def ask_to_plug(self):
		plug_in = input("Would you like to plug it in? y: ")
		if (plug_in == "y"):
			self.plug_in()

	def ask_to_push_on_button(self):
		power_on = input("Would you like to power it on? y: ")
		if (power_on == "y"):
			self.power_on()

	def break_it(self):
		self.is_broken = True

	def fix_it(self):
		self.is_broken = False

my_pc = Computer()

my_pc.check_boot()

my_pc.break_it()
print("\nyou broke your pc")

my_pc.check_boot()

other_pc = Computer()
other_pc.power_button_clicked = True
other_pc.plugged_in = True
other_pc.isBroken = False

print("\nchecking the other pc")
other_pc.check_boot()



