my_number = 13

try:
	value = int(input("What number am I thinking of? "))
except ValueError:
	value = int(input("Please enter a number: "))

while (value != my_number):
	try:
		value = (int(input("Nope! Try again...")))
	except ValueError:
		value = (int(input("Please enter a number. Try again...")))