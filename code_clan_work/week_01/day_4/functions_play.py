# Given a list of strings,
# print out the length of every string in the list

strings = ["apple", "banana", "orange", "kiwi"]

# for fruit in strings:
# 	print(len(fruit))

def print_length_of_strings(list_of_strings):
	for string in list_of_strings:
		print(len(string))

print(print_length_of_strings(strings))