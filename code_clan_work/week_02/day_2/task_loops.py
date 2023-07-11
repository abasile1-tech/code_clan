# Exercise 1
# Using single list comprehension, and the following list:
ages = [5, 15, 64, 27, 84, 26]
# Return a list of only the odd ages.
def get_odd_ages(ages):
	return[age for age in ages if age % 2 != 0]
print(get_odd_ages(ages))

# Exercise 2
# Using single list comprehension, and the following list:
years = range(2000, 2100)
# Return a list of the leap years in this century.
# Hint: A leap year is one that can be exactly divided by 4 (such as 2016, 2020, 2024, etc), 
# except if it can be exactly divided by 100.
def get_leap_years(years):
	return [year for year in years if year % 4 == 0 and year % 100 != 0]
print(get_leap_years(years))

# Exercise 3
# Using single list comprehension, and the following list:
chicken_names = ["Hen Solo", "Cluck Norris", "Hennifer Lopez", "ChewPekka", "Feather Locklear"]
# Return a list with chickens whose name is more than 10 characters
# Return a list of chickens whose name starts with the letter H
def get_long_names(names):
	return [name for name in names if len(name) > 10]

def get_h_names(names):
	return [name for name in names if name[0] == "H"]
print(get_long_names(chicken_names))
print(get_h_names(chicken_names))

# Exercise 4
# Using a single list comprehension, and the following list:
words = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
# Build a new list, with the first letter from each word
# Convert each letter to lower case
# Expected output: ["t", "q", "b", "f", "j", "o", "t", "l", "d"]
# Hint: Strings in Python work as if they were a tuple full of characters. 
# How would you get the first element from a tuple or list?
def get_first_letter(words):
	return[word[0].lower() for word in words]
print(get_first_letter(words))