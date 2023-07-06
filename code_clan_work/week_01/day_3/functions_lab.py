"""
Write each function and test it works by printing a call to the function 
with any required inputs (argument values) and 
checking the output (return value) in your terminal by running:

python3 functions_lab.py

Each docstring (""" """) includes instructions for the function name, 
any parameters it takes, and what it returns

If there is a `pass` in the body of the function, replace it with your own code

Some functions and checks have been started for you!
"""

# === COMPLETED EXAMPLE ==============

"""
return_10 function
takes no parameters
returns the number 10
"""
def return_10():
  return 10

print("------------------------------")
print("By calling return_10, I'm expecting 10, and the result is")
print(return_10())


# === START HERE =====================

"""
add function 
takes the parameters num_1 and num_2
returns the result of adding num_1 and num_2
"""
def add(num_1, num_2):
  return num_1 + num_2

print("------------------------------")
print("By adding 4 and 5, I'm expecting it to be 9, and the result is")
print(add(4, 5))


"""
subtract function
takes the parameters num_1 and num_2
returns the result of subtracting num_2 from num_1
"""
def subtract(num_1, num_2):
  return num_1 - num_2

print("------------------------------")
print("By subtracting 3 from 10, I'm expecting it to be 7, and the result is")
# check by calling the function with the arguments 10 and 3:
print(subtract(10,3))


"""
multiply function
takes the parameters num_1 and num_2
returns the result of multiplying num_1 and num_2
"""
# create the multiply function:
def multiply(num_1, num_2):
	return num_1 * num_2

print("------------------------------")
# replace _ with your own values and expectation:
print("By multiplying 3 and 5, I'm expecting it to be 15, and the result is")
# check by invoking the function with your own values:
print(multiply(3,5))


"""
divide function
takes the parameters num_1 and num_2
returns the resulting of dividing num_1 by num_2
"""
# define the divide function:
def divide(num_1, num_2):
	return num_1/num_2

print("------------------------------")
# replace _ with your own values and expectation:
print("By dividing 15 by 5, I'm expecting it to be 3, and the result is")
# check by calling the function with your own arguments:
print(divide(15,5))


# === NICE! CONTINUE =================

def length_of_string(str):
	"""
	length_of_string function
	takes a parameter str
	returns the length of str (number of characters, including spaces and punctuation)
	"""
	return len(str)

print("------------------------------")
print("By calculating the length of the string 'How now, brown cow?', I'm expecting it to be 19, and the result is")
print(length_of_string('How now, brown cow?'))

def join_string(str_1, str_2):
	"""
	join_string function
	takes the parameters str_1 and str_2
	returns str_1 and str_2 joined as one string
	"""

	return str_1 + " " + str_2

print("------------------------------")
print("By joining the strings 'go do' and 'good', I'm expecting it to be 'go do good', and the result is")
print(join_string('go do', 'good'))

def add_string_as_number(str_1, str_2):
	"""
	add_string_as_number function
	takes the parameters str_1 and str_2
	returns the result of adding str_1 and str_2 as ints
	"""
	return int(str_1) + int(str_2)

print("------------------------------")
print("By adding the strings '58' and '42' as numbers, I'm expecting it to be 100, and the result is")
print(add_string_as_number('58', '42'))



def number_to_full_name(month):
	"""
	number_to_full_name function
	takes a parameter month (int)
	returns the full name of the month
	"""
	match month:
		case 1:
			return "January"
		case 2:
			return "February"
		case 3:
			return "March"
		case 4:
			return "April"
		case 5:
			return "May"
		case 6:
			return "June"
		case 7:
			return "July"
		case 8:
			return "August"
		case 9:
			return "September"
		case 10:
			return "October"
		case 11:
			return "November"
		case 12:
			return "December"

# Sometimes, it's relevant to check the function with different values:
print("------------------------------")
print("By converting 1 to the full month name, I'm expecting it to be 'January', and the result is")
print(number_to_full_name(1))

print("------------------------------")
print("By converting 3 to the full month name, I'm expecting it to be 'March', and the result is")
print(number_to_full_name(3))

print("------------------------------")
print("By converting 9 to the full month name, I'm expecting it to be 'September', and the result is")
print(number_to_full_name(9))



# HINT: Could you use `number_to_full_name` by calling it from within this function?
def number_to_short_month_name(month):
	"""
	number_to_short_month_name function
	takes a parameter month (int)
	returns the short name of the month
	"""
	long_name = number_to_full_name(month)

	return long_name[0:3]

print("------------------------------")
print("By converting 2 to the short month name, I'm expecting it to be 'Feb', and the result is")
print(number_to_short_month_name(2))

print("------------------------------")
print("By converting 4 to the short month name, I'm expecting it to be 'Apr', and the result is")
print(number_to_short_month_name(4))

print("------------------------------")
print("By converting 10 to the short month name, I'm expecting it to be 'Oct', and the result is")
print(number_to_short_month_name(10))


# === EXTENSIONS =====================

def volume_of_cube(length_of_side):
	"""
	volume_of_cube function
	takes a parameter length_of_side
	returns the volume of a cube with that length_of_side
	"""
	return length_of_side ** 3

print("------------------------------")
print("By calculating the volume of a cube with the side of 3, I'm expecting it to be 27, and the result is")
print(volume_of_cube(3))

def string_reverse(str):
	"""
	string_reverse function
	takes a parameter str
	returns the result of reversing the str
	"""
	return str[::-1]

print("------------------------------")
print("By reversing the string 'Scotland', I'm expecting it to be 'dnaltocS', and the result is")
print(string_reverse('Scotland'))


# Write a function that converts fahrenheit to celcius (rounded to 2 decimal places):
def fahrenheit_to_celsius(fahrenheit):
	"""
	fahrenheit_to_celsius function
	takes a parameter fahrenheit
	returns the result of converting fahrenheit to celcius (rounded to 2 decimal places)
	"""
	return round(5/9 * (fahrenheit - 32),2)

print("------------------------------")
print("By converting 0 fahrenheit to celcius, I'm expecting it to be -17.78, and the result is")
print(fahrenheit_to_celsius(0))
