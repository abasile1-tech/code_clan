"""
Exercise 1:
Write a program that takes a list of numbers and prints the sum of all the numbers in the list.
"""
def print_sum(numbers):
	print(sum(numbers))

print_sum([5,4,3,2,1])

"""
Exercise 2:
Write a program that takes a list of strings and prints the length of each string in the list.
"""
def print_length(list_of_strings):
	for string in list_of_strings:
		print(len(string))

print_length(["hi","how","johnny"])

"""
Exercise 3:
Write a program that prompts the user to enter 5 names and stores them in a list. Then, print the list in alphabetical order.
HINT: Use a range(5) with a for loop to loop 5 times
HINT: To get user input and store it in a variable: name = input("Enter a name: ") 
"""
def input_names():
	list_of_names = []
	for i in range(5):
		name = input("Please enter a name: ")
		list_of_names.append(name)
	list_of_names.sort()
	print(list_of_names)  
# input_names()
"""
Exercise 4:
Write a program that takes a list of numbers and prints the largest and smallest numbers in the list.
HINT: min and max are built-in Python functions
"""
def print_max_and_min(numbers):
	print(f"largest: {max(numbers)}, smallest: {min(numbers)}")
print_max_and_min([5,4,3,2,1,7,8,9,0,-1])

"""
Exercise 5:
Write a program that takes a list of integers and prints the average of the numbers in the list.
"""
import statistics
def print_avg(integers):
	print(statistics.mean(integers))

print_avg([0,7,9,10,5])
"""
Exercise 6:
Write a program that takes a list of integers and removes all the duplicates, printing the updated list.
HINT: Python's in-built set function will remove duplicates from a list
"""

"""
Exercise 7:
Write a program that prompts the user to enter a sentence and prints the sentence in reverse order.
"""

"""
BONUS CHALLENGE!
Write a program that prompts the user to enter a sentence and counts the frequency of each word in the sentence using a dictionary.
HINT: Python's split() method will turn a set into a List
"""